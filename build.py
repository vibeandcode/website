#!/usr/bin/env python3
"""Assemble the vibe&code static pages from _shell.py, _pages.py and _content/.

No dependencies beyond Python 3. Output files are committed alongside the
sources so Vercel serves them as plain static HTML. Run after any edit:

    python3 build.py

_content/ holds text that is carried over verbatim rather than authored in
_pages.py: the SealDocs legal pages and its structured data. Edit those files
directly. The build never reads its own output, so it can be re-run freely.
"""
from pathlib import Path

from _shell import head, nav, footer, scripts
import _pages as P

ROOT = Path(__file__).parent
CONTENT = ROOT / "_content"


def write(name, html):
    (ROOT / name).write_text(html)
    print(f"wrote {name} ({len(html.encode()) // 1024} KB)")


def content(name):
    return (CONTENT / name).read_text()


ORG_LD = ('    <script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization",'
          '"name":"vibe&code","url":"https://vibeandcode.com","email":"vibeandcode@gmail.com",'
          '"description":"An independent studio making calm, private apps for iPhone and Android."}</script>')

# Home
write("index.html",
      head(P.HOME_TITLE, P.HOME_DESC, "/", extra=ORG_LD)
      + nav("/") + P.HOME + footer() + scripts())

# SealDocs, with its SoftwareApplication + FAQPage structured data
write("sealdocs.html",
      head(P.SD_TITLE, P.SD_DESC, "/sealdocs.html", P.SD_OG_TITLE, P.SD_OG_DESC, extra=content("sealdocs-jsonld.html"))
      + nav("/sealdocs.html") + P.SEALDOCS + footer("SealDocs is a vibe&amp;code creation.") + scripts())

# Support
write("support.html",
      head(P.SUPPORT_TITLE, P.SUPPORT_DESC, "/support.html")
      + nav("/support.html") + P.SUPPORT + footer()
      + scripts().replace("</body>", P.SUPPORT_SCRIPT + "</body>"))

# Legal pages: new chrome, same words
for name, title, desc in [
    ("sealdocs-privacy.html", "Privacy Policy | SealDocs", "How SealDocs handles your documents and data. Local-first, encrypted on your device."),
    ("sealdocs-terms.html", "Terms of Service | SealDocs", "The terms for using the SealDocs app."),
]:
    write(name,
          head(title, desc, "/" + name)
          + nav("/sealdocs.html")
          + f'    <section class="legal"><div class="container container-narrow">\n{content(name)}    </div></section>\n'
          + footer("SealDocs is a vibe&amp;code creation.") + scripts())
