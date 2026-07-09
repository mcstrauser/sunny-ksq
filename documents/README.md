# Documents

Drop PDFs (or other files) you want to host and link from the site into this folder.

Once a file is committed and pushed, it's served at:

```
https://mcstrauser.github.io/sunny-ksq/documents/<your-file-name>.pdf
```

## Tips

- **Use simple file names** — lowercase, dashes instead of spaces, e.g.
  `feasibility-study-2025.pdf`, not `Feasibility Study (final) v2.pdf`.
  Spaces and special characters make for ugly, fragile links.
- Anything in this folder is **public** once pushed — don't add files you
  don't want the world to see.

## How to link a document from the page

The site is a single `index.html` at the repo root. To add a document link,
add an entry to the relevant data array near the top of the `<script>` block:

**As a Resources card** — add to the `RESOURCES` array:

```js
{ kind:"Township record", title:"GKO Feasibility Study",
  desc:"The full 2025 feasibility study PDF.",
  href:"documents/feasibility-study-2025.pdf" },
```

**As a document chip on a timeline event** — add to that event's `docs` array:

```js
docs: [ { label:"Feasibility study (PDF)", href:"documents/feasibility-study-2025.pdf", icon:"▤" } ]
```

Relative paths like `documents/feasibility-study-2025.pdf` work both locally
and on the live site. Just tell Claude which document goes where and it can
wire the links for you.
