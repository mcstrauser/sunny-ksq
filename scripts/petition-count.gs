/**
 * Sunny KSQ — petition signature count endpoint
 * ---------------------------------------------
 * Returns ONLY the number of form responses as JSON: {"count": 64}
 * The responses spreadsheet stays private — no names, emails, or addresses
 * are ever exposed. Only the total is returned.
 *
 * SETUP
 * 1. Open the Google Sheet that holds your form responses.
 *    (In the Form: Responses tab → the green Sheets icon → "Link to Sheets".)
 * 2. In that Sheet: Extensions → Apps Script.
 * 3. Delete anything there, paste this whole file, and Save.
 * 4. If your responses tab is NOT named "Form Responses 1", change SHEET_NAME
 *    below to match (or leave it — the script falls back to the first tab).
 * 5. Deploy → New deployment → gear icon → "Web app".
 *      - Description:      petition count
 *      - Execute as:       Me
 *      - Who has access:   Anyone
 *    Click Deploy, authorize when prompted, and copy the "Web app URL"
 *    (it looks like https://script.google.com/macros/s/AKfy.../exec ).
 * 6. Send that URL to Claude — it goes into PETITION_COUNT_URL in index.html.
 *
 * UPDATING: if you ever edit this script, redeploy with
 * Deploy → Manage deployments → edit (pencil) → Version: New version → Deploy.
 * The Web app URL stays the same.
 */

var SHEET_NAME = 'Form Responses 1';

function doGet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
  // getLastRow() includes the header row, so subtract 1 for the signature total.
  var count = Math.max(0, sheet.getLastRow() - 1);
  return ContentService
    .createTextOutput(JSON.stringify({ count: count }))
    .setMimeType(ContentService.MimeType.JSON);
}
