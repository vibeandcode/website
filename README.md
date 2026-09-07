# vibeandcode.com

The vibe&code studio site: home, SealDocs, support and the SealDocs legal pages.
Plain static HTML on Vercel, no framework, no dependencies beyond Python 3.

The FeelScape site lives in `feelscape/` and is **not** authored here. It is the
build output of the separate FeelScape Astro project, copied in wholesale
(see that project's README → Deployment).

## Editing

The HTML pages are generated, so edit the sources and rebuild:

| File | What it holds |
| --- | --- |
| `_shell.py` | Shared chrome: `<head>`, nav, footer, the menu + reveal script, inline SVG icons |
| `_pages.py` | Page bodies and copy for home, SealDocs and support |
| `_content/` | Text carried over verbatim: the SealDocs legal pages and its JSON-LD |
| `site.css` | The stylesheet. Tokens mirror FeelScape's `src/styles/global.css` so both sites read as one family |
| `assets/` | SealDocs icon and Sealy mascot (from the app repo), studio favicon |

```sh
python3 build.py
```

writes `index.html`, `sealdocs.html`, `support.html`, `sealdocs-privacy.html`
and `sealdocs-terms.html`. Commit the output along with the sources; Vercel
serves the files as they are.

## Site-wide files

- `robots.txt` — governs the whole host, including FeelScape. Lists both sitemaps.
- `sitemap.xml` — this site's pages only. FeelScape's is generated at `feelscape/sitemap-index.xml`.
- `vercel.json` — `trailingSlash: true` (matching the FeelScape build) and the 301s from the retired `feelscape*.html` pages.

## Facts, not filler

Nothing on the site states a number, rating or claim that isn't true today.
SealDocs is "coming soon" until it is actually in the stores; FeelScape's facts
come from its own site. Keep it that way.
