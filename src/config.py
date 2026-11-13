"""Business facts for the [DBA name] website.

Every fact the site shows lives here once. Pages read from this file, so a
price, promise or contact detail is changed in one place and every page agrees.

Rules (from the project instructions and R0 section 7):
- Fields marked "# CONFIRM" need Vee's real value. Leave them blank ("" or None)
  until they are real and tested. Blank fields hide the sections that use them.
- Never invent contact details, prices, client counts, capacity or history.
- `python3 src/build.py --release` refuses to build while any launch-critical
  field is blank, so an unfinished site cannot be deployed by accident.
"""

# ---------------------------------------------------------------------------
# Business identity
# ---------------------------------------------------------------------------

BUSINESS_NAME = "[DBA name]"  # CONFIRM: set by thread 03 once the DBA is chosen and filed
LEGAL_NAME = "IVYY LLC"
LEGAL_LINE = "IVYY LLC, doing business as [DBA name]"  # CONFIRM: update with the filed DBA
DOMAIN = ""  # CONFIRM: bare domain, e.g. "example.com" (thread 03). No "Shopify" or "Odoo" in it.
STATE = "New York"  # where the business is run from; no street address anywhere on the site
TIMEZONE_LABEL = "US Eastern"
FOUNDER = "Vee"
TAGLINE = "Shopify and Odoo set up as one system, in US business hours."  # 03 section 12, tagline 1 (Recommended). Never a heading.

# ---------------------------------------------------------------------------
# Contact. Each one must be real and tested before launch (R0 section 7).
# ---------------------------------------------------------------------------

EMAIL = ""  # CONFIRM: domain inbox with MX, SPF, DKIM and DMARC set and tested (thread 10)
BOOKING_URL = ""  # CONFIRM: the one scheduler that books into the CRM (thread 10/14). No stopgap form services.
PHONE = ""  # CONFIRM: leave blank unless it rings Vee. A placeholder number must never ship.
PHONE_DISPLAY = ""  # CONFIRM: how the number is written on the page, if PHONE is set

# Live public profiles used in schema sameAs and the footer. Only real, live URLs.
PROFILES = [
    # ("LinkedIn", "https://www.linkedin.com/in/..."),  # CONFIRM: add once live (thread 17)
]

# ---------------------------------------------------------------------------
# About page. Vee writes or approves every line. Blank hides the section.
# ---------------------------------------------------------------------------

ABOUT_BIO = []  # CONFIRM: 2 to 4 paragraphs in Vee's words: real roles, real platform versions, real years. No part-time or "new business" framing.
ABOUT_CREDENTIALS = []  # CONFIRM: only certifications currently held, e.g. ("Odoo 20 Functional Certification", "2026")
PHOTO = ""  # CONFIRM: path under src/ to a real photo of Vee, or blank. No AI people.

# ---------------------------------------------------------------------------
# Promises. Each is defined once and reused on every page.
# Sources: 08 Support block, 08 package timelines, 08 section 14 rule R4.
# ---------------------------------------------------------------------------

PROMISES = {
    "first_reply": "by the end of the next business day",  # 08 support block, 14 R1
    "business_days": "Monday to Friday",
    "call_length": "30-minute",  # 14 pipeline, "Discovery booked"; used as "a 30-minute call"
    "proposal_after_call": "within 3 business days of our call",  # 14 R4
    "support_reply": "by the end of the next business day",  # 08 package 5
    "reply_short": "Next business day",  # hero fact; must match first_reply
}

# ---------------------------------------------------------------------------
# Packages and prices. Source: 08-Service-Catalog-and-Delivery-Playbook,
# "Price config for the website" and package names settled Nov 7, 2026 (threads 11, 12). Change 08 first,
# then 05's math, then this file, in one PR.
# ---------------------------------------------------------------------------

PRICES = {
    "roadmap_min": 1500, "roadmap_max": 3500,
    "store_move_min": 2500, "store_move_max": 10000,
    "odoo_launch_min": 8000, "odoo_launch_max": 20000,
    "connection_min": 2500, "connection_max": 7000,
    "support_10h": 1600, "support_20h": 3000,
    "larger_odoo_from": 15000,
}

PACKAGES = [
    {
        "slug": "systems-roadmap",
        "name": "Systems Roadmap",
        "kind": "Paid discovery",
        "price": ("roadmap_min", "roadmap_max"),
        "timeline": "2–3 weeks",
        "summary": (
            "A review of how orders, stock, purchasing and accounting move through "
            "your business today, ending in a written plan and a fixed quote for the next step. "
            "You keep the plan whether or not you hire us for the work."
        ),
        "includes": [
            "Up to three working sessions of 60 to 90 minutes",
            "An inventory of your current systems and the data you would bring over",
            "Where standard Shopify and Odoo features fit your process, and where they don't",
            "Which connector to use, which records sync and in which direction",
            "Plan and hosting advice: Shopify plan, Odoo Standard or Custom, Odoo Online or Odoo.sh",
            "A written roadmap of 8 to 15 pages and a draft SOW with a fixed fee for the next phase",
        ],
        "excludes": "Configuration, data migration and custom code. Those come in the next phase.",
        "payment": "Paid in full at signing.",
    },
    {
        "slug": "store-move",
        "name": "Store Move",
        "kind": "Move your store to Shopify",
        "price": ("store_move_min", "store_move_max"),
        "timeline": "3–8 weeks",
        "summary": (
            "Moving your store to Shopify from WooCommerce, Wix, Square Online or BigCommerce, "
            "with products, customers, order history, redirects and test orders done before launch. "
            "The fee depends mostly on how many products and how much history you bring over."
        ),
        "includes": [
            "Product, customer and order import, in that order, with notifications off",
            "Collections, navigation and one theme set up with your brand assets",
            "Shipping, taxes as your accountant confirms them, payments, checkout and policy pages",
            "Test orders for payment failure, refund, cancellation and fulfillment emails",
            "A redirect map from every old URL, then domain connection and launch",
            "Shopify POS for up to 2 locations, if it is in your scope",
            "A recorded 90-minute training session and a short admin guide",
        ],
        "excludes": (
            "Custom theme design, copywriting, product photography, Shopify Plus features "
            "and ongoing work after the two-week launch support period."
        ),
        "payment": "40% at signing, 40% when the store is ready for your review, 20% at launch.",
    },
    {
        "slug": "odoo-launch",
        "name": "Back Office Launch",
        "kind": "Odoo for 5 to 15 users",
        "price": ("odoo_launch_min", "odoo_launch_max"),
        "timeline": "6–12 weeks",
        "summary": (
            "Odoo set up for a business with 5 to 15 users: sales, inventory, purchasing, invoicing "
            "and accounting, with your data loaded and checked twice before go-live and four weeks "
            "of support after it."
        ),
        "includes": [
            "Configuration in a staging copy first, never straight in your live database",
            "Products, customers, vendors, opening stock and open balances, loaded twice and reconciled",
            "User roles and access, and up to 5 standard reports or dashboards",
            "Odoo POS for up to 2 locations, if it is in your scope",
            "Testing against written acceptance criteria that you sign off",
            "Up to three recorded training sessions and short user guides",
            "A backup before cutover, go-live, then four weeks of fixes with daily check-ins in week one",
        ],
        "excludes": (
            "Custom modules, manufacturing (MRP), multi-company setups, payroll, "
            "full transaction history, and accounting or tax advice."
        ),
        "payment": "40% at signing, 40% at the start of testing, 20% at go-live. The four weeks of support after go-live are included.",
    },
    {
        "slug": "connection",
        "name": "Store to Back Office Sync",
        "kind": "Connect Shopify and Odoo",
        "price": ("connection_min", "connection_max"),
        "timeline": "3–6 weeks",
        "summary": (
            "Orders, stock, products and fulfillments kept in sync between Shopify and Odoo, using a "
            "connector chosen for your plan and hosting. The connector license is extra and you buy it "
            "from the vendor."
        ),
        "includes": [
            "A short memo comparing connectors, with license cost, hosting needs and limits",
            "A check in a trial database that your Odoo plan allows the API access the connector needs",
            "Setup in staging, then product and customer matching",
            "Sync rules for orders, stock, fulfillments, refunds and taxes",
            "Tests for a new order, partial fulfillment, refund, out-of-stock item and POS sale",
            "Go-live, two weeks of monitoring, and a one-page guide for your staff",
        ],
        "excludes": (
            "Writing a custom connector, fixing bugs inside a vendor's connector (we report them to the "
            "vendor), and Odoo plan upgrades."
        ),
        "payment": "50% at signing, 50% when you accept the go-live.",
    },
]

SUPPORT = {
    "name": "Support block",
    "options": [
        ("10 hours", "support_10h", "use within 90 days"),
        ("20 hours", "support_20h", "use within 180 days"),
    ],
    "summary": (
        "Prepaid hours for questions, small changes, report tweaks, user setup, connector "
        "troubleshooting and short training after a project."
    ),
    "terms": (
        "Paid up front. Time is recorded in 15-minute steps with a 30-minute minimum per request, "
        "and you get a monthly statement of hours used and left. Unused hours expire at the end of "
        "the period. Requests over 4 hours are quoted separately. There is no after-hours or "
        "emergency response."
    ),
}

LARGER_PROJECTS = (
    "Manufacturing, several companies, QuickBooks history, or more than 15 users: "
    "from {larger_odoo_from}, quoted after a Systems Roadmap."
)

# ---------------------------------------------------------------------------
# Disclosures. Final wording lives in 07 (referral) and 06 (tax).
# ---------------------------------------------------------------------------

REFERRAL_DISCLOSURE = (
    "{name} may earn a referral commission from Shopify, Odoo or an app vendor when you buy a plan "
    "or app we recommend. It does not change the price you pay. Every proposal lists any commission "
    "that applies to it."
)  # 07 Referral disclosure. CONFIRM per vendor that the price really does not change.

SALES_TAX_LINE = (
    "Our fees are for services only, and each service is listed on its own invoice line. We do not "
    "resell software. If your state taxes a service on your invoice, the tax is added at your "
    "location's rate."
)  # 08, draft until thread 05 and the CPA confirm

# ---------------------------------------------------------------------------
# Offer. None means no offer bar. An offer needs a real end date, a real regular
# price, real capacity and written terms (00, Stay legal and honest). It hides
# itself the day after END.
# ---------------------------------------------------------------------------

OFFER = None
# OFFER = {
#     "text": "...",
#     "terms": "...",          # printed beside the offer
#     "regular_price": "...",
#     "capacity": "...",
#     "end": "2027-01-31",     # ISO date; shown while today <= end
# }

# ---------------------------------------------------------------------------
# Analytics and search
# ---------------------------------------------------------------------------

CF_WEB_ANALYTICS_TOKEN = ""  # CONFIRM: Cloudflare Web Analytics site token (cookieless). Blank = no beacon.
FIRST_PARTY_COUNTER = True  # the /api/e Worker (worker/index.js); needs the Analytics Engine binding in wrangler.jsonc
INDEXNOW_KEY = "fb31ef10d63c118be35bdd53e0d6fb4b"  # public by design; served at /<key>.txt

# Pages last changed on (ISO date). Shown as "Updated" only on guides; the sitemap
# omits lastmod unless a real date is set here.
LAST_CHANGED = {}

# Real product screenshots, key -> (file under src/, alt text). Filled only with genuine
# captures of sample data; empty keys fall back to the drawn screens.
SCREENS = {
    "hero": ("media/odoo/hero-products.webp", "Odoo 20 Inventory products with price and stock on hand, such as Cabinet with Doors with 33 on hand. Sample data."),
    "hero-m": ("media/odoo/hero-products-m.webp", ""),
    "inventory": ("media/odoo/stock-list.webp", "Odoo 20 product list with sales price, on hand and forecasted quantities. Sample data."),
    "sales": ("media/odoo/invoice.webp", "Odoo 20 customer invoice INV/2026/00011 for sales order S00027, posted and marked paid. Sample data."),
    "delivery": ("media/odoo/delivery.webp", "Odoo 20 delivery order WH/OUT/00074 for sales order S00027, done, with 3 Large Cabinets shipped. Sample data."),
}

# Silent screen recordings, made in our own demo systems with sample data, never in a client's.
# Each one starts on the task it names and ends when the task is done (Vee, Nov 12, 2026: short, no app opening).
# key: (platform "shopify" or "odoo", app shown in the window bar, title, what happens, file stem under src/
# (stem.mp4, stem.webm and stem-poster.jpg), date recorded). A key used on a page but missing here is left out.
CLIPS = {
    "sale": ("odoo", "Sales", "Quote to delivery",
             "A quotation for 3 Large Cabinets is confirmed, and the warehouse validates the delivery.",
             "media/odoo/sale", "2026-11-13"),
    "purchase": ("odoo", "Purchase", "Purchase order to stock",
                 "A purchase order for 20 office chairs is confirmed, then received into stock.",
                 "media/odoo/purchase", "2026-11-13"),
    "pos": ("odoo", "Point of Sale", "A sale at the register",
            "Three items are rung up and paid in cash at the register.",
            "media/odoo/pos", "2026-11-13"),
    "invoice": ("odoo", "Invoicing", "Invoice to paid",
                "A posted invoice for two desks is paid, and Odoo marks it paid.",
                "media/odoo/invoice", "2026-11-13"),
    "locations": ("odoo", "Inventory", "Stock moved between two locations",
                  "One product is stocked in the warehouse and the shop. Five units move across, and both counts change.",
                  "media/odoo/locations", "2026-11-13"),
    "count": ("odoo", "Inventory", "A stock count corrected",
              "A recount finds one fewer desk organizer than Odoo expected, and the count is applied.",
              "media/odoo/count", "2026-11-13"),
    "return": ("odoo", "Inventory and Invoicing", "A return and its refund",
               "A delivered lamp comes back into stock, then the credit note is posted and refunded.",
               "media/odoo/return", "2026-11-13"),
    "reports": ("odoo", "Sales and Inventory", "What sold, and what will run short",
                "Sales by product, sorted by revenue, then the products whose forecast goes below zero.",
                "media/odoo/reports", "2026-11-13"),
}
