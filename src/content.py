"""Resources hub content: FAQ pages, guides and video pages.

Text only. Pages are built in build.py. Tokens filled at build time:
  {NAME}            the business name from config
  [[key]]           a price from config.PRICES, e.g. [[support_10h]]
  [[min|max]]       a price range, e.g. [[store_move_min|store_move_max]]

Rules for anything added here (00 project instructions, 13 Skills Map):
- Every answer and guide is written fresh. Don't copy text from another page of the site;
  the build's duplicate check fails if a resource page repeats a long run of words.
- Every vendor price or limit carries the date it was checked, and the source is listed.
- Guides stay "draft" until Vee approves them. Draft guides build on staging only.
"""

CHECKED = "2026-11-11"  # the day the facts below were read on the vendors' own pages

# ---------------------------------------------------------------------------
# FAQ pages. (question, answer, link href, link text). Answers are 40 to 80 words.
# ---------------------------------------------------------------------------

FAQ_SHOPIFY = [
    ("Which Shopify plan do I need if I also sell in person?",
     "Every Shopify plan can take payments in person with a phone or a card reader, so the choice usually comes "
     "down to staff accounts and fees. Basic has no extra staff accounts, Grow has 5 and Advanced has 15. Staff "
     "permissions and in-store stock tools come with POS Pro, at $89 a month per location. Prices checked on "
     "shopify.com on Nov 11, 2026.",
     "/tools/shopify-plan-picker", "Try the plan picker"),
    ("Can I move my WooCommerce store without losing Google traffic?",
     "Usually, yes. Traffic lost after a move mostly comes from old links that now go nowhere. Before launch, every "
     "old product, category and page address gets a 301 redirect to its new Shopify address, and the busiest ones "
     "are checked by hand. Rankings can still move for a few weeks while Google recrawls the site.",
     "/services/store-move", "What a Store Move includes"),
    ("Do my customers keep their accounts when I move to Shopify?",
     "Their names, addresses and past orders can come with them. Passwords can't, because no platform hands over "
     "stored passwords. Shopify's newer customer accounts sign people in with a one-time code sent by email, so "
     "most customers have nothing to reset. On classic accounts, customers set a new password, and we help you "
     "write the email that explains why.",
     "/services/store-move", "How a store move works"),
    ("What does Shopify POS need at the counter?",
     "The Shopify POS app runs on an iPad, iPhone or Android device. For cards, add a Shopify card reader or use Tap "
     "to Pay on a supported phone. A receipt printer, barcode scanner and cash drawer are optional extras. Check "
     "Shopify's list of supported hardware before you buy, because older tablets and other brands of reader may "
     "not work.",
     "/guides/shopify-pos-vs-odoo-pos", "Shopify POS or Odoo POS"),
    ("Can Shopify track stock in more than one location?",
     "Yes. Basic, Grow and Advanced each allow up to 10 inventory locations, and Plus allows up to 200 (checked Nov "
     "11, 2026). Each location keeps its own count, you choose which ones fill online orders, and transfers move "
     "stock between them. For reorder rules based on past sales and vendor price lists, stores usually add a back "
     "office such as Odoo.",
     "/odoo", "What Odoo adds"),
    ("When do I need POS Pro?",
     "When staff at a shop need different permissions, or the shop needs in-store inventory tools, pickup and "
     "flexible delivery. Shopify sells those as POS Pro, $89 a month per location on Basic, Grow and Advanced, and "
     "Plus includes it for 20 locations (checked Nov 11, 2026). A small shop with one or two trusted people at the "
     "register can often skip it.",
     "/tools/shopify-plan-picker", "Check it in the plan picker"),
    ("Can Shopify handle wholesale prices?",
     "Yes, within limits. Shopify's B2B features let you set up company accounts with catalogs that carry their own "
     "prices. Basic, Grow and Advanced allow up to 3 catalogs, and Plus has no cap (checked Nov 11, 2026). Many "
     "price lists, phone orders or credit limits per customer tend to fit better in Odoo, with Shopify kept in "
     "sync.",
     "/services/store-to-back-office-sync", "Connect Shopify and Odoo"),
    ("Is Shopify's own inventory enough, or do I need an app?",
     "For one or two locations and a few vendors, Shopify's counts, transfers and purchase orders usually cover it. "
     "Stores start looking further when they need reorder points from sales history, vendor bills matched to "
     "receipts, landed costs, or a stock value the accountant trusts. Before buying an inventory app, check it "
     "doesn't repeat what your accounting software already does.",
     "/shopify#enough", "When Shopify alone is enough"),
    ("How do Shopify payouts show up in my books?",
     "A payout is one bank deposit that bundles many orders, minus fees and refunds. The bank shows the deposit, but "
     "your books need the sales, fees and refunds behind it. A payout report, or a connector that brings payouts "
     "into your accounting software, makes the two match. Your bookkeeper decides how to record it, and the data "
     "gets set up so they can.",
     "/guides/shopify-connectors-odoo-online", "Connectors and payouts"),
    ("Can I sell on Shopify and keep stock in another system?",
     "Yes, if one system owns the count and the other follows it. A common setup has Odoo owning products and stock "
     "while Shopify shows what's available to sell. When both systems edit the same count, they drift apart within "
     "days. The connector brings orders in and sends stock numbers out on a schedule you can check.",
     "/tools/sync-simulator", "Try the sync model"),
    ("How long does a store move take?",
     "A Store Move runs 3–8 weeks. A small catalog with little order history sits at the short end. Thousands of "
     "products, deep variants, subscriptions or apps that keep their own data push it toward eight. Most of that time "
     "goes to checking imported data and testing orders, because the import itself is quick.",
     "/services/store-move", "Store Move scope and price"),
    ("What happens to my old URLs after the move?",
     "Each one is pointed at the matching Shopify page with a permanent redirect. Shopify's address structure is "
     "fixed, with paths such as /products/ and /collections/, so most addresses change. The redirect map is built "
     "from your old sitemap and analytics, imported into Shopify, and the top pages are tested again after launch.",
     "/guides", "More guides"),
    ("Can you design a custom theme?",
     "No. We set up an existing theme with your logo, colors, fonts and photos, which suits most stores that sell a "
     "catalog. For a design that doesn't exist yet, hire a Shopify theme designer or developer. We can work next to "
     "them, so products, settings and checkout are ready when the design is.",
     "/services/store-move", "What's in a Store Move"),
    ("Does Shopify work out sales tax for me?",
     "Shopify calculates sales tax at checkout on every plan, based on the places you tell it you're registered. It "
     "doesn't decide where you must register, file or pay, which depends on your sales in each state. We enter the "
     "settings, and your accountant confirms the settings.",
     "/shopify", "Shopify setup"),
    ("Who owns the store after you set it up?",
     "You do, from the first day. The store is opened in your name, or handed to you through Shopify's ownership "
     "transfer, and the plan bills your card. We work from a staff account and remove it at handover, confirmed in "
     "writing. Apps you install bill you directly too.",
     "/faq/working-with-us", "How we work with you"),
]

FAQ_ODOO = [
    ("What's the difference between Odoo Community and Odoo Enterprise?",
     "Community is Odoo's free, open-source edition. Enterprise adds what Community lacks, such as full accounting, "
     "Studio and Odoo's own support, and it's the edition behind Odoo's paid plans, including Odoo Online. For a "
     "business with 5 to 15 users, a paid plan is usually the better fit. The screens on this site come from a "
     "Community demo database.",
     "/odoo", "Odoo setup"),
    ("Odoo Online, Odoo.sh or our own server: which one?",
     "Odoo Online is hosted by Odoo and needs the least upkeep, but it can't run modules from outside developers. "
     "Odoo.sh is also run by Odoo, is built for databases with extra modules, and bills hosting on top of your plan. "
     "Your own server gives full control and full responsibility. We work on Odoo Online and Odoo.sh, not on "
     "self-hosted setups.",
     "/guides/odoo-online-vs-odoo-sh", "Odoo Online or Odoo.sh"),
    ("Standard or Custom plan, and why does it matter for a connector?",
     "Standard runs on Odoo Online only and includes every app. Custom adds Studio, more than one company, Odoo.sh or "
     "on-premise hosting, and External API access (Odoo's pricing page, checked Nov 11, 2026). Connectors that run "
     "outside Odoo and call its API need that access, so they need Custom, and the plan applies to every user.",
     "/guides/shopify-connectors-odoo-online", "Which connectors fit your plan"),
    ("How long does an Odoo setup take for 10 users?",
     "A Back Office Launch runs 6–12 weeks for 5 to 15 users. Clean data and a team that tests on time keep it near "
     "six weeks. Messy product lists, a second warehouse, registers or a QuickBooks cleanup push it toward twelve. "
     "The schedule is written into the proposal before work starts, with dates for data, testing and go-live.",
     "/services/back-office-launch", "Back Office Launch scope"),
    ("Can we move from QuickBooks without losing our history?",
     "Your history stays safe in QuickBooks, which you can keep for lookups. What moves to Odoo is what you need to "
     "run from day one: products, customers, vendors, opening stock, open invoices and bills, and opening balances "
     "agreed with your accountant. Bringing years of transactions across is a separate, larger project.",
     "/guides/quickbooks-to-odoo-data", "The data to pull first"),
    ("Can Odoo run our registers?",
     "Yes. Odoo Point of Sale runs in a web browser on a tablet, laptop or touchscreen, and sells from the same "
     "products and stock as the rest of Odoo. Odoo 20 added a lighter mode that tracks quantities without installing "
     "the Inventory app. Cards go through a supported terminal, and for US shops that means providers such as "
     "Stripe or Adyen.",
     "/videos/odoo-register-sale", "Watch a register sale"),
    ("What changed in Odoo 20?",
     "Odoo 20 came out in September 2026. For stores and wholesalers, the useful changes are suggested minimum and "
     "maximum stock on reorder rules, offline mode for staff, a stock aging report, and an Avalara Included option "
     "for US sales tax. Every AI feature now runs on paid credits, and Odoo 20 still ships without a Shopify "
     "connector in its standard apps.",
     "/odoo", "Odoo 20 for store owners"),
    ("Do Odoo's AI features cost extra?",
     "Yes. Odoo's release notes for version 20 say every AI feature needs credits, bought through Odoo's in-app "
     "purchases. That covers the AI agents that create and update records and the finance questions you can ask about "
     "your own accounting. If your team plans to use AI daily, test the credit cost in a trial first.",
     "", ""),
    ("Can we try Odoo before we buy it?",
     "Yes, in three ways. Odoo offers a free trial database, a One App Free plan that runs a single app for unlimited "
     "users, and a public demo with sample data. The trial is the best test, because you can load a slice of your own "
     "products and check a connector on the plan you'd pay for.",
     "/tools/odoo-tours", "Click through Odoo 20 first"),
    ("What does Odoo cost per user?",
     "On Odoo's US pricing page (checked Nov 11, 2026), Standard is $24.90 per user per month, paid yearly, for the "
     "first 12 months, then $31.10. Custom is $49.00, then $61.00. Paying monthly costs more. Odoo Online hosting is "
     "included, Odoo.sh hosting is billed separately, and you pay Odoo directly, never through us.",
     "/guides/odoo-online-vs-odoo-sh", "Costs for 10 users"),
    ("How do we upgrade from Odoo 19 to 20?",
     "Odoo's upgrade service converts the database, but the checking is yours. Upgrade a test copy first, then check "
     "reports, the connector and any extra modules, and show staff what moved. Odoo 20 renames some payment statuses, "
     "for example. Upgrade the live database only after the test copy passes.",
     "", ""),
    ("Can Odoo handle US sales tax?",
     "Yes. Odoo's US setup connects to Avalara's AvaTax for rates by address, and Odoo 20 adds an Avalara Included "
     "option aimed at smaller businesses, plus a redesigned US sales tax report. Which states you collect in, and how "
     "you file, is your accountant's call. We set up what they confirm.",
     "", ""),
    ("What is a staging database, and why do we need one?",
     "It's a copy of your Odoo database used for building and testing. Settings, imports and connector rules go "
     "there first, your team tests against a written checklist, and only then does anything touch the live database. "
     "A mistake in staging costs a reset, not a day of orders.",
     "/how-it-works", "How a project runs"),
    ("Our Odoo project stalled. Can you take it over?",
     "Often, yes. The first step is a written review of what's set up, what's broken, what's missing and what state "
     "the data is in. From that you get a fixed fee to finish, or a plain note that starting over costs less. You "
     "keep the review either way, and it says nothing about who worked on it before.",
     "/services/systems-roadmap", "Start with a Systems Roadmap"),
    ("Can Odoo and Shopify share one product list?",
     "They can work from one list if one system owns it. One setup keeps products, prices and stock in Odoo, sends "
     "stock to Shopify and pulls orders back. Odoo's own connector does the reverse for products, pulling them from "
     "Shopify and matching on SKU. Decide who edits what before go-live, and pick the connector to match.",
     "/guides/shopify-connectors-odoo-online", "How the connectors differ"),
]

FAQ_US = [
    ("Who will I actually work with?",
     "Vee, who runs {NAME}, leads your project from the scoping call to handover and is your contact the whole way "
     "through. Decisions are confirmed in writing, and the plan, the test checklist and the handover notes are "
     "yours to keep.",
     "/about", "About {NAME}"),
    ("Do you work with businesses outside the US?",
     "Not at the moment. We work with businesses based in the US, in US Eastern business hours, with US sales tax, "
     "payments and shipping in mind. If you're outside the US, a Shopify or Odoo specialist in your own country will "
     "know your tax rules and local payment providers better than we would.",
     "", ""),
    ("Is the first call free?",
     "It is. The scoping call takes 30 minutes and costs nothing. We ask how you sell, how stock and purchasing work "
     "and how the books are kept, and you get a plain answer on whether one of our services fits. If it does, a "
     "written proposal follows within 3 business days.",
     "/book", "Book a scoping call"),
    ("Do you earn commission from Shopify, Odoo or app vendors?",
     "We may. Shopify, Odoo and some app vendors pay referral commissions when a client buys a plan or app we "
     "recommend. It doesn't change the price you pay, and any commission tied to your project is listed in your "
     "proposal. The recommendation comes first, including when it pays us nothing.",
     "/pricing", "How our fees work"),
    ("Who owns the accounts and passwords?",
     "You do. Shopify, Odoo, app and domain accounts are opened in your name and billed to your card. We get our own "
     "staff or user login, never yours, and we don't keep your passwords. At handover our access is removed, and we "
     "confirm that in writing.",
     "/privacy", "How we handle data"),
    ("What happens after launch?",
     "Every project includes time after go-live: two weeks of launch support after a Store Move, four weeks of fixes "
     "after a Back Office Launch, and two weeks of monitoring after a Sync. After that, a Support block covers "
     "questions and small changes: 10 hours for [[support_10h]] within 90 days, or 20 hours for [[support_20h]] "
     "within 180 days.",
     "/services/support-block", "Support block terms"),
    ("What hours do you work, and in which time zone?",
     "Monday to Friday, US Eastern time. Messages get a reply by the end of the next business day, and calls are "
     "booked inside those hours. There's no after-hours or emergency line, which is why go-live dates are agreed in "
     "writing well ahead.",
     "/how-it-works", "How a project runs"),
    ("What if we need changes mid-project?",
     "Raise it as soon as it comes up. You get a written change order that says what's added or dropped, what it "
     "costs and how it moves the dates, and nothing new starts until you sign it. Everything you agreed at the start "
     "keeps its fixed fee.",
     "/pricing", "Pricing and payment terms"),
    ("Will you sign our NDA?",
     "Yes. Send it before the first detailed call and we'll review and sign it, or we can send our own mutual NDA. "
     "Either way, client names, data and screenshots aren't shared without written permission.",
     "", ""),
    ("Do you write custom code?",
     "No. Our packages use standard Shopify and Odoo features, plus connectors and apps from their vendors. That keeps "
     "upgrades simpler, since there's no custom code to rewrite at each new Odoo version. If your process truly needs "
     "a custom module, the Systems Roadmap says so, and scopes it so a developer can quote it.",
     "/services/systems-roadmap", "What a Systems Roadmap covers"),
]

FAQ_PAGES = [
    # (slug, label, platform, h1, lead, list)
    ("shopify", "Shopify", "shopify", "Shopify questions",
     "Plans, POS, store moves, wholesale and who owns what. Each answer links to the page that goes further.",
     FAQ_SHOPIFY),
    ("odoo", "Odoo", "odoo", "Odoo questions",
     "Editions, hosting, plans, Odoo 20, QuickBooks and taking over a stalled setup.",
     FAQ_ODOO),
    ("working-with-us", "Working with us", "both", "Questions about working with us",
     "Who does the work, when we reply, what you own and what happens after launch.",
     FAQ_US),
]

# ---------------------------------------------------------------------------
# Guides. Body is light markdown: "## " heading, "- " list, "1. " list, "| " table rows
# (first row is the header), [text](url) links. Blank lines separate blocks.
# ---------------------------------------------------------------------------

GUIDES = [
    {
        "slug": "shopify-connectors-odoo-online",
        "platform": "both",
        "status": "approved",
        "title": "Which Shopify connectors work with Odoo Online",
        "seo_title": "Shopify connectors that work with Odoo Online",
        "desc": ("Odoo-side Shopify connectors need Odoo.sh, Odoo's own included. Apps on the Shopify side can "
                 "work with Odoo Online, but they need the Custom plan."),
        "checked": CHECKED,
        "short": ("Very few. Odoo Online can't run modules from the Apps store, and Odoo's own documentation says its "
                  "Shopify Connector works only on Odoo.sh. What's left are apps installed on the Shopify side that "
                  "reach Odoo through its API. Odoo lists that API access under its Custom plan, so check your plan "
                  "before you buy."),
        "body": """
## Why Apps store connectors need Odoo.sh

Odoo Online is Odoo's own cloud hosting, and Odoo's hosting documentation says it "is not compatible with non-standard apps". A connector bought on the Odoo Apps store is a non-standard app: a module installed into your database next to Odoo's own code. That rules out Apps store connectors on Odoo Online, whoever wrote them.

Odoo's own Shopify Connector sits under the same rule. Its setup page says the integration "only works with Odoo-SH" and needs Odoo 19.0 or 20.0. Two of the larger outside vendors say the same about theirs: VentorTech's listing says Odoo Online is not supported, and TeqStars' says its module is not compatible with it.

Don't trust the Availability box on Apps store listings. When we checked on Nov 11, 2026, it showed Online, Odoo.sh and On Premise on every Shopify connector we opened, including the ones whose own text rules Online out.

## The connectors we checked

| Connector | Runs | Listed price | Odoo Online |
| Odoo's Shopify Connector (ecommerce_shopify) | Inside Odoo | $198.87 | No. Odoo's docs say Odoo.sh only |
| VentorTech (integration_shopify) | Inside Odoo | $557.13 | No, per the listing |
| TeqStars (shopify) | Inside Odoo | $446.59 | No, per the listing |
| Emipro (shopify_ept) | Inside Odoo | $612.96 | The listing doesn't say. As an Apps store module, expect no |
| Techspawn OdooSyncO | On Shopify | $20–35 a month | Yes, per the listing, for Odoo 16 and later |
| Webkul Odoo Connector | On Shopify | $35 a month | Works over Odoo's API, so the plan rule applies |

Apps store prices are what the Odoo 20.0 listings showed on Nov 11, 2026. Shopify App Store prices were checked on Nov 6, 2026. Odoo's own connector also has a Shopify-side app with its own paid plans, offered in the US and Canada.

## Check your Odoo plan first

Apps on the Shopify side don't install anything in Odoo. They log in to your database from outside and read or write records through Odoo's External API, and Odoo's pricing page lists External API under the Custom plan, not Standard.

For a 10-user business paying yearly, that's $249 a month on Standard against $490 a month on Custom in the first year, and $311 against $610 once the first-year discount ends (Odoo's US prices, checked Nov 11, 2026). The higher price applies to every user in the database, so count the whole difference as part of what the connector costs.

## How Odoo's own connector behaves

If you do move to Odoo.sh, Odoo's connector is the cheapest of the Odoo-side options. Its documentation describes how it works:

- It runs on a schedule, not in real time. Orders come in every 10 minutes by default, and stock goes back to Shopify after each order pull.
- Products travel from Shopify to Odoo, matched on SKU. A Shopify product without a SKU won't import.
- Shopify variants arrive in Odoo as separate products, not as variants of one product.
- Orders, customers, returns and refunds come from Shopify into Odoo. Deliveries and stock go both ways.

The third-party modules go further in places, such as products flowing both ways or Shopify payouts imported for bank reconciliation. A store with variants, two warehouses and a bookkeeper reconciling payouts is the kind of business where that extra cost tends to make sense.

## When the other option wins: no connector yet

If you take a handful of orders a day, keep stock in Shopify and use Odoo mainly for invoices and accounting, a connector can wait. Exporting Shopify orders and importing them into Odoo once a week costs nothing and is easy to undo. Add a connector when someone is retyping orders, the two systems disagree about stock, or a second sales channel opens.

## How to test a connector before you pay

1. Start an Odoo trial on the plan you intend to buy, not a bigger one.
2. Connect it to a Shopify development store or a test copy of your catalog, never your live store.
3. Install the connector and confirm it connects. On Standard, this is where an API-based app shows whether it can get in.
4. Place ten test orders, including one with a discount code, one partial fulfillment and one refund.
5. Check where each order, payment and stock change lands in Odoo, and what Shopify shows afterward.
6. Ask the vendor in writing which Odoo versions and hosting types they support, and what happens at the next major Odoo version.
""",
        "faqs": [
            ("Can I install a connector from the Odoo Apps store on Odoo Online?",
             "No. Odoo Online doesn't run non-standard apps, and Apps store modules are non-standard, even when the "
             "listing tags them for Online. You'd need Odoo.sh, which also means the Custom plan."),
            ("Does a connector bring Shopify payouts into Odoo accounting?",
             "Some do. Odoo's own connector creates invoices and payments for each order, and its documentation "
             "doesn't mention payouts. Emipro's listing describes payout import for reconciliation. If your "
             "bookkeeper reconciles payouts, make it a test case before you buy."),
            ("If we start on Odoo Online, do we have to move to Odoo.sh later?",
             "Only if you need a module Odoo doesn't ship as standard. A Shopify-side app on the Custom plan, or no "
             "connector at all, keeps you on Online. If you already know you'll want an Odoo-side connector, starting "
             "on Odoo.sh saves a move later."),
        ],
        "sources": [
            ("Odoo documentation: Shopify Connector configuration",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector/setup.html", CHECKED),
            ("Odoo documentation: Shopify Connector overview",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector.html", CHECKED),
            ("Odoo 20 documentation: Hosting", "https://www.odoo.com/documentation/20.0/administration/hosting.html",
             CHECKED),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
            ("Odoo Apps: ecommerce_shopify, 20.0", "https://apps.odoo.com/apps/modules/20.0/ecommerce_shopify", CHECKED),
            ("Odoo Apps: integration_shopify (VentorTech), 20.0",
             "https://apps.odoo.com/apps/modules/20.0/integration_shopify", CHECKED),
            ("Odoo Apps: shopify (TeqStars), 20.0", "https://apps.odoo.com/apps/modules/20.0/shopify", CHECKED),
            ("Odoo Apps: shopify_ept (Emipro), 20.0", "https://apps.odoo.com/apps/modules/20.0/shopify_ept", CHECKED),
            ("Shopify App Store: OdooSyncO (Techspawn)", "https://apps.shopify.com/synco-odoo-connector", "2026-11-06"),
            ("Shopify App Store: Odoo Connector (Webkul)", "https://apps.shopify.com/shopify-openerp-connector",
             "2026-11-06"),
        ],
        "services": ["connection"],
        "related": ["odoo-online-vs-odoo-sh", "shopify-pos-vs-odoo-pos", "quickbooks-to-odoo-data"],
        "notes": [
            "Names six vendors with prices. R0 asks for a quick legal look before publishing a page that compares "
            "named firms; Vee decides.",
            "Shopify App Store prices are from Nov 6 and could not be re-read (apps.shopify.com blocks page reading).",
        ],
    },
    {
        "slug": "odoo-online-vs-odoo-sh",
        "platform": "odoo",
        "status": "approved",
        "title": "Odoo Online vs Odoo.sh: when a connector or custom module forces the move",
        "seo_title": "Odoo Online vs Odoo.sh: when you have to move",
        "desc": ("Odoo Online includes hosting but runs no third-party modules. What forces a move to Odoo.sh, what "
                 "it costs for 10 users, and when to stay where you are."),
        "checked": CHECKED,
        "short": ("Stay on Odoo Online until you need a module Odoo doesn't ship as standard. Online includes hosting "
                  "and Odoo runs its upgrades, but it can't run third-party or custom modules. Odoo.sh can, needs the "
                  "Custom plan, and bills hosting on top. An Odoo-side Shopify connector is a typical reason to "
                  "move."),
        "body": """
## What each one is

- Odoo Online: Odoo hosts your database on its own servers. Hosting and up to 100 GB of storage are part of the plan price, and it runs Odoo's standard apps on either the Standard or the Custom plan.
- Odoo.sh: also run by Odoo, but built for databases with custom or third-party modules. Your modules live in a GitHub repository, with staging and development branches to test changes before they reach the live database. It needs the Custom plan, and hosting is billed separately.
- Your own server: Odoo on hardware or a cloud account you run yourself. We don't work on self-hosted setups, so this guide leaves it aside.

## What forces the move

- An Odoo-side Shopify connector. That includes Odoo's own, which its documentation says works only on Odoo.sh.
- Any module from the Odoo Apps store. Odoo's hosting page says Online "is not compatible with non-standard apps".
- A custom module written for your business.

Not on the list: Studio, a second company, or External API access for an outside app. Those need the Custom plan, and the Custom plan also runs on Odoo Online.

## What it costs for 10 users

| Setup | Paid yearly, first 12 months | After the first year | Hosting |
| Odoo Online, Standard | $249 a month | $311 a month | Included |
| Odoo Online, Custom | $490 a month | $610 a month | Included |
| Odoo.sh, Custom | $490 a month | $610 a month | Billed separately by Odoo.sh |

Odoo's US prices for 10 users, checked Nov 11, 2026. Odoo.sh bills hosting per worker, storage and staging environment; its pricing page gives the figure for your size.

## What you take on with Odoo.sh

- Every third-party module has to be updated for each new Odoo version before you can upgrade, and the vendor may charge for the new version.
- Upgrades and module updates are tested in a staging branch first, which takes planning.
- Someone has to own the repository and merge changes. That's usually your implementer or a developer, not your staff.

Your staff won't notice much. They use the same Odoo apps in the same browser.

## Moving later

Odoo's hosting page describes how a database moves between hosting types. Odoo Online can run Odoo's in-between versions, such as 16.3, and those can't move to Odoo.sh. The database first has to be upgraded to the next major version, which can mean waiting for that version's release.

## When the other option wins: staying on Odoo Online

For a business with 5 to 15 users on Odoo's standard apps, Online is the lower-effort choice: no hosting bill, no repository, and no module updates to wait for before each upgrade. If the link to Shopify can be an app on the Shopify side, on the Custom plan, or a weekly import, you can stay. Move when a specific module you need won't run on Online, not before.
""",
        "faqs": [
            ("Can Studio run on Odoo Online?",
             "Yes. Studio needs the Custom plan, and the Custom plan runs on Odoo Online. Odoo's pricing FAQ says "
             "installing Studio moves a database to Custom, so check what that does to the price for all your users "
             "first."),
            ("Is Odoo.sh harder to use day to day?",
             "Not for your staff. They use the same Odoo apps in the browser. The difference sits behind the scenes: "
             "a code repository, branches for testing, and module updates that someone has to manage."),
            ("Can we go back from Odoo.sh to Odoo Online?",
             "Only without the modules. Odoo Online can't take a database with non-standard apps, so every "
             "third-party module would be uninstalled first, and whatever it did, such as a Shopify sync, would stop."),
        ],
        "sources": [
            ("Odoo 20 documentation: Hosting", "https://www.odoo.com/documentation/20.0/administration/hosting.html",
             CHECKED),
            ("Odoo pricing (US) and pricing FAQ", "https://www.odoo.com/pricing", CHECKED),
            ("Odoo documentation: Shopify Connector configuration",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector/setup.html", CHECKED),
            ("Odoo.sh pricing", "https://www.odoo.sh/pricing", "2026-11-06"),
        ],
        "services": ["systems-roadmap"],
        "related": ["shopify-connectors-odoo-online", "quickbooks-to-odoo-data", "shopify-pos-vs-odoo-pos"],
        "notes": ["Odoo.sh dollar amounts could not be read on Nov 6; the guide gives none."],
    },
    {
        "slug": "quickbooks-to-odoo-data",
        "platform": "odoo",
        "status": "approved",
        "title": "Moving from QuickBooks to Odoo: the data you need before you start",
        "seo_title": "QuickBooks to Odoo: the data you need first",
        "desc": ("The lists, balances and counts to pull from QuickBooks before an Odoo setup, how to pick a cutover "
                 "date, and why most history can stay behind."),
        "checked": CHECKED,
        "short": ("Before you start, pull your product list with costs, customers, vendors, open invoices and bills, a "
                  "stock count by location, and a trial balance at your cutover date. That's what Odoo needs to run "
                  "from day one. Years of closed transactions can stay in QuickBooks, where your accountant can still "
                  "look them up."),
        "body": """
## The list to pull

| Data | What to check before you export |
| Products and services | One row per item with a unique SKU, a unit of measure, a sales price and a cost. Merge duplicates and drop items you no longer sell. |
| Customers | Billing and shipping addresses, tax-exempt status and payment terms. Merge duplicates, because Odoo imports every row it's given. |
| Vendors | Payment terms and what you buy from each, with vendor prices if you track them. |
| Open invoices | Every unpaid customer invoice at cutover, with its due date and the amount still owed. |
| Open bills | Every unpaid vendor bill at cutover, listed the same way. |
| Stock on hand | A count by location on cutover day, ideally a physical count, with the cost of each item. |
| Trial balance | Account balances at the cutover date, agreed with your accountant. They become Odoo's opening entries. |
| Chart of accounts | Your account list, mapped to Odoo's US chart rather than copied line for line. |

Odoo's own accounting setup list names the same pieces at the time of implementation: opening entries, open invoices and bills, an inventory count and a trial balance.

## Pick the cutover date first

Pick a month end and plan go-live a few days after it. The trial balance, open invoices, open bills and stock count all have to describe the same moment, or the opening numbers won't tie out. Agree the date with your accountant before anything is exported, and keep it away from your busiest weeks.

## Clean up in QuickBooks, not in Odoo

Fix things at the source before you export: merge duplicate customers and items, mark old items inactive, and fill in missing SKUs. Editing a spreadsheet halfway through an import is where errors creep in, and fixing them in Odoo afterward means fixing them twice.

## Load it twice

Load everything into a staging copy of Odoo first and compare totals. Open receivables, open payables, stock value and the trial balance should match QuickBooks to the cent. Then clear the copy, export again at cutover and load the live database. Odoo's import tool copes better with very long files in smaller batches, so split them.

## What stays in QuickBooks

Closed invoices, paid bills, old bank transactions and past years' reports. Keep QuickBooks access for lookups as long as your accountant wants it, or export the reports they ask for before you cancel. Moving full transaction history is possible, but it's a separate project with its own mapping and checks, and you can decide on it later.

## When the other option wins: bringing history over

Some businesses do need their history in Odoo. A lender or auditor may want several years in one system, sales reports by customer may need to reach back years, or QuickBooks access may be ending. Then history is worth moving, scoped on its own with a fixed price. A Back Office Launch covers the opening data above; full history is one of our larger Odoo projects, from [[larger_odoo_from]], quoted after a Systems Roadmap.
""",
        "faqs": [
            ("Can Odoo import QuickBooks files directly?",
             "Not as QuickBooks files. Odoo imports spreadsheets, CSV or Excel, through its import tool, so each list "
             "is exported from QuickBooks, arranged to match Odoo's columns, then imported. Odoo offers import "
             "templates for common records."),
            ("Do we need a physical stock count?",
             "It's the safest choice. Opening stock sets the value your accountant sees on day one, so a count you "
             "trust matters more than a perfect product list. If a full count isn't possible, count your top sellers "
             "and highest-value items."),
            ("Who decides the opening balances?",
             "Your accountant. We load the trial balance they sign off at the cutover date and check that Odoo's "
             "opening numbers match it. We don't make accounting or tax decisions."),
        ],
        "sources": [
            ("Odoo 20 documentation: Accounting, get started",
             "https://www.odoo.com/documentation/20.0/applications/finance/accounting/get_started.html", CHECKED),
            ("Odoo 20 documentation: Export and import data",
             "https://www.odoo.com/documentation/20.0/applications/essentials/export_import_data.html", CHECKED),
        ],
        "services": ["odoo-launch"],
        "related": ["odoo-online-vs-odoo-sh", "shopify-connectors-odoo-online", "shopify-pos-vs-odoo-pos"],
        "notes": ["QuickBooks help pages could not be opened from the build environment; the guide makes no "
                  "QuickBooks-specific claims beyond exporting lists and reports."],
    },
    {
        "slug": "shopify-pos-vs-odoo-pos",
        "platform": "both",
        "status": "approved",
        "title": "Shopify POS vs Odoo POS for a two-location retailer",
        "seo_title": "Shopify POS vs Odoo POS for two locations",
        "desc": ("How Shopify POS and Odoo Point of Sale compare for a two-location retailer: hardware, card "
                 "payments, staff permissions, stock and cost."),
        "checked": CHECKED,
        "short": ("Choose Shopify POS when most sales happen online and Shopify already holds your products and "
                  "stock. Choose Odoo POS when most sales happen at the counter and purchasing, stock and accounting "
                  "live in Odoo. With two shops on Shopify, budget POS Pro at $89 a month per location if you need "
                  "staff roles or in-store inventory tools."),
        "body": """
## Side by side

| | Shopify POS | Odoo Point of Sale |
| Runs on | The Shopify POS app on an iPad, iPhone or Android device | A web browser on a tablet, laptop or touchscreen |
| Cards in the US | Shopify's readers or Tap to Pay, at 2.6% + 10¢ on Basic down to 2.4% + 10¢ on Advanced | A terminal from Odoo's supported list, such as Stripe or Adyen, at that provider's rates |
| Staff roles and permissions | POS Pro, $89 a month per location | Part of Odoo, set per employee |
| Stock across two shops | A count per location, with in-store inventory tools in POS Pro | Warehouse locations, transfers and reorder rules in Odoo Inventory |
| Purchasing and accounting | Purchase orders and transfers in Shopify, accounting in a separate app | Purchase, Inventory and Accounting in the same Odoo database |
| What you pay for the software | Your Shopify plan, plus POS Pro where you need it | Your Odoo plan per user, with Point of Sale included |

Shopify figures from shopify.com/pricing, checked Nov 11, 2026. Odoo's terminal list from the Odoo 20 documentation, checked the same day.

## Choose Shopify POS when

- Most of your revenue comes through the online store, and both shops sell the same catalog.
- Your team already knows Shopify, and you'd rather train them on one system.
- Your stock is simple enough that per-location counts and transfers cover it.

Shopify POS sells from the same products, prices and stock as your online store, so nothing has to sync between the website and the counter.

## Choose Odoo POS when

- Most sales happen at the counter, and purchasing, stock and books already run in Odoo or are about to.
- You reorder from vendors every week and want reorder rules and vendor bills next to the sales behind them.
- You want the register and the warehouse to be one system, with no connector between them.

Odoo 20 added a few register features worth knowing about. Point of Sale can run with simplified inventory, without the Inventory app. It can take more than one currency at checkout. And when a session closes, it posts the whole session as one sale in accounting.

## Running both

Some retailers keep Shopify POS at the counter and Odoo behind it. That works if your connector brings register sales into Odoo as well as online orders. Ask the vendor how POS sales arrive, test a few in a trial, and check that stock at each shop matches afterward.

## When the other option wins

An Odoo business that sells mostly online may still be better off with Shopify POS at the counter, connected to Odoo, so the website and the registers share one checkout and one price list. A Shopify-first store with purchasing trouble rarely needs Odoo POS to fix it. It needs a back office behind Shopify, and the registers can stay as they are.
""",
        "faqs": [
            ("Can Odoo POS use a Shopify card reader?",
             "No. Shopify's readers work with Shopify POS. Odoo Point of Sale takes cards through a terminal from its "
             "own supported list, which for US shops means providers such as Stripe or Adyen."),
            ("Is POS Pro required for two locations?",
             "No. You can sell at two locations without it. Shopify lists POS Pro for staff roles and permissions, "
             "in-store inventory management, and pickup and delivery. Where a shop needs those, it's $89 a month for "
             "that location (checked Nov 11, 2026)."),
            ("Which one costs less?",
             "It depends on your size. Shopify POS costs your Shopify plan plus POS Pro where you need it. Odoo Point "
             "of Sale comes with your Odoo plan, which is priced per user. Add card processing fees to both before "
             "comparing."),
        ],
        "sources": [
            ("Shopify pricing", "https://www.shopify.com/pricing", CHECKED),
            ("Odoo 20 release notes", "https://www.odoo.com/odoo-20-release-notes", CHECKED),
            ("Odoo 20 documentation: Payment terminals",
             "https://www.odoo.com/documentation/20.0/applications/sales/point_of_sale/payment_methods/terminals.html",
             CHECKED),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
        ],
        "services": ["store-move", "odoo-launch"],
        "related": ["shopify-connectors-odoo-online", "odoo-online-vs-odoo-sh", "quickbooks-to-odoo-data"],
        "notes": ["Offline behavior of both registers was not checked, so the guide doesn't compare it."],
    },    {
        "slug": "when-you-dont-need-an-erp",
        "platform": "shopify",
        "status": "approved",
        "title": "When you don't need an ERP yet",
        "seo_title": "When a Shopify store doesn't need an ERP yet",
        "desc": ("The signs a Shopify store can wait on an ERP, the signs it can't, and the cheaper fixes to try "
                 "first. Plan limits checked on Shopify and Odoo's own pages."),
        "checked": "2026-11-12",
        "short": ("If you sell from a few locations, Shopify's stock counts match your shelves, and your bookkeeper "
                  "closes the month without retyping orders, you can wait. Shopify's paid plans already handle stock "
                  "in up to 10 locations, in-person sales and basic wholesale pricing. An ERP starts to pay when "
                  "purchasing, assembly or accounting can't keep pace with sales."),
        "body": """
## What Shopify already handles

A lot of what people buy an ERP for is already in a Shopify plan. From Shopify's pricing page, checked Nov 11, 2026:

- Stock counts in up to 10 locations on Basic, Grow and Advanced.
- Selling in person with the POS app on every plan. POS Pro, at $89 a month per location, adds staff roles and in-store inventory tools.
- Wholesale price lists through Shopify B2B, with up to 3 catalogs below the Plus plan.
- Sales tax calculated on every plan. Your accountant still confirms the settings.

Pair that with an accounting app your bookkeeper already uses, and that covers a lot of stores.

## Signs you can wait

- Your stock counts in Shopify match what's on the shelf when you count.
- One person handles purchasing from a spreadsheet in an hour or two a week.
- You sell finished goods. Nothing gets assembled from parts.
- Your bookkeeper closes each month from the data the accounting app pulls in, with no retyping.
- Your sales come through the online store and the counter, both already in Shopify.

## Signs it's time

- Someone copies orders, invoices or stock numbers from one system to another every week.
- Fast sellers run out while slow ones pile up, because reordering is guesswork.
- You build kits or make products, and need to know what the parts cost and how many are left.
- Wholesale customers want payment terms, credit limits and statements that your setup can't produce.
- Freight and duty never make it into product cost, so margins on paper look better than they are.
- Stock sits in a warehouse, two shops and a third-party warehouse, and nobody trusts one number.

One of these alone can often be fixed with an app. Three or more, and the fixes start costing more than one system would.

To score your own setup, try the [ERP readiness check](/tools/erp-readiness). It asks eight questions like these.

## Cheaper steps to try first

1. Give every product and variant its own SKU. You'll need clean SKUs whatever you choose next.
2. Count your stock once a quarter and correct Shopify on the spot. Find out how far off it drifts.
3. Write down the weekly jobs that eat the most hours. Price an app for the worst one before pricing a whole system.
4. Try an ERP screen with your own products. Odoo's One App Free plan runs one app, plus the apps it depends on, for any number of users at no charge (odoo.com/pricing, checked Nov 11, 2026). It won't connect to Shopify on that plan, but it shows how purchasing or inventory would look.

## When the other option wins: start the ERP now

Some changes are easier to make with the ERP already in place. Opening a warehouse, adding wholesale at volume, starting to make products, or replacing an accounting system that's being retired are all good moments to set it up. Moving in the middle of one of those means doing the big change twice.
""",
        "faqs": [
            ("Is Shopify an ERP?",
             "No. Shopify runs your store, your registers, your stock counts and your orders. An ERP adds purchasing "
             "rules, manufacturing, accounting and the reports that tie them together. Many stores pair Shopify with "
             "an accounting app instead, and that's enough for a long time."),
            ("What does an ERP cost for a small store?",
             "Odoo's Standard plan is $24.90 per user a month paid yearly for the first 12 months, then $31.10 "
             "(odoo.com/pricing, checked Nov 11, 2026). Five users comes to about $125 a month in the first year. "
             "Setup work is extra, and it's usually the bigger number."),
            ("If we add an ERP later, do we have to rebuild the Shopify store?",
             "No. Shopify stays your storefront and checkout. The ERP sits behind it, joined by a connector or a "
             "regular import. Clean SKUs and accurate stock counts now make that step much shorter."),
        ],
        "sources": [
            ("Shopify pricing", "https://www.shopify.com/pricing", CHECKED),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
        ],
        "services": ["systems-roadmap"],
        "related": ["shopify-pos-vs-odoo-pos", "shopify-odoo-inventory-sync", "odoo-online-vs-odoo-sh"],
        "notes": ["The six 'time' signs are judgment, not vendor facts. Vee should check they match what Vee sees "
                  "on calls."],
    },
    {
        "slug": "shopify-odoo-inventory-sync",
        "platform": "both",
        "status": "approved",
        "title": "Shopify to Odoo inventory sync: what moves which way, and how often",
        "seo_title": "Shopify Odoo inventory sync: direction and timing",
        "desc": ("What a Shopify to Odoo connector sends in each direction, how often stock updates, where "
                 "overselling comes from, and how to test it before go-live."),
        "checked": CHECKED,
        "short": ("With Odoo's own Shopify Connector, orders and products flow from Shopify into Odoo, and Odoo "
                  "sends stock levels back after each order pull. Those pulls run every 10 minutes by default, so the "
                  "two counts can disagree for a few minutes. Apps that run on the Shopify side keep their own "
                  "schedules, so ask each vendor how often stock moves."),
        "body": """
## Decide which system owns the count

Stock changes in both places. Online orders and Shopify POS sales happen in Shopify. Vendor receipts, counts and transfers usually happen in Odoo. If both systems are allowed to set the number, they'll overwrite each other.

The rule we use: once a connector is live, Odoo holds the real on-hand count, and Shopify shows what's available to sell. Receive stock and do counts in Odoo only. If staff fix a number in Shopify directly, the next sync can put Odoo's number back.

## What moves which way with Odoo's connector

| What | Direction | When |
| Orders | Shopify to Odoo | Every 10 minutes by default |
| Products | Shopify to Odoo | On import. A product needs a SKU in Shopify to come across |
| Customers | Shopify to Odoo | With their orders |
| Stock levels | Odoo to Shopify | After each order pull |
| Fulfillments and deliveries | Both ways | With the scheduled runs |
| Returns and refunds | Shopify to Odoo | With the scheduled runs |
| Invoices and payments | Created in Odoo | From the imported orders |

From Odoo's Shopify Connector documentation, read Nov 11, 2026. The connector runs only on Odoo.sh, with Odoo 19.0 or 20.0.

## Where overselling comes from

The connector works on scheduled runs, not live updates. Say the last lamp sells online at 2:01. Until the next run brings that order into Odoo, Odoo still counts one lamp, and so does any register selling from Odoo. If someone sells it at the counter at 2:05, you've sold the same lamp twice.

For most stores, a few minutes of gap is fine. It matters when the same item sells online and in person on the same day, or when you run limited stock. Three ways to narrow it:

- Run the order pull more often, if your Odoo setup allows it, and watch the server load.
- Keep the last one or two units of quick sellers off the online count. Ask your connector vendor whether it supports a buffer like this.
- Sell the counter's stock from a separate location, so online orders can't take it.

## Two or more locations

On Basic, Grow and Advanced, Shopify lets you track stock in up to 10 locations (shopify.com/pricing, checked Nov 11, 2026). Each Shopify location has to match a warehouse or location in Odoo, or the stock lands in the wrong place. Before you buy a connector, confirm it sends a separate count per location, not a total. Then test it with a transfer between two shops.

## What changes with an app on the Shopify side

Apps installed in Shopify, rather than in Odoo, reach your database through Odoo's External API. On Odoo Online that needs the Custom plan. They also set their own sync schedules, which can be faster or slower than Odoo's 10 minutes. Ask the vendor three things in writing: how often stock moves, whether it moves per location, and what happens to orders placed while the app is down.

## When the other option wins: no live sync

A store with a few orders a day may not need a sync at all. Keep stock in Shopify, use Odoo for invoices and books, and bring orders across with a weekly export and import. It's slower, but nothing can overwrite anything, and it costs no connector fees. Add a sync when retyping takes hours or the counts start to drift.

## How to test it before go-live

1. Set one test product to 5 units in Odoo and wait for Shopify to show 5.
2. Buy one online with a test payment. Check that Odoo shows 4 after the next run.
3. Receive 10 units in Odoo. Check that Shopify shows 14 after the next run.
4. Refund the online order. Check where the unit ends up in each system.
5. Switch the connector off for an hour and sell the product on both sides. Switch it back on and see how it settles the difference.
""",
        "faqs": [
            ("Does Shopify to Odoo stock sync happen in real time?",
             "Not with Odoo's own connector. It runs on a schedule, every 10 minutes by default, and sends stock to "
             "Shopify after each order pull. Some Shopify-side apps sync more often. Ask for the interval in writing "
             "before you buy."),
            ("What happens to stock when a Shopify order is refunded?",
             "Odoo's connector brings returns and refunds into Odoo. Whether the unit goes back on the shelf depends "
             "on how the return is processed there. Make a refund one of your test cases and check both systems "
             "after the next run."),
            ("What if the connector stops working?",
             "Both systems keep selling, and their counts drift apart. When it's running again, check that it picked "
             "up the orders placed while it was down, then count your quick sellers and correct the numbers in Odoo."),
        ],
        "sources": [
            ("Odoo documentation: Shopify Connector overview",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector.html", CHECKED),
            ("Odoo documentation: Shopify Connector configuration",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector/setup.html", CHECKED),
            ("Shopify pricing", "https://www.shopify.com/pricing", CHECKED),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
        ],
        "services": ["connection"],
        "related": ["shopify-connectors-odoo-online", "shopify-pos-vs-odoo-pos", "odoo-online-vs-odoo-sh"],
        "notes": ["Whether the order-pull interval can be shortened was not checked on a live Odoo.sh database; the "
                  "guide says 'if your Odoo setup allows it'."],
    },
    {
        "slug": "odoo-20-changes",
        "platform": "odoo",
        "status": "approved",
        "title": "Odoo 20 for store owners: what changed, and what the AI features cost",
        "seo_title": "Odoo 20 for store owners: changes and AI costs",
        "desc": ("The Odoo 20 changes that matter to a store, from offline mode to suggested reorder levels, and "
                 "what the AI features cost in credits and plan price."),
        "checked": "2026-11-12",
        "short": ("Odoo 20 came out in September 2026. For a store, the useful changes are offline mode, suggested "
                  "reorder levels, a stock aging report, simpler returns and several register updates. The AI "
                  "features run on prepaid credits, and Odoo's documentation says installing the AI app on "
                  "Standard moves the database to the Custom plan, which roughly doubles the per-user price."),
        "body": """
## What changed that a store will notice

| Area | Change in Odoo 20 | Why it matters |
| Inventory | Suggested minimum and maximum levels for reorder rules, based on demand history, days of coverage and order frequency | A starting point for reorder rules, where most stores guess |
| Inventory | A stock aging report in Moves Analysis | Shows which stock has sat longest |
| Inventory | Stock on hand at a past date, with a precise time | Month-end and year-end counts without a spreadsheet |
| Inventory | Landed costs on specific products in a transfer | Freight and duty land on the items that carried them |
| Inventory | Returns without the old return wizard | Fewer clicks at the returns desk |
| Inventory | A ShipStation connector for rates, labels and tracking | One fewer app for stores already on ShipStation |
| Point of Sale | Runs with simplified inventory, without the Inventory app | One on-hand number per product for a small shop |
| Point of Sale | Snooze products, search orders by receipt number, more than one currency | Day-to-day counter work |
| Sales | Discount codes limited to one use per customer | Welcome codes that can't be reused |
| Accounting | Payment statuses renamed: In Process is now Paid, and Paid is now Reconciled | Bookkeepers need to know before they read reports |
| Accounting | Automatic invoice reminders | Fewer manual follow-ups on unpaid invoices |
| US sales tax | A cheaper Avalara option, Avalara Included, and a redesigned US Sales Tax Report | Your accountant still confirms the settings |
| Everywhere | Offline mode: create, edit and archive records with no connection | Useful in back rooms and warehouses with weak signal |

From Odoo's Odoo 20 release notes, read Nov 12, 2026.

## What the AI features cost

Three facts from Odoo's own pages, read Nov 12, 2026:

- The release notes say all AI features now need credits, bought through in-app purchases.
- In-app purchase credits are prepaid, sold in packs, and priced per service in Odoo's catalog.
- The AI app's documentation warns that installing it on a Standard plan database triggers an upsell to the Custom plan.

The credits are usually the small part. The plan change is the big one, because it applies to every user in the database. Odoo's US prices, paid yearly, checked Nov 11, 2026:

| Users | Standard, first year | Custom, first year | Standard, after year one | Custom, after year one |
| 5 | $124.50 a month | $245 a month | $155.50 a month | $305 a month |
| 10 | $249 a month | $490 a month | $311 a month | $610 a month |
| 15 | $373.50 a month | $735 a month | $466.50 a month | $915 a month |

If you're already on Custom for Studio or a connector, AI adds only the credits. If you're on Standard, decide whether AI is worth the plan change before anyone installs the app.

## Shopify and Odoo 20

The release notes add marketplace links for TikTok and Lazada, and none for Shopify. Odoo's own Shopify Connector supports 19.0 and 20.0, but its documentation says it works only on Odoo.sh. On Odoo Online, Shopify still means an app on the Shopify side, or a regular import.

## Before you upgrade from 19

- Brief your bookkeeper on the renamed payment statuses before the first month-end on 20.
- On Odoo.sh, check that every third-party module has a 20.0 version. Without one, the upgrade stops or the module's features go.
- Run the upgrade on a copy of your database first, and do a few days of normal work in it: sales, receipts, a register session, a bank reconciliation.

## When the other option wins: wait on 19

If a module you rely on has no 20.0 version yet, or you're in the middle of a busy season, waiting is the safer call. Nothing in Odoo 20 forces an urgent move for a small store. Plan the upgrade for a quiet month.
""",
        "faqs": [
            ("Do we have to use Odoo's AI features?",
             "No. Odoo 20 runs without them. They need prepaid credits, and Odoo's documentation says installing the "
             "AI app on Standard moves the database to Custom. If you stay off the AI app, your plan doesn't change."),
            ("Does Odoo 20 have a built-in Shopify connector?",
             "Odoo makes a Shopify Connector that supports 19.0 and 20.0, but its documentation says it runs only on "
             "Odoo.sh. On Odoo Online, the options are an app on the Shopify side, which needs the Custom plan, or a "
             "regular import."),
            ("What's the most useful Odoo 20 change for a retailer?",
             "For most stores, suggested reorder levels and the stock aging report. One tells you when to buy, the "
             "other shows what isn't selling. Offline mode helps too if your stockroom has weak signal."),
        ],
        "sources": [
            ("Odoo 20 release notes", "https://www.odoo.com/odoo-20-release-notes", "2026-11-12"),
            ("Odoo 20 documentation: AI", "https://www.odoo.com/documentation/20.0/applications/productivity/ai.html",
             "2026-11-12"),
            ("Odoo 20 documentation: In-app purchases",
             "https://www.odoo.com/documentation/20.0/applications/essentials/in_app_purchase.html", "2026-11-12"),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
            ("Odoo documentation: Shopify Connector configuration",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector/setup.html", CHECKED),
        ],
        "services": ["odoo-launch"],
        "related": ["odoo-online-vs-odoo-sh", "shopify-connectors-odoo-online", "shopify-odoo-inventory-sync"],
        "notes": ["AI credit pack prices sit on iap.odoo.com, which this workspace can't reach, so the guide gives none.",
                  "Title changed from the plan's 'what AI credits cost' to 'what the AI features cost', since the plan "
                  "change is the cost that matters and credit prices weren't readable."],
    },    {
        "slug": "odoo-standard-vs-custom-plan",
        "platform": "odoo",
        "status": "approved",
        "title": "Odoo Standard vs Custom plan for a 10-user business",
        "seo_title": "Odoo Standard vs Custom plan for 10 users",
        "desc": ("What Odoo's Custom plan adds over Standard, what each costs for 10 users, and the five things "
                 "that move a database onto Custom. US prices checked on odoo.com."),
        "checked": "2026-11-12",
        "short": ("Standard is enough if you run Odoo's own apps on Odoo Online and nothing outside Odoo reads or "
                  "writes your data. You need Custom for Studio, a second company, Odoo.sh or your own server, outside "
                  "apps that use the External API, and the AI app. For 10 users paid yearly, Custom costs $241 more a "
                  "month in the first year."),
        "body": """
## What each plan includes

| | Standard | Custom |
| Per user, paid yearly, first 12 months | $24.90 a month | $49.00 a month |
| Per user, paid yearly, after that | $31.10 a month | $61.00 a month |
| Apps | All of Odoo's apps | All of Odoo's apps |
| Hosting | Odoo Online only | Odoo Online, Odoo.sh or your own server |
| Studio | Not included | Included |
| More than one company | Not included | Included |
| External API for outside apps | Not included | Included |
| AI agents | Not included | Included, with credits bought separately |

Odoo's US prices from odoo.com/pricing, checked Nov 11, 2026. AI details from Odoo's AI documentation, read Nov 12, 2026.

## What 10 users pay

| Billing | Standard | Custom | Difference |
| Paid yearly, first 12 months | $249 a month | $490 a month | $241 a month |
| Paid yearly, after that | $311 a month | $610 a month | $299 a month |
| Paid monthly, first 12 months | $311 a month | $611 a month | $300 a month |
| Paid monthly, after that | $389 a month | $762 a month | $373 a month |

Across the first year, paid yearly, that's $2,988 on Standard and $5,880 on Custom. Odoo's footnote says the lower first-year price is valid for 12 months for the users in the first order, so budget the regular price for year two.

## Five things that move a database to Custom

1. Installing Studio, to add your own fields or screens.
2. Adding a second company.
3. Installing the AI app. Odoo's documentation says this triggers an upsell to Custom on a Standard database.
4. Hosting on Odoo.sh or your own server, usually because you need a module that isn't one of Odoo's standard apps.
5. Connecting an outside app that reads or updates Odoo records through the API. Most Shopify connectors that run on the Shopify side work this way.

The plan applies to the whole database. If one of these happens, every user moves to the Custom price, not only the person who needed it.

## How to decide

Answer these before you sign:

- Will anything outside Odoo send data in or read it out? A Shopify app, a shipping tool, a reporting tool?
- Do you need a field or a screen Odoo doesn't have? That's Studio.
- Do you run, or plan to run, two legal companies?
- Is there a module from the Odoo Apps store you can't do without?
- Do you want the AI agents?

If every answer is no, Standard fits. If any answer is yes, price Custom before you sign.

## When the other option wins: Custom from day one

If you already know you'll connect Shopify through an outside app, or you need an Apps store module, start on Custom. Switching partway through a project changes the budget for every user, and it tends to happen right after go-live, when nobody planned for it.
""",
        "faqs": [
            ("Can we start on Standard and move to Custom later?",
             "Yes. Installing Studio, adding a company or installing the AI app moves the database to Custom, and "
             "the new price applies to every user. Check the price for your whole team before anyone clicks install."),
            ("Does the Custom plan include Odoo.sh hosting?",
             "No. Odoo's pricing page says Odoo.sh hosting is billed on top of the plan. Odoo Online hosting is "
             "included on both plans, with storage up to 100 GB."),
            ("Do outside apps really need Custom?",
             "Apps that call Odoo's API from outside, to read or update records, fall under External API, which "
             "Odoo lists only under Custom. A Shopify-side connector usually works that way. Ask the vendor how it "
             "connects."),
        ],
        "sources": [
            ("Odoo pricing (US) and pricing FAQ", "https://www.odoo.com/pricing", CHECKED),
            ("Odoo 20 documentation: AI", "https://www.odoo.com/documentation/20.0/applications/productivity/ai.html",
             "2026-11-12"),
        ],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["odoo-online-vs-odoo-sh", "shopify-connectors-odoo-online", "odoo-20-changes"],
        "notes": ["Odoo's pricing page also lists a Light User at $8.90. Its terms were not read, so the guide leaves "
                  "it out."],
    },
    {
        "slug": "shopify-plan-for-pos-pro",
        "platform": "shopify",
        "status": "approved",
        "title": "Shopify Basic, Grow or Advanced before adding POS Pro",
        "seo_title": "Shopify Basic, Grow or Advanced with POS Pro",
        "desc": ("How to pick a Shopify plan when you also sell in person: staff accounts, card rates, when the "
                 "lower rates pay for the higher plan, and what POS Pro adds."),
        "checked": CHECKED,
        "short": ("Pick the plan for your staff and online sales first, then add POS Pro only where a shop needs "
                  "staff roles or in-store inventory tools. Basic fits an owner-run shop, Grow adds 5 staff accounts "
                  "and Advanced 15. POS Pro is $89 a month per location on all three. Lower card rates rarely pay "
                  "for a higher plan alone."),
        "body": """
## The three plans side by side

| | Basic | Grow | Advanced |
| Paid yearly | $29 a month | $89 a month | $359 a month |
| Paid monthly | $39 a month | $105 a month | $399 a month |
| Staff accounts | None listed beyond the owner | 5 | 15 |
| Inventory locations | 10 | 10 | 10 |
| In-person card rate | 2.6% + 10¢ | 2.5% + 10¢ | 2.4% + 10¢ |
| Online card rate | 2.9% + 30¢ | 2.7% + 30¢ | 2.5% + 30¢ |
| Extra fee without Shopify Payments | 2% | 1% | 0.6% |
| Custom apps through Shopify's API | Limited data access | Full data access | Full data access |
| POS Pro | $89 a month per location | $89 a month per location | $89 a month per location |

From shopify.com/pricing, US prices, checked Nov 11, 2026.

## What POS Pro adds

Every plan can take payments at a counter with a phone or a card reader, keep simple customer profiles, and handle returns at the shop where the item was bought. Shopify lists four things for POS Pro on top of that:

- Unlimited staff roles and permissions.
- In-store inventory management.
- In-store pickup.
- Flexible delivery options.

If your shop has one or two people who can do everything, you may not need it. If you want each person's role at the register to limit what they can do, that's POS Pro.

## When the lower card rates pay for a higher plan

Each step up lowers the card rate by a little. Here's how much you'd need to sell by card each month before the savings cover the higher plan, paid yearly:

| Move | Extra plan cost | In-person savings | Break-even, in-person only | Online savings | Break-even, online only |
| Basic to Grow | $60 a month | 0.1% | $60,000 a month | 0.2% | $30,000 a month |
| Grow to Advanced | $270 a month | 0.1% | $270,000 a month | 0.2% | $135,000 a month |

Staff accounts are usually the better reason to move up. Treat any rate savings as a bonus.

## Pricing a two-shop setup

Say two shops, six staff who need their own logins, and roles at both counters. That points to Grow, with POS Pro at both locations: $89 plus 2 × $89, or $267 a month paid yearly. The same setup on Advanced comes to $537 a month. The difference only makes sense if you need more than 5 staff accounts or Advanced's other features.

To try your own numbers, use the [Shopify plan picker](/tools/shopify-plan-picker).

## When the other option wins: Shopify Plus

More than 10 selling locations, more than 15 staff accounts, or more than 3 B2B catalogs all point past Advanced. Plus costs $2,300 a month or more, includes POS Pro for 20 locations, and goes up to 200 locations with Shopify Payments. It's a different budget, so price it only when one of those limits is real.
""",
        "faqs": [
            ("Do I need POS Pro to sell in person?",
             "No. Every Shopify plan can sell at a counter with the POS app and a card reader. POS Pro adds staff "
             "roles, in-store inventory tools, pickup and delivery options, at $89 a month per location (checked Nov "
             "11, 2026)."),
            ("Does an Odoo connector work on the Basic plan?",
             "Check before you buy. Shopify's pricing page lists limited data access for custom apps on Basic and "
             "full access from Grow up. Odoo's own connector can link through a custom app, so test it on the plan "
             "you'll actually use."),
            ("Can we change plans later?",
             "Yes. A plan change keeps your products, orders and customers. Price the move against what you need "
             "now, such as staff accounts, rather than buying a bigger plan early."),
        ],
        "sources": [
            ("Shopify pricing", "https://www.shopify.com/pricing", CHECKED),
            ("Odoo documentation: Shopify Connector configuration",
             "https://www.odoo.com/documentation/19.0/applications/sales/sales/shopify_connector/setup.html", CHECKED),
        ],
        "services": ["store-move"],
        "related": ["shopify-pos-vs-odoo-pos", "when-you-dont-need-an-erp", "shopify-odoo-inventory-sync"],
        "notes": ["The 'Can we change plans later' answer says a plan change keeps data. That's Shopify's normal "
                  "behavior but was not read on a Shopify page on Nov 11; re-check on help.shopify.com before "
                  "approving.",
                  "Break-even figures are our own arithmetic from the checked rates."],
    },
    {
        "slug": "odoo-implementation-timeline",
        "platform": "odoo",
        "status": "approved",
        "title": "How long an Odoo implementation takes for 10 users",
        "seo_title": "How long an Odoo implementation takes for 10 users",
        "desc": ("Where the weeks go in a 10-user Odoo setup, what stretches the timeline, what shortens it, and a "
                 "sample eight-week plan for a retailer."),
        "checked": "2026-11-12",
        "short": ("Plan for 6 to 12 weeks from a signed scope to go-live for a 10-user business on Odoo's standard "
                  "apps, then a few weeks of support. Most of that time goes to data and testing, not settings. "
                  "Manufacturing, a second company, years of transaction history or a Shopify connector each add "
                  "time."),
        "body": """
## Where the weeks go

| Stage | Typical length | What happens | What you do |
| Setup in a staging copy | Weeks 1 to 3 | Company, warehouses, products, taxes, users and access | Answer setup questions, confirm tax settings with your accountant |
| First data load | Weeks 2 to 4 | Products, customers, vendors, opening stock and open balances | Check record counts and totals against your old system |
| Testing | Weeks 4 to 8 | Real orders, receipts, invoices, payments and a register session, run against written checks | Run your own daily work in the test copy |
| Training and second load | Weeks 6 to 10 | Short recorded sessions, then a fresh load of current data | Attend, and sign off the counts again |
| Go-live | About one week | Backup, a short freeze on changes, the final load, checks on live orders | Stop entering data in the old system on the agreed day |
| Support | Four weeks after | Fixes and questions as real work starts | Report anything that looks wrong early |

The stages overlap. Run one after another, they'd take far longer.

## Why data takes the longest

Odoo's documentation warns that imports are permanent and can't be undone. That's why data goes into a staging copy first, gets checked, and gets loaded a second time just before go-live. Each load needs someone on your side to compare counts and totals: number of products, stock value, open invoices, money owed to vendors.

## What makes it longer

- Products without SKUs, duplicate customers or vendors spelled three ways. Cleaning comes before loading.
- Bringing years of transaction history instead of opening balances.
- Manufacturing, with bills of materials and work orders.
- A second company, with transactions between the two.
- A Shopify connector, which has its own setup and testing.
- Decisions that wait a week for the one person who can make them.
- Going live in your busy season or at year-end.

## What makes it shorter

- One person on your side who can decide, with a few hours a week set aside.
- A clean product list with a SKU on every item.
- Starting on opening balances at the start of a month or quarter.
- Using Odoo's standard features as they are, and keeping a list of nice-to-haves for after go-live.

## A sample eight-week plan for a 10-user retailer

1. Week 1: kickoff, access, staging copy, warehouse and product structure agreed.
2. Week 2: products and customers loaded into staging, sales and inventory settings.
3. Week 3: vendors, purchasing and reorder rules, opening stock loaded.
4. Week 4: accounting setup, open balances, taxes confirmed by your accountant.
5. Week 5: testing with your team, problems logged and fixed.
6. Week 6: training sessions, second round of testing, sign-off on the written checks.
7. Week 7: second data load, counts signed off, go-live date confirmed.
8. Week 8: backup, freeze, final load, go-live, daily check-ins.

Treat it as a sample. Your own plan depends on your data and how quickly decisions get made.

## When the other option wins: a smaller first phase

If 6 weeks is more than you can spare, start smaller. Sales, inventory and purchasing can go live first, with accounting moving over at the start of the next quarter. You get the stock benefits sooner, and the books move at a clean cut-off date. The trade-off is a few weeks of running accounting in your old system alongside.
""",
        "faqs": [
            ("Can Odoo be set up for 10 users in two weeks?",
             "Not with data loaded twice and tested. A two-week setup usually skips the test load, the training or "
             "both, and that's where go-live problems come from. Settings are quick. Checking your data takes the "
             "time."),
            ("When is the best time to go live?",
             "At the start of a month or quarter, right after a stock count, and outside your busy season. Opening "
             "balances are easier to agree at a clean cut-off date, and staff learn faster when they're not rushed."),
            ("How much of our time does it take?",
             "Plan for one lead person at a few hours a week, more during testing. Each user needs time for training "
             "and for running their own work in the test copy before go-live."),
        ],
        "sources": [
            ("Odoo 20 documentation: Export and import data",
             "https://www.odoo.com/documentation/20.0/applications/essentials/export_import_data.html", "2026-11-12"),
        ],
        "services": ["odoo-launch"],
        "related": ["quickbooks-to-odoo-data", "odoo-standard-vs-custom-plan", "odoo-online-vs-odoo-sh"],
        "notes": ["The 6 to 12 weeks matches the Back Office Launch timeline in config.py. The stage lengths and the "
                  "sample plan are our own planning, not a track record."],
    },
]

# ---------------------------------------------------------------------------
# Glossary: (term, plain definition, page that uses it, link text). Definitions are one or two sentences,
# written for this page. Vendor facts carry the same checks as the guides (Nov 11 and 12, 2026).
# ---------------------------------------------------------------------------

GLOSSARY = [
    ("API", "The door one program uses to read or change data in another. Connectors use APIs to move orders "
     "and stock between Shopify and Odoo.", "/guides/shopify-connectors-odoo-online", "Which connectors work with Odoo Online"),
    ("Available quantity", "The units you can still sell: what's on hand, minus units already promised to open "
     "orders.", "/guides/shopify-odoo-inventory-sync", "How stock moves between Shopify and Odoo"),
    ("B2B catalog", "A wholesale price list in Shopify, assigned to business customers. Plans below Plus allow up "
     "to 3.", "/guides/shopify-plan-for-pos-pro", "Shopify plans compared"),
    ("Community and Enterprise", "Odoo's two editions. Community is free and open source; Enterprise is the paid "
     "edition with more apps, sold through Odoo's Standard and Custom plans.", "/faq/odoo", "Odoo questions"),
    ("Connector", "Software that copies orders, products and stock levels between two systems, either on a "
     "schedule or as changes happen.", "/guides/shopify-connectors-odoo-online", "Which connectors work with Odoo Online"),
    ("Custom plan", "Odoo's higher-priced plan. It adds Studio, more than one company, outside apps through the "
     "External API, and hosting on Odoo.sh or your own server.", "/guides/odoo-standard-vs-custom-plan",
     "Standard or Custom for 10 users"),
    ("Cutover", "The point where you stop entering work in the old system and start in the new one, with a final "
     "data load in between.", "/guides/odoo-implementation-timeline", "How long an Odoo setup takes"),
    ("ERP", "Enterprise resource planning: one system for sales, stock, purchasing and accounting, so every "
     "department works from the same records.", "/guides/when-you-dont-need-an-erp", "When you don't need one yet"),
    ("External API", "Odoo's name for outside software reading or updating your Odoo records. Odoo lists it only "
     "under the Custom plan.", "/guides/odoo-standard-vs-custom-plan", "Standard or Custom for 10 users"),
    ("Forecasted quantity", "Odoo's count of what you'll have once planned receipts arrive and planned deliveries "
     "leave.", "/tools/odoo-tours", "See it in the Odoo 20 tours"),
    ("In-app purchase credits", "Prepaid credits for Odoo's paid services, such as text messages and the AI "
     "features. They're bought in packs, priced per service.", "/guides/odoo-20-changes", "What changed in Odoo 20"),
    ("Landed cost", "Freight, duty and other charges added to the vendor's price, so a product's cost shows what it "
     "took to get it onto your shelf.", "/guides/odoo-20-changes", "What changed in Odoo 20"),
    ("Location", "In Shopify, a shop, warehouse or app that holds stock or fills orders. In Odoo, a place inside a "
     "warehouse, such as a shelf or a returns area.", "/guides/shopify-odoo-inventory-sync",
     "How stock moves between Shopify and Odoo"),
    ("Module", "An add-on that extends Odoo. Odoo's own apps are modules, and so is anything bought on the Odoo Apps "
     "store, which Odoo Online can't run.", "/guides/odoo-online-vs-odoo-sh", "Odoo Online or Odoo.sh"),
    ("Odoo Online", "Odoo's own cloud hosting, included in the plan price. It runs Odoo's standard apps only.",
     "/guides/odoo-online-vs-odoo-sh", "Odoo Online or Odoo.sh"),
    ("Odoo.sh", "Odoo's hosting for databases that need custom or third-party modules, with branches for testing "
     "changes. It needs the Custom plan, and hosting is billed on top.", "/guides/odoo-online-vs-odoo-sh",
     "Odoo Online or Odoo.sh"),
    ("On hand", "The units the system says are physically in a location right now.",
     "/guides/shopify-odoo-inventory-sync", "How stock moves between Shopify and Odoo"),
    ("Opening balance", "What each account holds on the day you start in a new accounting system: cash, money "
     "customers owe you, money you owe vendors.", "/guides/quickbooks-to-odoo-data", "Moving from QuickBooks to Odoo"),
    ("Payout", "Shopify's transfer of your sales money to your bank, after fees and refunds. Your bookkeeper matches "
     "each payout to the orders inside it.", "/faq/shopify", "Shopify questions"),
    ("POS", "Point of sale: the register app and card reader you sell with at a counter.",
     "/guides/shopify-pos-vs-odoo-pos", "Shopify POS or Odoo POS"),
    ("POS Pro", "A Shopify add-on for staff roles, in-store inventory tools, pickup and delivery, priced per "
     "location.", "/guides/shopify-plan-for-pos-pro", "Shopify plans compared"),
    ("Purchase order", "A written order to a vendor for goods at agreed prices. In Odoo, receiving it adds the "
     "stock.", "/videos/odoo-purchase-to-stock", "Watch a purchase order received"),
    ("Reconciliation", "Matching the payments in your books to the lines on your bank statement until the two "
     "agree.", "/guides/quickbooks-to-odoo-data", "Moving from QuickBooks to Odoo"),
    ("Redirect", "A rule that sends people and search engines from an old page address to its new one, so links "
     "and rankings carry over after a store move.", "/services/store-move", "Store Move"),
    ("Reordering rule", "An Odoo setting with a minimum and maximum for a product. When the forecast falls below "
     "the minimum, Odoo proposes a purchase back up to the maximum.", "/guides/odoo-20-changes",
     "What changed in Odoo 20"),
    ("Shopify Payments", "Shopify's own card processing. Using a different provider adds a fee on each sale, from 2% "
     "on Basic to 0.6% on Advanced.", "/guides/shopify-plan-for-pos-pro", "Shopify plans compared"),
    ("SKU", "Stock keeping unit: the code that tells one product or variant from another. Connectors use it to "
     "match products between systems.", "/guides/shopify-odoo-inventory-sync", "How stock moves between Shopify and Odoo"),
    ("Staging database", "A copy of your database for trying changes and data loads before they touch the live "
     "one.", "/faq/odoo", "Odoo questions"),
    ("Standard plan", "Odoo's lower-priced plan with all apps, on Odoo Online only.",
     "/guides/odoo-standard-vs-custom-plan", "Standard or Custom for 10 users"),
    ("Statement of work", "The written scope, price, deliverables and payment terms for a project, signed before "
     "work starts.", "/how-it-works", "How a project runs"),
    ("Studio", "Odoo's tool for adding fields, screens and automations without code. Installing it moves a "
     "database to the Custom plan.", "/guides/odoo-standard-vs-custom-plan", "Standard or Custom for 10 users"),
    ("Transfer", "A stock move from one place to another, like warehouse to shop. Odoo also files receipts and "
     "deliveries as transfers.", "/guides/shopify-odoo-inventory-sync", "How stock moves between Shopify and Odoo"),
    ("Variant", "One version of a product, such as a size or a color. Odoo's own Shopify connector brings each "
     "Shopify variant in as a separate product.", "/guides/shopify-connectors-odoo-online",
     "Which connectors work with Odoo Online"),
    ("Webhook", "A message one system sends another the moment something happens, such as a new order. Odoo's own "
     "Shopify connector uses scheduled runs instead.", "/guides/shopify-odoo-inventory-sync",
     "How stock moves between Shopify and Odoo"),
]

# ERP readiness check: eight yes or no questions. A yes is a sign the current setup is straining.
ERP_CHECK = [
    ("copy", "Does someone copy orders, invoices or stock numbers from one system to another every week?"),
    ("reorder", "Do quick sellers run out, or slow ones pile up, because reordering is guesswork?"),
    ("make", "Do you build kits or make products from parts?"),
    ("terms", "Do wholesale customers need payment terms, credit limits or statements?"),
    ("landed", "Do freight and duty costs stay out of your product costs?"),
    ("places", "Is stock kept in three or more places, such as a warehouse, shops and an outside warehouse?"),
    ("close", "Does month-end take days because sales, stock and bank figures don't match?"),
    ("change", "Are you opening a warehouse, adding wholesale or starting to make products in the next 12 months?"),
]
