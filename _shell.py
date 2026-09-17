"""Shared page chrome for the vibe&code static site.

Each page file calls `head(...)`, `nav(...)`, `footer(...)` and `scripts()` so
the header, footer and behaviours stay identical across pages without a build
step. Run `python3 build.py` after editing a page module or this file.
"""

SITE = "https://vibeandcode.com"
EMAIL = "vibeandcode@gmail.com"
YEAR = 2026

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

WORDMARK = '<a href="/" class="wordmark" aria-label="vibe&amp;code home">vibe<em>&amp;</em>code</a>'

ICONS = {
    "check": '<svg fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>',
    "apple": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3.609 1.814L13.792 12 3.61 22.186a.996.996 0 01-.61-.92V2.734a1 1 0 01.609-.92zm10.89 10.893l2.302 2.302-10.937 6.333 8.635-8.635zm3.199-3.199l2.302 2.302a1 1 0 010 1.38l-2.302 2.302L15.396 12l2.302-2.492zM5.864 2.658L16.8 8.99l-2.302 2.302L5.864 2.658z"/></svg>',
    "mail": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l9 6 9-6M4 6h16a1 1 0 011 1v10a1 1 0 01-1 1H4a1 1 0 01-1-1V7a1 1 0 011-1z"/></svg>',
    "clock": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path stroke-linecap="round" d="M12 7v5l3 2"/></svg>',
    "camera": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "users": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path stroke-linecap="round" d="M2.5 20c.6-3.6 3.3-5.5 6.5-5.5s5.9 1.9 6.5 5.5M16 4.5a3.5 3.5 0 010 7M21.5 20c-.4-2.6-1.9-4.3-4-5"/></svg>',
    "bell": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M6 16V11a6 6 0 1112 0v5l2 2H4l2-2zM10 20a2 2 0 004 0"/></svg>',
    "seal": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6l7-3z"/><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/></svg>',
    "lock": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path stroke-linecap="round" d="M8 11V8a4 4 0 118 0v3"/></svg>',
    "export": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4v12m0-12l-4 4m4-4l4 4M4 15v3a2 2 0 002 2h12a2 2 0 002-2v-3"/></svg>',
    "spark": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3zM5 18l.7 1.8L7.5 20.5l-1.8.7L5 23l-.7-1.8-1.8-.7 1.8-.7L5 18z"/></svg>',
    "heart": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/></svg>',
    "hand": '<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12V5.5a1.5 1.5 0 013 0V11m0-6.5V4a1.5 1.5 0 013 0v7m0-5.5a1.5 1.5 0 013 0V12m0-2a1.5 1.5 0 013 0v5a6 6 0 01-6 6h-1.5a6 6 0 01-5-2.7L4 14a1.6 1.6 0 012.5-2L8 13.5"/></svg>',
    "plus": '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M12 5v14M5 12h14"/></svg>',
    "menu": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "close": '<svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M6 18L18 6M6 6l12 12"/></svg>',
}


def check(text):
    return f'<li>{ICONS["check"]}{text}</li>'


def head(title, description, path, og_title=None, og_desc=None, extra=""):
    canonical = SITE + path
    og_title = og_title or title
    og_desc = og_desc or description
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <!-- Google Search Console ownership, one token per property (also set in
         the FeelScape site's BaseLayout) -->
    <meta name="google-site-verification" content="gw_3Ca-UQc2DjiyHfWBnK0FZyEdbZBNoo_NvPrGSXkQ">
    <meta name="google-site-verification" content="V8AIMkkVxl_7GxqgDzSyBO-XaUtjMIFE-FvMp14fZXE">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="vibe&code">
    <meta name="robots" content="index, follow">
    <meta name="theme-color" content="#FBF9F7">
    <link rel="canonical" href="{canonical}">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">

    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical}">
    <meta property="og:site_name" content="vibe&code">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_desc}">
{extra}
    {FONTS}
    <link rel="stylesheet" href="/site.css">
</head>
<body>
    <a href="#main" class="skip">Skip to content</a>
"""


NAV_LINKS = [("/#apps", "Apps"), ("/#about", "About"), ("/sealdocs.html", "SealDocs"), ("/feelscape/", "FeelScape"), ("/support.html", "Support")]


def nav(current=""):
    links = "".join(
        f'\n                <a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV_LINKS
    )
    mobile = "".join(f'\n                <a href="{href}">{label}</a>' for href, label in NAV_LINKS)
    return f"""    <header class="nav">
        <div class="container nav-inner">
            {WORDMARK}
            <nav class="nav-links" aria-label="Main navigation">{links}
            </nav>
            <div class="nav-right">
                <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-mobile">
                    <span id="menu-icon">{ICONS["menu"]}</span>
                    <span id="close-icon" hidden>{ICONS["close"]}</span>
                </button>
            </div>
        </div>
        <div class="nav-mobile" id="nav-mobile">
            <nav aria-label="Mobile navigation">{mobile}
            </nav>
        </div>
    </header>
    <main id="main">
"""


def footer(note=None):
    note = note or "vibe&amp;code is an independent studio. FeelScape and SealDocs are its apps."
    return f"""    </main>
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    {WORDMARK}
                    <p>Small, careful apps for iPhone and Android, made by one person who reads every email.</p>
                </div>
                <div>
                    <h4>Apps</h4>
                    <ul>
                        <li><a href="/feelscape/">FeelScape</a></li>
                        <li><a href="/sealdocs.html">SealDocs</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Studio</h4>
                    <ul>
                        <li><a href="/#about">About</a></li>
                        <li><a href="/support.html">Support</a></li>
                        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="/feelscape/privacy/">FeelScape privacy</a></li>
                        <li><a href="/feelscape/terms/">FeelScape terms</a></li>
                        <li><a href="/sealdocs-privacy.html">SealDocs privacy</a></li>
                        <li><a href="/sealdocs-terms.html">SealDocs terms</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© {YEAR} vibe&amp;code. {note}</p>
                <p><a href="/support.html">Support</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            </div>
        </div>
    </footer>
"""


SCRIPTS = """    <script>
    (() => {
        document.documentElement.classList.add('js');
        // Mobile menu
        const btn = document.getElementById('nav-toggle'), menu = document.getElementById('nav-mobile');
        const mi = document.getElementById('menu-icon'), ci = document.getElementById('close-icon');
        btn?.addEventListener('click', () => {
            const open = menu.classList.toggle('open');
            btn.setAttribute('aria-expanded', String(open));
            mi.hidden = open; ci.hidden = !open;
        });
        // Reveal on scroll. Everything is visible without JS, and as a safety
        // net everything is revealed after 1.5s regardless, so landing on an
        // anchor like /#about never leaves the sections above it blank.
        const els = document.querySelectorAll('.reveal');
        const showAll = () => els.forEach((el) => el.classList.add('in'));
        if (els.length && 'IntersectionObserver' in window) {
            const io = new IntersectionObserver((entries) => {
                entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
            }, { rootMargin: '0px 0px -6% 0px', threshold: 0.02 });
            els.forEach((el) => io.observe(el));
            setTimeout(showAll, 1500);
        } else {
            showAll();
        }
    })();
    </script>
</body>
</html>
"""


def scripts():
    return SCRIPTS
