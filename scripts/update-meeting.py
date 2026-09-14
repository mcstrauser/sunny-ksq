#!/usr/bin/env python3
"""Refresh meeting.json with the next Board of Supervisors meeting.

Reads the Township's CivicPlus calendar RSS feed and writes the earliest
upcoming "Board of Supervisors" event. The page can't fetch the feed itself
(the Township server sends no CORS headers), so a scheduled GitHub Action runs
this and commits meeting.json when it changes.
"""
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

FEED = "https://www.kennett.pa.us/RSSFeed.aspx?ModID=58&CID=All-calendar.xml"
NS = {"ce": "https://www.kennett.pa.us/Calendar.aspx"}
OUT = pathlib.Path(__file__).resolve().parent.parent / "meeting.json"
TZ = ZoneInfo("America/New_York")


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "sunnyksq-meeting-sync"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())

    today = dt.datetime.now(TZ).date()
    found = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        if "board of supervisors" not in title.lower():
            continue
        m = re.search(r"[A-Z][a-z]+ \d{1,2}, \d{4}", item.findtext("ce:EventDates", "", NS))
        if not m:
            continue
        day = dt.datetime.strptime(m.group(0), "%B %d, %Y").date()
        if day < today:
            continue
        t = re.match(r"\s*(\d{1,2}:\d{2} [AP]M)", item.findtext("ce:EventTimes", "", NS))
        time = dt.datetime.strptime(t.group(1), "%I:%M %p").strftime("%H:%M") if t else "19:00"
        found.append({"date": day.isoformat(), "time": time, "title": title,
                      "link": (item.findtext("link") or "").strip()})

    if not found:
        print("No upcoming Board of Supervisors meeting in feed; leaving meeting.json as is.")
        return 0

    nxt = min(found, key=lambda e: (e["date"], e["time"]))
    new = json.dumps(nxt, indent=2) + "\n"
    if OUT.exists() and OUT.read_text() == new:
        print("meeting.json unchanged:", nxt["date"])
        return 0
    OUT.write_text(new)
    print("meeting.json updated:", nxt["date"], nxt["time"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
