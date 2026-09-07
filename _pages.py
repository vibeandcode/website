"""Page bodies for the vibe&code site. See build.py."""
from _shell import ICONS, EMAIL, check

# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

HOME_TITLE = "vibe&code | Calm, private apps for iPhone and Android"
HOME_DESC = "vibe&code is a one-person studio making small, careful apps. FeelScape writes affirmations for how you feel. SealDocs keeps your documents safe on your device."

HOME = f"""
    <section class="hero bg-sky" aria-label="Introduction">
        <div class="drift" style="top:-160px;left:-160px;width:540px;height:540px;background:color-mix(in srgb, var(--lavender) 30%, transparent)"></div>
        <div class="drift" style="top:40px;right:-180px;width:520px;height:520px;background:color-mix(in srgb, var(--peach) 70%, transparent);animation-delay:-8s"></div>
        <div class="drift" style="bottom:-200px;left:33%;width:600px;height:600px;background:color-mix(in srgb, var(--mint) 60%, transparent);animation-delay:-14s"></div>

        <div class="container hero-inner">
            <div class="hero-copy fade-up">
                <span class="pill glass"><span class="dot"></span>An independent app studio</span>
                <h1 class="display h1">Small apps, <span class="gradient-text">made with care.</span></h1>
                <p class="lead">vibe&amp;code is a one-person studio building calm, private apps for iPhone and Android. No growth hacks, no dark patterns. Just software that does one thing well and then gets out of your way.</p>
                <div class="btn-row">
                    <a href="#apps" class="btn btn-primary">See the apps</a>
                    <a href="/support.html" class="btn btn-ghost">Say hello</a>
                </div>
                <ul class="checks">
                    {check("Free to start")}
                    {check("Private by default")}
                    {check("Made by a person you can email")}
                </ul>
            </div>

            <div class="hero-visual fade-up" style="animation-delay:120ms">
                <div class="phone float">
                    <img src="/feelscape/images/screenshots/screen-4-640.webp"
                         srcset="/feelscape/images/screenshots/screen-4-640.webp 640w, /feelscape/images/screenshots/screen-4-1080.webp 1080w"
                         sizes="(min-width: 1000px) 420px, 80vw" width="640" height="1270"
                         alt="FeelScape showing an affirmation written for the user's mood" fetchpriority="high" decoding="async">
                </div>
                <div class="float-card glass float tl" style="animation-delay:-2.5s" aria-hidden="true">
                    <div class="meta"><img src="/feelscape/images/logo/feelscape-icon-96.png" alt="" width="20" height="20">FeelScape · Anxious · 9:12 am</div>
                    <p>Right now, in this breath, I am safe.</p>
                </div>
                <div class="float-card glass float br" style="animation-delay:-4.5s" aria-hidden="true">
                    <div class="meta"><img src="/assets/sealdocs-icon-96.png" alt="" width="20" height="20">SealDocs · Passport</div>
                    <p>Expires in 42 days. Renewal usually takes three weeks.</p>
                    <div class="bar"><i></i></div>
                </div>
            </div>
        </div>
    </section>

    <section id="apps" class="section" aria-labelledby="apps-heading">
        <div class="container">
            <div class="section-head reveal">
                <p class="eyebrow">The apps</p>
                <h2 id="apps-heading" class="display h2">Two so far. Both built the same way.</h2>
                <p class="lead" style="margin-top:14px">Quiet on the outside, careful on the inside. Each one started as something I wanted for myself.</p>
            </div>

            <article class="card card-hover app-card reveal">
                <div class="app-card-body">
                    <div class="app-head">
                        <img src="/feelscape/images/logo/feelscape-icon.png" alt="" width="64" height="64" class="app-icon">
                        <div>
                            <h3 class="h3" style="font-size:1.35rem">FeelScape</h3>
                            <p class="sub">Free on iOS and Android</p>
                        </div>
                    </div>
                    <h4 class="display h2">Affirmations written for exactly how you feel.</h4>
                    <p class="lead">Log your mood in 30 seconds and get affirmations written for that feeling, on that day, by an AI that remembers what you tell it. No streaks, no guilt, no quote library.</p>
                    <div class="tags">
                        <span class="tag teal">Mood tracker</span><span class="tag teal">AI affirmations</span><span class="tag teal">50 moods</span><span class="tag teal">37 languages</span>
                    </div>
                    <div class="btn-row" style="margin-top:6px">
                        <a href="/feelscape/" class="btn btn-brand">Explore FeelScape</a>
                        <a href="/feelscape/download/" class="text-link">Download free →</a>
                    </div>
                </div>
                <div class="app-card-media fs">
                    <div class="phone">
                        <img src="/feelscape/images/screenshots/screen-2-640.webp" width="640" height="1270" alt="FeelScape mood picker with coloured mood circles" loading="lazy" decoding="async">
                    </div>
                </div>
            </article>

            <article class="card card-hover app-card flip reveal" style="margin-top:24px">
                <div class="app-card-body">
                    <div class="app-head">
                        <img src="/assets/sealdocs-icon.png" alt="" width="64" height="64" class="app-icon">
                        <div>
                            <h3 class="h3" style="font-size:1.35rem">SealDocs</h3>
                            <p class="sub">Coming soon to iOS and Android</p>
                        </div>
                    </div>
                    <h4 class="display h2">A private vault for the documents that matter.</h4>
                    <p class="lead">Passports, insurance, pet records, licences. Stored encrypted on your device, organised by person, with a reminder before anything expires. Nothing leaves your phone unless you say so.</p>
                    <div class="tags">
                        <span class="tag pink">Document vault</span><span class="tag pink">Local-first</span><span class="tag pink">Expiry reminders</span><span class="tag pink">37+ document types</span>
                    </div>
                    <div class="btn-row" style="margin-top:6px">
                        <a href="/sealdocs.html" class="btn btn-pink">Meet SealDocs</a>
                        <a href="/sealdocs.html#faq" class="text-link pink">Read the FAQ →</a>
                    </div>
                </div>
                <div class="app-card-media sd">
                    <img src="/assets/sealy-waving.png" width="480" height="480" alt="Sealy, the SealDocs mascot, waving" class="sealy" loading="lazy" decoding="async">
                </div>
            </article>
        </div>
    </section>

    <section id="about" class="section bg-elevated" aria-labelledby="about-heading">
        <div class="container">
            <div class="section-head reveal">
                <p class="eyebrow">How things get made here</p>
                <h2 id="about-heading" class="display h2">A few rules I don't break.</h2>
            </div>
            <div class="grid grid-4">
                <div class="card card-pad principle reveal">
                    <span class="n">01 — Feel first</span>
                    <h3 class="h3">Start with how it should feel</h3>
                    <p>Every app begins with the moment someone opens it. The code follows that, not the other way round.</p>
                </div>
                <div class="card card-pad principle reveal">
                    <span class="n">02 — Private by default</span>
                    <h3 class="h3">Your data stays yours</h3>
                    <p>SealDocs keeps documents on your device. FeelScape never sells your moods. Anything that leaves your phone is something you chose.</p>
                </div>
                <div class="card card-pad principle reveal">
                    <span class="n">03 — No guilt</span>
                    <h3 class="h3">No streaks, no nagging</h3>
                    <p>FeelScape dropped streaks on purpose. An app should be glad to see you, not keep score of when you left.</p>
                </div>
                <div class="card card-pad principle reveal">
                    <span class="n">04 — One person</span>
                    <h3 class="h3">Real replies</h3>
                    <p>Every support email lands with the person who built the app. Usually answered within a day or two.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" aria-label="Philosophy">
        <div class="container container-narrow" style="text-align:center">
            <p class="quote reveal">“Good software comes from thinking about the person on the other side of the screen, not about the software.”</p>
            <p class="quote-by reveal">The only mission statement this studio has</p>
        </div>
    </section>

    <section class="section section-tight" aria-labelledby="cta-heading">
        <div class="container">
            <div class="cta-card bg-dawn reveal">
                <div class="drift" style="top:-100px;right:-100px;width:320px;height:320px;background:color-mix(in srgb, var(--lavender) 30%, transparent)"></div>
                <div class="drift" style="bottom:-100px;left:-60px;width:280px;height:280px;background:color-mix(in srgb, var(--teal) 25%, transparent);animation-delay:-9s"></div>
                <div class="inner">
                    <h2 id="cta-heading" class="display h2">Questions, ideas, bugs?</h2>
                    <p class="lead">Write to <a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a>. It reaches the person who made the apps, and replies usually take a day or two.</p>
                    <div class="btn-row center">
                        <a href="/support.html" class="btn btn-primary">Get in touch</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# --------------------------------------------------------------------------
# SealDocs
# --------------------------------------------------------------------------

SD_TITLE = "SealDocs | Privacy-First Document Vault App"
SD_DESC = "Store, organize, and track your critical documents securely. SealDocs keeps everything encrypted on your device — passports, IDs, insurance, pet records, and more. Smart expiry reminders. Coming soon to iOS and Android."
SD_OG_TITLE = "SealDocs — Your Documents, Secured & Organized"
SD_OG_DESC = "Privacy-first document vault. Store, organize, and track expiry dates for passports, IDs, insurance, and more. Encrypted locally on your device."

SD_FEATURES = [
    ("clock", "pink", "Smart expiry tracking", "Automatic reminders at 90, 30 and 7 days before expiry. Colour-coded urgency, so you always know what needs attention first."),
    ("spark", "blue", "Sealy, the assistant", "Ask “Am I ready for Japan?” and get source-backed answers based on your actual documents. A concierge for your paperwork."),
    ("users", "lav", "Profiles for everyone", "Organise documents for the whole household. Family members, pets and businesses each get their own vault."),
    ("camera", "gold", "Scan and go", "Point, scan, done. On-device text recognition detects the document type and pulls out the key details. No cloud processing needed."),
    ("lock", "pink", "Biometric lock", "Face ID and Touch ID protection. Your vault stays locked until you say otherwise."),
    ("export", "blue", "Your data, portable", "Export the vault as JSON or PDF at any time. Import from backups. It is always yours to take with you."),
]

SD_CATEGORIES = [
    ("Personal", "11 types", "#4A90D9"), ("Vehicle", "5 types", "#E17055"), ("Household", "5 types", "#FDCB6E"), ("Financial", "3 types", "#0984E3"),
    ("Family", "1 type", "#E84393"), ("Pet", "5 types", "#7ED321"), ("Business", "5 types", "#2D3436"), ("Subscriptions", "5 types", "#6C5CE7"),
]

SD_FAQ = [
    ("What is SealDocs?", "SealDocs is a privacy-first document vault app that helps you securely store, organize, and track expiry dates for critical documents like passports, IDs, insurance cards, pet records, and business licenses. Everything is encrypted locally on your device — your documents never leave your phone unless you explicitly choose to use cloud features."),
    ("Is my data really private?", "Yes. All documents are stored in an encrypted SQLite database on your device. Nothing leaves your phone unless you explicitly opt in to cloud features like backup or AI assistant. We don't sell or share your data with third parties, and there's no cross-app tracking or fingerprinting. Period."),
    ("What types of documents can I store?", "SealDocs supports 37+ document types across 8 categories: Personal (passports, IDs, visas, health insurance), Vehicle (car insurance, registration, inspection), Household (rental contracts, utilities), Financial (credit cards, loans), Family (school enrollment), Pet (vaccinations, microchip, pet passport), Business (licenses, tax registration), and Subscriptions (memberships, domains, SaaS)."),
    ("Is SealDocs free to use?", "Yes! SealDocs is free to download and use with 1 profile and up to 5 documents. A premium subscription unlocks unlimited documents, unlimited profiles (family, pets, businesses), the AI assistant Sealy, cloud backup, data export, and more."),
    ("Who is Sealy?", "Sealy is SealDocs' friendly AI assistant — a cute seal character that acts as your personal document concierge. Ask Sealy questions like \"Am I ready for Japan?\" or \"When does Luna's vaccination expire?\" and get source-backed answers based on your actual documents. Sealy also sends smart reminders and celebrates when you're all caught up."),
    ("Does SealDocs work offline?", "Yes. Since all documents are stored locally on your device in an encrypted database, you can access your entire vault without an internet connection. Cloud features like backup and the AI assistant require connectivity, but your core vault is always available — even on a plane or in a remote area."),
    ("Can I export or delete my data?", "Absolutely. Premium users can export their entire vault as JSON or PDF at any time. You can also delete all your data from the settings with a single action. Your data is always yours — we believe in giving you full control, no questions asked."),
]


def _features():
    out = []
    for icon, tone, title, text in SD_FEATURES:
        out.append(f"""                <div class="card card-pad feature reveal">
                    <span class="icon {tone}">{ICONS[icon]}</span>
                    <h3 class="h3">{title}</h3>
                    <p>{text}</p>
                </div>""")
    return "\n".join(out)


def _categories():
    return "\n".join(
        f"""                <div class="card chip reveal"><span class="sw" style="background:{c}"></span><span class="name">{n}</span><span class="count">{k}</span></div>"""
        for n, k, c in SD_CATEGORIES
    )


def _faq():
    return "\n".join(
        f"""                <details{' open' if i == 0 else ''}>
                    <summary><span>{q}</span><span class="plus">{ICONS["plus"]}</span></summary>
                    <div class="answer">{a}</div>
                </details>"""
        for i, (q, a) in enumerate(SD_FAQ)
    )


SEALDOCS = f"""
    <section class="hero bg-blush" aria-label="SealDocs overview">
        <div class="drift" style="top:-160px;left:-160px;width:520px;height:520px;background:color-mix(in srgb, var(--sd-pink) 22%, transparent)"></div>
        <div class="drift" style="top:60px;right:-180px;width:520px;height:520px;background:color-mix(in srgb, var(--sd-blue) 30%, transparent);animation-delay:-8s"></div>

        <div class="container hero-inner">
            <div class="hero-copy fade-up">
                <span class="pill glass"><span class="dot pink"></span>SealDocs · Coming soon</span>
                <h1 class="display h1">Your documents. Your device. <span class="gradient-text-pink">Always secure.</span></h1>
                <p class="lead">Store, organise and track expiry dates for the documents that matter. <strong>Encrypted locally</strong>, so nothing leaves your phone unless you say so.</p>
                <div class="btn-row">
                    <span class="store soon">{ICONS["apple"]}<span><span class="top">Coming soon on the</span><span class="name">App Store</span></span></span>
                    <span class="store soon">{ICONS["play"]}<span><span class="top">Coming soon on</span><span class="name">Google Play</span></span></span>
                </div>
                <ul class="checks pink">
                    {check("37+ document types")}
                    {check("Encrypted on your device")}
                    {check("Free to start")}
                </ul>
            </div>

            <div class="hero-visual fade-up" style="animation-delay:120ms;max-width:360px">
                <img src="/assets/sealdocs-icon.png" width="256" height="256" alt="SealDocs app icon: Sealy the seal holding a document" class="float" style="width:72%;margin:0 auto;border-radius:22%;box-shadow:var(--shadow-lift)">
                <div class="float-card glass float bl" style="animation-delay:-3s" aria-hidden="true">
                    <div class="meta"><i style="background:#4A90D9"></i>Passport · Personal</div>
                    <p>Expires in 42 days. Time to renew.</p>
                    <div class="bar"><i></i></div>
                </div>
                <div class="float-card glass float tr" style="animation-delay:-5s" aria-hidden="true">
                    <div class="meta"><i style="background:#7ED321"></i>Luna · Pet vaccination</div>
                    <p>All up to date. Sealy is napping.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" aria-labelledby="how-heading">
        <div class="container">
            <div class="section-head reveal">
                <p class="eyebrow pink">How it works</p>
                <h2 id="how-heading" class="display h2">Three steps. Thirty seconds.</h2>
            </div>
            <div class="grid grid-3">
                <div class="card card-pad feature reveal">
                    <span class="step-num">01</span>
                    <h3 class="h3">Scan it</h3>
                    <p>Point your camera at any document. SealDocs detects the type and extracts the key details with on-device text recognition. No cloud required.</p>
                </div>
                <div class="card card-pad feature reveal">
                    <span class="step-num">02</span>
                    <h3 class="h3">File it by person</h3>
                    <p>Profiles for family members, pets and businesses. Every document lands in the right place, sorted by person, category and urgency.</p>
                </div>
                <div class="card card-pad feature reveal">
                    <span class="step-num">03</span>
                    <h3 class="h3">Hear about it early</h3>
                    <p>Reminders 90, 30 and 7 days before anything expires. Passport renewal, insurance lapse, a pet's vaccination. You will know in time.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-elevated" aria-labelledby="privacy-heading">
        <div class="container">
            <div class="grid grid-2" style="align-items:center;gap:44px">
                <div class="reveal">
                    <p class="eyebrow pink">Your documents, your device</p>
                    <h2 id="privacy-heading" class="display h2">Privacy that actually means something.</h2>
                    <p class="lead" style="margin-top:18px">Most apps put your sensitive documents on their servers. SealDocs was built local-first from the start: passports, IDs and records are encrypted and stored on your phone, not somewhere you don't control. Cloud features are optional and always explicit.</p>
                </div>
                <div class="card card-pad reveal">
                    <ul class="checklist">
                        <li>{ICONS["check"]}<span>Encrypted local SQLite database</span></li>
                        <li>{ICONS["check"]}<span>Biometric lock (Face ID / Touch ID)</span></li>
                        <li>{ICONS["check"]}<span>No cross-app tracking or fingerprinting</span></li>
                        <li>{ICONS["check"]}<span>Cloud OCR is per-image opt-in only</span></li>
                        <li>{ICONS["check"]}<span>Export or delete all data at any time</span></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section" aria-labelledby="features-heading">
        <div class="container">
            <div class="section-head reveal">
                <p class="eyebrow pink">Features</p>
                <h2 id="features-heading" class="display h2">Everything you need to stay organised.</h2>
            </div>
            <div class="grid grid-3">
{_features()}
            </div>
        </div>
    </section>

    <section class="section bg-elevated" aria-labelledby="categories-heading">
        <div class="container">
            <div class="section-head reveal">
                <p class="eyebrow pink">37+ document types</p>
                <h2 id="categories-heading" class="display h2">Because life is complicated.</h2>
                <p class="lead" style="margin-top:14px">From passports to pet vaccinations, there is a place for every document that matters.</p>
            </div>
            <div class="chip-grid">
{_categories()}
            </div>
        </div>
    </section>

    <section class="section" aria-label="Why SealDocs exists">
        <div class="container container-narrow" style="text-align:center">
            <img src="/assets/sealy-happy.png" width="120" height="120" alt="" class="reveal" style="margin:0 auto 20px;width:120px" loading="lazy">
            <p class="quote reveal">“Life runs on documents. People don't fail to track them because they don't care. They fail because information is fragmented, deadlines are invisible, and retrieval happens under stress. SealDocs exists to fix that.”</p>
            <p class="quote-by reveal">Why SealDocs was made</p>
        </div>
    </section>

    <section id="faq" class="section section-tight bg-elevated" aria-labelledby="faq-heading">
        <div class="container container-narrow">
            <div class="section-head reveal">
                <p class="eyebrow pink">FAQ</p>
                <h2 id="faq-heading" class="display h2">Frequently asked questions</h2>
            </div>
            <div class="card faq reveal">
{_faq()}
            </div>
        </div>
    </section>

    <section class="section" aria-labelledby="cta-heading">
        <div class="container">
            <div class="cta-card bg-dawn reveal">
                <div class="drift" style="top:-100px;right:-100px;width:320px;height:320px;background:color-mix(in srgb, var(--sd-pink) 24%, transparent)"></div>
                <div class="drift" style="bottom:-100px;left:-60px;width:280px;height:280px;background:color-mix(in srgb, var(--sd-blue) 30%, transparent);animation-delay:-9s"></div>
                <div class="inner">
                    <h2 id="cta-heading" class="display h2">Never miss a deadline again.</h2>
                    <p class="lead">SealDocs is nearly ready for iOS and Android. Want to know the day it ships? Send a note and you will be the first to hear.</p>
                    <div class="btn-row center">
                        <a href="mailto:{EMAIL}?subject=SealDocs%20launch" class="btn btn-pink">Tell me when it launches</a>
                    </div>
                    <p class="note">Free to download. Your documents stay on your device.</p>
                </div>
            </div>
        </div>
    </section>
"""

# --------------------------------------------------------------------------
# Support
# --------------------------------------------------------------------------

SUPPORT_TITLE = "Support | vibe&code"
SUPPORT_DESC = "Get help with FeelScape or SealDocs, report a bug, or send an idea. Email vibeandcode@gmail.com; replies usually within a day or two."

SUPPORT = f"""
    <section class="hero bg-sky" aria-label="Support">
        <div class="drift" style="top:-160px;right:-160px;width:480px;height:480px;background:color-mix(in srgb, var(--peach) 60%, transparent)"></div>
        <div class="container" style="position:relative;padding:56px 20px 48px">
            <div class="hero-copy fade-up" style="max-width:720px">
                <p class="eyebrow">Support</p>
                <h1 class="display h1" style="margin-top:8px">How can I help?</h1>
                <p class="lead">Questions, feedback or a bug in FeelScape or SealDocs: email <a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a> or use the form below, which opens a pre-filled message in your email app. Replies usually take a day or two.</p>
            </div>
        </div>
    </section>

    <section class="section" aria-label="Contact">
        <div class="container">
            <div class="grid grid-2" style="gap:36px;align-items:start">
                <div style="display:flex;flex-direction:column;gap:20px">
                    <div class="card card-pad reveal">
                        <div class="contact-line">
                            <span class="icon">{ICONS["mail"]}</span>
                            <div><b>Email</b><a href="mailto:{EMAIL}" class="text-link" style="font-size:14px">{EMAIL}</a></div>
                        </div>
                        <div class="contact-line" style="margin-top:18px">
                            <span class="icon">{ICONS["clock"]}</span>
                            <div><b>Response time</b><span>Usually within 24 to 48 hours</span></div>
                        </div>
                    </div>
                    <div class="card card-pad reveal">
                        <div class="app-head">
                            <img src="/feelscape/images/logo/feelscape-icon.png" alt="" width="48" height="48" class="app-icon" style="width:48px;height:48px;border-radius:14px">
                            <div><h2 class="h3">FeelScape</h2><p class="sub">Subscriptions, restoring purchases, data export</p></div>
                        </div>
                        <p class="muted small" style="margin-top:14px">The FeelScape support page walks through the common ones: cancelling through Apple or Google, restoring on a new phone, and exporting or deleting your data.</p>
                        <a href="/feelscape/support/" class="text-link small" style="display:inline-block;margin-top:12px">FeelScape support →</a>
                    </div>
                    <div class="card card-pad reveal">
                        <div class="app-head">
                            <img src="/assets/sealdocs-icon.png" alt="" width="48" height="48" class="app-icon" style="width:48px;height:48px;border-radius:14px">
                            <div><h2 class="h3">SealDocs</h2><p class="sub">Coming soon</p></div>
                        </div>
                        <p class="muted small" style="margin-top:14px">SealDocs isn't in the stores yet. Questions about how it will handle your documents are answered in the FAQ; anything else, just write.</p>
                        <a href="/sealdocs.html#faq" class="text-link pink small" style="display:inline-block;margin-top:12px">SealDocs FAQ →</a>
                    </div>
                </div>

                <form class="card card-pad form reveal" id="contact-form" data-email="{EMAIL}">
                    <h2 class="display" style="font-size:1.6rem;margin-bottom:18px">Send a message</h2>
                    <div class="row">
                        <label class="field">Name<input type="text" name="name" required autocomplete="name"></label>
                        <label class="field">Email<input type="email" name="email" required autocomplete="email"></label>
                    </div>
                    <label class="field">Topic
                        <select name="subject" required>
                            <option value="">Choose one</option>
                            <option>FeelScape support</option>
                            <option>SealDocs question</option>
                            <option>Bug report</option>
                            <option>Feature idea</option>
                            <option>Something else</option>
                        </select>
                    </label>
                    <label class="field">Message<textarea name="message" rows="6" required></textarea></label>
                    <button type="submit" class="btn btn-primary">Open in my email app</button>
                    <p class="status" role="status" aria-live="polite"></p>
                </form>
            </div>
        </div>
    </section>
"""

SUPPORT_SCRIPT = """    <script>
    (() => {
        const form = document.getElementById('contact-form');
        const status = form.querySelector('.status');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const f = Object.fromEntries(new FormData(form));
            const to = form.dataset.email;
            const subject = `[vibe&code] ${f.subject || 'Support'} \\u2014 ${f.name}`;
            const body = `${f.message}\\n\\n\\u2014\\n${f.name}\\nReply to: ${f.email}`;
            status.textContent = 'Opening your email app\\u2026 if nothing happens, email ' + to + ' directly.';
            window.location.href = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        });
    })();
    </script>
"""
