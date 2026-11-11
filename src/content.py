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
        "status": "draft",
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
        "status": "draft",
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
        "status": "draft",
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
        "status": "draft",
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
    },
]

# ---------------------------------------------------------------------------
# Video pages: one per recording in config.ODOO_REEL (matched by key).
# Chapters are (seconds, label). Transcript lines describe what is on screen; the recordings are silent.
# ---------------------------------------------------------------------------

VIDEOS = [
    {
        "key": "sale", "slug": "odoo-quote-to-delivery", "platform": "odoo",
        "title": "Odoo 20: a quotation becomes a delivered order",
        "seconds": 26.3, "recorded": "2026-11-11",
        "guide": "shopify-connectors-odoo-online", "tour": "sale",
        "chapters": [
            (0, "Start a quotation for Azure Interior",
             "A new quotation opens in Odoo Sales, and the customer Azure Interior is picked from the contact list. "
             "Odoo fills in the address and payment terms."),
            (8, "Add 3 Large Cabinets",
             "Large Cabinet is added as an order line and the quantity goes to 3. At $320 each, the line comes to "
             "$960 before tax."),
            (14, "Confirm the sales order",
             "Confirm turns the quotation into sales order S00026."),
            (16, "Open the delivery",
             "The Delivery button opens WH/OUT/00073, the warehouse's delivery for this order, with all 3 cabinets "
             "available."),
            (20, "Validate the delivery",
             "Validate marks the delivery done, and the 3 cabinets come off the stock count."),
        ],
    },
    {
        "key": "purchase", "slug": "odoo-purchase-to-stock", "platform": "odoo",
        "title": "Odoo 20: a purchase order received into stock",
        "seconds": 27.4, "recorded": "2026-11-11",
        "guide": "quickbooks-to-odoo-data", "tour": "buy",
        "chapters": [
            (0, "Start a request for quotation",
             "A new request for quotation opens in Odoo Purchase, and the vendor Wood Corner is picked."),
            (8, "Order 20 Office Chairs",
             "Office Chair Black is added and the quantity goes to 20. At $120.50 each, the line comes to $2,410."),
            (15, "Confirm the purchase order",
             "Confirm Order turns the request into purchase order P00017."),
            (18, "Open the receipt",
             "The Receipt button opens WH/IN/00013, which lists the 20 chairs Odoo expects to arrive."),
            (20, "Validate the receipt",
             "Validate records the chairs as received, and on hand for Office Chair Black goes up by 20."),
        ],
    },
    {
        "key": "pos", "slug": "odoo-register-sale", "platform": "odoo",
        "title": "Odoo 20: a sale at the register, paid in cash",
        "seconds": 30.0, "recorded": "2026-11-11",
        "guide": "shopify-pos-vs-odoo-pos", "tour": "",
        "chapters": [
            (0, "Open the Furniture Shop register",
             "From the Point of Sale dashboard, the Furniture Shop register is opened."),
            (6, "Count the opening cash",
             "Odoo asks for the opening cash count. The amount is confirmed and the register opens."),
            (10, "Ring up three items",
             "Desk Organizer, Office Lamp and Monitor Stand are tapped onto the order. The total with tax is $55.53."),
            (19, "Take payment in cash",
             "Payment opens the payment screen, and Cash is chosen for the full amount."),
            (23, "Sale complete",
             "Validate completes the sale, and the receipt screen shows $55.53 paid."),
        ],
    },
    {
        "key": "invoice", "slug": "odoo-invoice-to-paid", "platform": "odoo",
        "title": "Odoo 20: an invoice posted and marked paid",
        "seconds": 23.7, "recorded": "2026-11-11",
        "guide": "quickbooks-to-odoo-data", "tour": "",
        "chapters": [
            (0, "Open sales order S00027",
             "Sales order S00027 for Azure Interior opens from the quotations list. It's fully delivered and ready "
             "to invoice."),
            (5, "Create the invoice",
             "Create Invoice offers a regular invoice or a down payment. A regular invoice is created as a draft."),
            (10, "Confirm the invoice",
             "Confirm posts the draft as INV/2026/00011."),
            (15, "Register the payment",
             "Pay opens the payment form with the Bank journal and the full $1,104.00, and Create Payment records "
             "it."),
            (20, "Marked paid",
             "The invoice now carries the Paid stamp."),
        ],
    },
]
