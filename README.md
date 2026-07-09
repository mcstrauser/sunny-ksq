# Sunny KSQ

A resident-led advocacy timeline for the Kennett Township municipal facility
expansion. Live site: **https://mcstrauser.github.io/sunny-ksq/**

## What's here

- **`index.html`** — the entire site. A single self-contained page (HTML + CSS +
  vanilla JS, no build step). All content lives in the data arrays near the top
  of the `<script>` block: `EVENTS`, `STATS`, `ASKS`, `RESOURCES`, `GOALS`.
- **`assets/`** — logos and icons.
- **`documents/`** — PDFs and other files to host and link from the page. See
  [`documents/README.md`](documents/README.md).

## Editing content

Open `index.html` and edit the relevant data array. For example, to add a
timeline event, add an object to `EVENTS`; to add a resource card, add to
`RESOURCES`. Save, commit, and push — GitHub Pages redeploys automatically
within a minute or two.

## Publishing

The site is served by GitHub Pages from the `main` branch root. Any push to
`main` updates the live site.
