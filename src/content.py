"""Resources hub content: FAQ pages, guides and video pages.

Text only. Pages are built in build.py. Tokens filled at build time:
  {NAME}            the business name from config
  [[...]]           no longer allowed: the site shows no prices of ours (Vee, Nov 13, 2026); the build fails

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
     "questions and small changes, in blocks of 10 hours used within 90 days or 20 hours within 180 days.",
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

## When you're better off without a connector

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
        "related": ["shopify-vs-woocommerce-with-a-back-office", "odoo-online-vs-odoo-sh", "shopify-pos-vs-odoo-pos", "quickbooks-to-odoo-data"],
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

## When staying on Odoo Online is the right call

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
        "related": ["stalled-odoo-project", "shopify-connectors-odoo-online", "quickbooks-to-odoo-data", "shopify-pos-vs-odoo-pos"],
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

## When bringing the history over is worth it

Some businesses do need their history in Odoo. A lender or auditor may want several years in one system, sales reports by customer may need to reach back years, or QuickBooks access may be ending. Then history is worth moving, scoped on its own with a fixed price. A Back Office Launch covers the opening data above; full history is one of our larger Odoo projects, quoted after a Systems Roadmap.
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
        "related": ["odoo-vs-quickbooks-and-an-inventory-app", "clean-product-data-before-moving", "odoo-online-vs-odoo-sh", "shopify-connectors-odoo-online", "shopify-pos-vs-odoo-pos"],
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

## When the other register is the better choice

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
        "related": ["opening-a-second-location", "shopify-connectors-odoo-online", "odoo-online-vs-odoo-sh", "quickbooks-to-odoo-data"],
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

## When starting the ERP now makes sense

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
        "related": ["retyping-shopify-orders-into-quickbooks", "shopify-pos-vs-odoo-pos", "shopify-odoo-inventory-sync", "odoo-online-vs-odoo-sh"],
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

## When you don't need a live sync

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
        "related": ["shopify-overselling", "shopify-connectors-odoo-online", "shopify-pos-vs-odoo-pos", "odoo-online-vs-odoo-sh"],
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

## When staying on 19 a while longer is fine

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

## When to start on Custom from day one

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
        "related": ["shopify-odoo-project-cost", "odoo-online-vs-odoo-sh", "shopify-connectors-odoo-online", "odoo-20-changes"],
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

## When Shopify Plus earns its price

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
        "related": ["opening-a-second-location", "shopify-pos-vs-odoo-pos", "when-you-dont-need-an-erp", "shopify-odoo-inventory-sync"],
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

## When a smaller first phase is the better plan

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
        "related": ["stalled-odoo-project", "quickbooks-to-odoo-data", "odoo-standard-vs-custom-plan", "odoo-online-vs-odoo-sh"],
        "notes": ["The 6 to 12 weeks matches the Back Office Launch timeline in config.py. The stage lengths and the "
                  "sample plan are our own planning, not a track record."],
    },    {
        "slug": "shopify-odoo-project-cost",
        "platform": "both",
        "status": "draft",
        "title": "What a Shopify and Odoo setup costs a small business",
        "seo_title": "Shopify and Odoo setup cost for a small business",
        "desc": ("The yearly software bill for a 10-person store on Shopify and Odoo, what outside help costs on "
                 "Odoo's own price list, and what makes a project bigger. Vendor prices dated."),
        "checked": CHECKED,
        "short": ("Budget in two parts. Software is a yearly bill: for a 10-person business on Shopify Grow and Odoo "
                  "Custom with a connector, our worked example lands near $7,200 to $8,400 in year one. Setup help is "
                  "a one-time cost that depends on your data, locations and apps, and it is usually the bigger number."),
        "body": """
## The two bills

Owners often price the software and forget the setup, or the other way round. The software is a subscription you pay the vendors every month or year for as long as you use it. The setup is the work of deciding what goes where, moving your data, connecting the two systems and getting your team through the first weeks. You pay for that once, to whoever does it, whether that's a consultant, Odoo's own team or someone on your staff.

## The software, for a 10-person business

This example is a store with one shop and a website, 10 people who need Odoo, and Shopify connected to Odoo. Prices are the US list prices on shopify.com and odoo.com, paid yearly, checked Nov 11, 2026.

| Item | Per month | First year |
| Shopify Grow (5 staff accounts) | $89 | $1,068 |
| POS Pro for the shop, if staff need roles or in-store stock tools | $89 | $1,068 |
| Odoo Custom, 10 users, first-year price | $490 | $5,880 |
| A connector that runs on the Shopify side | $20–35 | $240–420 |

That comes to $7,188 to $7,368 without POS Pro and $8,256 to $8,436 with it. From the second year, Odoo Custom for 10 users rises to $610 a month on the list price, which adds $1,440 a year.

Why Custom and not Standard? A connector has to reach your Odoo data from outside, and Odoo lists that access (the External API) under Custom. Odoo's own Shopify connector needs Odoo.sh hosting, which also needs Custom and bills hosting on top. The full reasoning is in [Odoo Standard or Custom for 10 users](/guides/odoo-standard-vs-custom-plan).

Leave room for card processing fees, apps you already pay for, hardware for the counter, and Odoo's paid credits if your team plans to use its AI features or text messages.

## What outside help costs

The clearest public price list for Odoo setup work is Odoo's own. Odoo sells Success Packs, blocks of hours run by its project team, and points companies under 50 employees to them. From odoo.com/pricing-packs, checked Nov 6, 2026:

| Pack | Hours | List price |
| Starter | 4 | $580 |
| Basic | 25 | $3,600 |
| Standard | 50 | $7,000 |
| Custom | 100 | $12,500 |
| Pro | 200 | $25,000 |

That works out to about $125 to $145 an hour at list. Odoo takes 15% off a new customer's first pack, and bills travel and the upkeep of custom modules separately. The packs cover Odoo. Work on the Shopify side, the connector and your store move is a separate question.

A Shopify agency or an Odoo partner will usually quote a project rather than hours. Most ask for a discovery step first, paid or free, because the same plan can mean very different work in two businesses.

## What makes a project bigger

- A few hundred clean SKUs load in an afternoon. Several thousand variants with missing barcodes and costs take days of cleanup before anything moves.
- Open orders, open invoices and opening balances are the minimum to bring over. Every extra year of past orders adds mapping, loading and checking.
- Each warehouse, shop or third-party warehouse adds stock rules, transfers and counts to test.
- Registers bring hardware, payment terminals, staff roles and end-of-day closing to set up and train.
- Every app the new setup replaces needs its data moved and its job covered. Custom modules add build time now and upkeep with every Odoo version.
- Testing and data checks need people who know the business. When they can't spare the hours, the dates slide.

## Where budgets go over

Most overruns trace back to two things: scope that grows mid-project and data that turns out messier than anyone said. A fixed fee with a written scope protects you from the first, as long as additions go through a signed change order. A short paid discovery step protects you from the second, because someone looks at the real data before the price is set.

The other quiet cost is the work you already pay for. If your team retypes orders or fixes stock counts by hand, put a number on it with the calculator below and set that next to the setup cost.

@tool

## When a smaller spend is the better choice

You may not need both systems yet. A store with one or two locations, finished goods and a bookkeeper who closes the month without retyping can often stay on Shopify with an accounting app; see [When you don't need an ERP yet](/guides/when-you-dont-need-an-erp). If you only need Odoo and your team has time to do much of the work, a Success Pack bought from Odoo can cost less than a full outside project. A connected setup earns its cost when the same orders, stock and refunds have to agree across your store, your shop counters and your books.
""",
        "faqs": [
            ("Why don't you publish a price for your own work?",
             "Because two stores on the same plan can need very different amounts of work. Product count, history, "
             "locations and apps move the number several times over. We set a fixed fee after a free call and put it "
             "in writing, with the scope, before anything starts."),
            ("Can we start smaller and add Odoo later?",
             "Yes. Many stores start with Shopify and an accounting app, then add Odoo when purchasing, wholesale or "
             "several locations outgrow it. Clean SKUs and accurate stock counts now make that later step shorter "
             "and cheaper."),
            ("Do we pay for the software through you?",
             "No. Shopify, Odoo and any connector vendor bill you directly, at their published prices, in your name. "
             "Our fee covers the work only, and every software line is listed in the proposal so you see the "
             "whole cost."),
        ],
        "sources": [
            ("Shopify pricing", "https://www.shopify.com/pricing", CHECKED),
            ("Odoo pricing (US)", "https://www.odoo.com/pricing", CHECKED),
            ("Odoo Success Packs", "https://www.odoo.com/pricing-packs", "2026-11-06"),
            ("Odoo Apps store: Shopify connectors, 20.0", "https://apps.odoo.com/apps/modules/browse?search=shopify", CHECKED),
            ("Shopify App Store: Odoo connectors", "https://apps.shopify.com/search?q=odoo", "2026-11-06"),
        ],
        "services": ["systems-roadmap", "connection"],
        "related": ["odoo-standard-vs-custom-plan", "when-you-dont-need-an-erp", "odoo-implementation-timeline"],
        "tool": "manual-cost",
        "notes": ["Market numbers are vendor list prices only. The Octura cost report and Clutch agency rates were left "
                  "out until someone re-checks them on the live pages."],
    },    {
        "slug": "shopify-payouts-dont-match-bank",
        "platform": "shopify",
        "status": "draft",
        "title": "Shopify payouts don't match the bank deposit",
        "seo_title": "Why Shopify payouts don't match your sales or bank",
        "desc": ("Why a Shopify Payments deposit is smaller than your sales report. How to match one payout to the "
                 "cent, and book it so fees and refunds stay visible."),
        "checked": "2026-11-13",
        "short": ("A payout is one bank transfer covering many orders, after Shopify has taken out card fees, refunds, "
                  "chargebacks and any held amounts. Sales paid by other methods never pass through it. Match each "
                  "payout from its own transaction export, and book it in parts so the fees and refunds show."),
        "body": """
## Why the deposit is smaller than the sales

Your sales report counts orders. Your bank shows money. Between the two, Shopify Payments groups card payments into one transfer and takes out what it's owed: processing fees on each charge, refunds you issued, chargebacks and their dispute fees, and anything held back as a reserve. Orders paid through PayPal, gift cards, cash at the counter or a manual method never pass through a Shopify Payments payout at all. Both numbers can be right and still disagree.

## What to check, in this order

1. Timing. A payout covers the charges in its own window, which rarely lines up with your calendar month. An order placed late on the 31st can land in next month's deposit.
2. Card fees. Each charge loses its processing fee before it's paid out.
3. Refunds. A refund comes out of the next payout, even when the order was months ago.
4. Chargebacks. A disputed payment is taken back, with a fee, while the dispute is open, and returned if you win.
5. Other payment methods. Sort the orders for the period by how they were paid. Anything outside Shopify Payments settles somewhere else.
6. Holds and adjustments. Reserves and corrections show as their own lines on the payout.

## How to match one payout

Open the payout in Shopify Payments and export its transactions. Add up the charges, then take away refunds, fees, chargebacks and adjustments. The result should equal the deposit to the cent. If it doesn't, the gap is almost always a transaction you've counted in the wrong period, so check the dates on the first and last lines.

Do this once by hand for a busy week. It shows you which of the six causes drive most of your gap, and it's the same check any app or connector will be doing for you later.

## Booking payouts so the books stay honest

When a bookkeeper enters a payout as one deposit labeled sales, the fees vanish into a smaller sales figure and refunds disappear with them. A cleaner pattern uses a clearing account for each payment provider. Orders post sales into it, refunds and fees post against it, and the bank deposit empties it. If the clearing account isn't back to zero after a payout, something hasn't been recorded.

That pattern works in QuickBooks with a payout app and in Odoo with a journal per provider. Your bookkeeper picks the accounts. The setup work is making sure the data arrives split, so nobody has to type the pieces in.

## When matching by hand is enough

A store with a few payouts a week, one currency and only online sales can match each one from the export in a few minutes. Automating it pays when payouts carry hundreds of orders, when counter and online card sales arrive together, when you sell in more than one currency, or when month-end takes your bookkeeper more than an hour or two of matching.
""",
        "faqs": [
            ("Why did a refund for an old order come out of this week's payout?",
             "Refunds are taken from the payout that's open when you issue them, whatever the order date. A March "
             "order refunded in June reduces June's deposit, so June sales and June cash won't line up without that "
             "refund on the list."),
            ("Do cash sales at the counter show up in payouts?",
             "No. Cash goes into the drawer and from there to your own bank deposit. Card sales taken on Shopify POS "
             "through Shopify Payments do show up, mixed in with online card sales, which is why a store with shops "
             "needs a location on each sale to reconcile cleanly."),
            ("Should we record the orders or the payout in the books?",
             "Both, as different events. The orders are sales. The payout is cash moving from Shopify to your bank, "
             "less fees and refunds. Recording only one of them loses either the fees or the timing. Your bookkeeper "
             "decides how each line is coded."),
        ],
        "sources": [],
        "services": ["connection", "odoo-launch"],
        "related": ["retyping-shopify-orders-into-quickbooks", "quickbooks-to-odoo-data", "shopify-odoo-inventory-sync", "shopify-odoo-project-cost"],
        "notes": ["Written from practice; no vendor numbers. Vee should check the Payouts screen wording in the demo "
                  "store before approving, and add a screenshot if it helps."],
    },
    {
        "slug": "shopify-stock-doesnt-match-shelf",
        "platform": "shopify",
        "status": "draft",
        "title": "Shopify stock doesn't match what's on the shelf",
        "seo_title": "Shopify inventory doesn't match the shelf",
        "desc": ("The usual reasons Shopify's counts drift from the stockroom once you sell in person, how to find "
                 "the one causing yours, and the habits that keep counts true."),
        "checked": "2026-11-13",
        "short": ("Counts drift when stock moves without the system hearing about it: deliveries not received, "
                  "returns put back by hand, transfers never marked arrived, or two systems editing the same number. "
                  "Find which one by reading the adjustment history on a few problem items, then fix the habit "
                  "before you buy anything."),
        "body": """
## Where the gap usually comes from

Shopify only knows what someone tells it. Every unit that moves without a matching entry opens a gap, and the gaps add up quietly until a customer orders something that isn't there. The common leaks:

- A delivery is unpacked and shelved, but nobody receives it in Shopify, so the count stays low and the item looks sold out online.
- A return goes back on the shelf, but the refund didn't restock it, or it did restock it and the item was actually damaged.
- Stock moves from the stockroom to the shop floor or a second shop, and the transfer is created but never marked received.
- The counter sells from one location while the item is recorded at another.
- An app, a marketplace or another system also writes stock numbers, and each one overwrites the other.
- Kits and bundles sell as one item while the parts are counted separately.

Shrinkage and miscounts happen too, but they're rarely the main cause in a small store.

## Find your cause before you fix anything

Pick three items that were wrong at the last count. Open each one's inventory history in Shopify and read every change since that count: who changed it, from where, and why. Then walk the item's real path, from delivery to shelf to sale. The place where the real path has a step the history doesn't is your leak.

Three items are usually enough. The same gap tends to show up in all of them.

## Habits that keep counts true

1. One owner per number. Decide which system holds the count for each location, and make every other system read from it.
2. Receive what arrives, the day it arrives, against a purchase order or transfer.
3. Count a little often. Ten fast sellers a week catches drift long before a full stocktake would.
4. Give every adjustment a reason. A pile of unexplained corrections is the clearest sign of a leak.
5. One location per physical place. A shop, a stockroom and a warehouse each get their own.

## When the fix is a back office

If counts drift because two systems both write stock, or because purchasing, kits and wholesale orders live outside Shopify, better habits won't close the gap on their own. That's when a back office such as Odoo owns the count and Shopify shows what's available from it. If the leak is a skipped step at the counter or the loading door, fix the step first. It's cheaper, and you'll need the habit either way.
""",
        "faqs": [
            ("How often should a small store count stock?",
             "Count your fastest sellers every week or two and everything else once a quarter. Short, frequent "
             "counts find drift while it's still easy to trace. A once-a-year stocktake tells you there's a gap "
             "but not where it came from."),
            ("Should returns go straight back into stock?",
             "Only once someone has checked the item. Restock it if it's sellable, and record it as damaged or "
             "written off if it isn't. Restocking everything automatically puts damaged items back on sale and "
             "shows stock you can't ship."),
            ("Can two systems both update the same stock count?",
             "They can, but they shouldn't. When both write the number, each overwrites the other and the count "
             "drifts within days. Choose one owner and have the other follow it on a schedule you can check."),
        ],
        "sources": [],
        "services": ["connection", "odoo-launch"],
        "related": ["shopify-overselling", "when-to-reorder-best-sellers", "shopify-odoo-inventory-sync", "when-you-dont-need-an-erp", "shopify-pos-vs-odoo-pos"],
        "notes": ["Practice-based. Check the inventory history wording against the demo store before approving."],
    },
    {
        "slug": "retail-and-wholesale-one-stock-count",
        "platform": "both",
        "status": "draft",
        "title": "Selling retail and wholesale from one stock count",
        "seo_title": "Stop overselling across Shopify and wholesale",
        "desc": ("Why wholesale orders taken by email or phone oversell your online store. Three ways to share one "
                 "stock count between retail and wholesale."),
        "checked": "2026-11-11",
        "short": ("Overselling starts when a wholesale order is agreed outside the system that feeds your store, so "
                  "the units still look free online. Fix it by entering wholesale orders where stock is counted, "
                  "keeping a small buffer on fast sellers, or holding a separate wholesale stock location for large "
                  "seasonal orders."),
        "body": """
## Why it happens

A buyer emails an order for 200 units. Someone confirms it, adds it to a spreadsheet and plans to pick it next week. Until that order exists in the system your store reads, those 200 units still show as available online. A busy weekend later, retail customers have bought some of them, and either the wholesale order ships short or online orders get refunded.

Prepacks, case quantities and pre-booked seasonal orders make it worse, because large amounts are promised weeks before they leave the building.

## Three ways to share one count

1. Enter every wholesale order where stock lives, the day it's agreed. In Shopify, that means a B2B order or a completed draft order. A draft that's still open doesn't hold stock unless you reserve the items on it. In Odoo, a confirmed sales order reserves the units on its delivery, and a connector sends Shopify only what's still free.
2. Keep a buffer on fast sellers. Show online a little less than you have, so a late wholesale order doesn't take the last units a customer already bought.
3. Give wholesale its own stock for big seasonal orders. Move the pre-booked quantity to a separate location as soon as it's confirmed, so retail never sees it.

Most businesses use the first everywhere and the third for their largest orders.

## What Shopify covers on its own

Shopify's B2B features let wholesale customers order from their own catalogs with their own prices, and those orders take stock like any other. Plans below Plus allow up to 3 catalogs (shopify.com/pricing, checked Nov 11, 2026). Where Shopify gets stretched is many price lists, credit limits, payment terms and statements, and wholesale orders that arrive by phone and need a person to enter them.

## When separate stock is the better choice

If wholesale is most of your volume, ships from a different building, or is sold months ahead against stock you haven't received yet, a shared count adds risk without much benefit. Keep wholesale in its own location or warehouse, move stock to retail on purpose, and let each channel sell only what's been given to it.
""",
        "faqs": [
            ("How big should a stock buffer be?",
             "Start with what one busy day of online sales takes from that item, and adjust after a month. A buffer "
             "that's too large hides stock you could have sold, so keep it on fast sellers only and review it when "
             "sales change."),
            ("Can wholesale customers order straight from our Shopify store?",
             "Yes, through Shopify's B2B features, with company accounts and their own catalogs and prices. The "
             "orders take stock like retail orders. Customers who order by phone or email still need someone to "
             "enter the order the same day."),
            ("What does Odoo add for wholesale?",
             "Price lists per customer, payment terms, credit limits, statements and backorders, all reserving "
             "stock from the same count your store reads. Shopify keeps the storefront and checkout, and the "
             "connector sends it the free quantity."),
        ],
        "sources": [("Shopify pricing", "https://www.shopify.com/pricing", "2026-11-11")],
        "services": ["connection", "odoo-launch"],
        "related": ["shopify-overselling", "when-to-reorder-best-sellers", "shopify-odoo-inventory-sync", "shopify-stock-doesnt-match-shelf", "shopify-plan-for-pos-pro"],
        "notes": ["The draft order reserve behavior should be tried in the demo store before approval."],
    },
    {
        "slug": "stalled-odoo-project",
        "platform": "odoo",
        "status": "draft",
        "title": "A stalled Odoo project: how to tell if it can be saved",
        "seo_title": "Stalled Odoo implementation: rescue it or start over",
        "desc": ("What to collect when an Odoo project has stalled, the checks that show whether it can be finished, "
                 "and the signs that starting over will cost less."),
        "checked": "2026-11-13",
        "short": ("Before deciding anything, get admin access, the subscription in your name and the source code for "
                  "any custom modules. Then check the version, the custom work and the state of the data. Standard "
                  "apps with fixable data are usually worth finishing. Undocumented custom code on an old version "
                  "often isn't."),
        "body": """
## Secure what you own first

A stalled project often ends with the person who built it out of reach. Before anyone judges the setup, make sure you hold these:

- An administrator login to the database, in your company's name.
- The Odoo subscription billed to you, so it can't lapse with someone else's card.
- For Odoo.sh, owner access to the project and to the code repository behind it.
- The source code of every custom or purchased module, plus any license keys for paid ones.
- Whatever was written down: scope, field maps, test notes, emails with decisions.

Ask for credentials to be handed over in a password manager or reset by you, not pasted into email.

## Four checks that decide it

1. Version. A database a version or two behind can be upgraded. One several versions behind turns finishing into an upgrade project as well.
2. Custom code. List every module that isn't Odoo's own. For each, find out what it does, whether you have the code, and whether a standard feature now does the same job.
3. Data. Open products, customers, vendors and stock. Check whether the counts, costs and opening balances are believable. Duplicates and half-finished imports can be cleaned. Data nobody trusts usually gets loaded again.
4. What already works. A sale, a delivery, a purchase and an invoice, run end to end in a copy. Each one that works is work you keep.

## What a rescue looks like

Once the review is written, finishing usually means fixing configuration, removing or replacing custom modules that aren't needed, cleaning and reloading data where needed, and testing in a staging copy before anything changes in the live database. A good review also lists what was done well. You paid for that work, and keeping it is part of the case for finishing.

## When starting over costs less

Starting fresh tends to win when the database is several versions old, when key behavior depends on custom code you don't have or nobody can explain, or when the data has been edited so often that no one trusts a single number. A new database on the current version, with the useful configuration copied across by hand, can come in under the cost of untangling the old one. The written review should price both paths so you can compare them.
""",
        "faqs": [
            ("Who owns the database if a contractor set it up?",
             "Normally you do, if the subscription and the hosting are in your company's name. If they were opened "
             "under the contractor's account, ask for them to be moved to your company before any other work starts."),
            ("Can a stalled project be finished without the original developer?",
             "Usually, if you have the source code and admin access. Standard Odoo apps don't depend on who set them "
             "up. Custom modules without code are the main exception, because they can't be fixed or upgraded."),
            ("How long does a review of a stalled project take?",
             "We do it as a Systems Roadmap, which typically takes 2–3 weeks. Most of that depends on how quickly "
             "access is handed over and how much custom code there is to read."),
        ],
        "sources": [],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["odoo-online-vs-odoo-sh", "odoo-implementation-timeline", "odoo-20-changes"],
        "notes": ["Practice-based. No claims about who worked on the database before, per the FAQ answer on the site."],
    },
    {
        "slug": "who-to-hire-for-shopify-and-odoo",
        "platform": "both",
        "status": "draft",
        "title": "Agency, freelancer, Odoo's own team or a consultant: who to hire",
        "seo_title": "Who to hire for a Shopify and Odoo setup",
        "desc": ("Shopify agency, Odoo partner, Odoo's Success Packs, freelancer or independent consultant. What each "
                 "covers for a small product business."),
        "checked": "2026-11-06",
        "short": ("Each kind of help covers a different part of the job. Shopify agencies build storefronts, Odoo "
                  "partners and Odoo's own Success Packs set up the back office, freelancers take defined tasks, and "
                  "an independent consultant can own the link between them. Pick by who answers for the whole "
                  "result, then by price."),
        "body": """
## The question to ask first

A store that runs Shopify in front and Odoo behind it needs three things done: the storefront, the back office, and the link between them, meaning which system owns which record and how orders, stock, refunds and payouts move. Most problems after go-live live in that link. So before comparing prices, ask each option who answers for it.

## The options side by side

| Option | Usually covers | Usually leaves to you | How it's priced |
| Shopify agency | Theme, apps, checkout, store moves | Stock rules, purchasing, accounting | Project quote, often with a minimum |
| Odoo partner | Odoo setup, data, training | The Shopify side and the storefront | Project quote or hour blocks |
| Odoo Success Pack | Odoo setup run by Odoo's own team | Shopify, the connector, your store move | Prepaid hours on a public list |
| Freelancer | A defined task: an import, a report, a module | Planning, testing, the parts around the task | Hourly or per task |
| Independent consultant | Planning, both systems and the link, within a set scope | Custom development beyond that scope | Usually a fixed fee after discovery |

These are typical shapes, and plenty of firms cross the lines. Ask each one to say in writing what they won't do.

## Odoo's Success Packs, in numbers

Odoo publishes its pack prices, which makes them a useful reference for any quote. From odoo.com/pricing-packs, checked Nov 6, 2026, they run from 4 hours for $580 to 200 hours for $25,000, which works out to about $125 to $145 an hour at list, with 15% off a new customer's first pack. Odoo points companies under 50 employees to these packs. They cover Odoo work, so the Shopify side and the connector still need an owner.

## What to ask anyone you're considering

1. Who answers for orders, stock and refunds agreeing across both systems?
2. Is the fee fixed, and what happens when scope changes?
3. Will we be able to test everything in a copy before it touches the live store?
4. Whose name are the accounts, the subscription and any code in?
5. What do we get at handover, and who removes your access?

The answers matter more than the label on the firm.

## When a single specialist is the better hire

If you only need one side, hire for that side. A store moving platforms with no back office change needs a good Shopify agency or freelancer. A wholesaler with no online store can work straight with Odoo or a partner. A narrow task with a clear spec, such as one import or one report, suits a freelancer. Someone who owns both systems and the link earns their fee when the trouble sits between them.
""",
        "faqs": [
            ("Is a certified Odoo partner always the safer choice?",
             "Partner status tells you a firm sells and implements Odoo at volume. It doesn't tell you whether they "
             "work on the Shopify side, who you'll deal with day to day, or whether the fee is fixed. Ask the same "
             "questions of everyone."),
            ("Can we do the setup ourselves?",
             "Some teams can, especially with standard apps and clean data. The parts that usually need outside help "
             "are the connector decision, the data load and testing before go-live. A short paid review before you "
             "start can tell you which parts to keep in-house."),
            ("Why do agencies have minimum project sizes?",
             "Their teams and processes are built for larger projects, and smaller ones cost them nearly as much to "
             "run. That's reasonable, but it means a 10-person store may be paying for more process than it needs."),
        ],
        "sources": [("Odoo Success Packs", "https://www.odoo.com/pricing-packs", "2026-11-06")],
        "services": ["systems-roadmap", "connection"],
        "related": ["shopify-vs-woocommerce-with-a-back-office", "shopify-odoo-project-cost", "stalled-odoo-project", "odoo-implementation-timeline"],
        "notes": ["No named agencies, partners or freelancers, per the competitor rule. The table is our summary of "
                  "typical scopes, not a survey."],
    },
    {
        "slug": "retyping-shopify-orders-into-quickbooks",
        "platform": "shopify",
        "status": "draft",
        "title": "Retyping Shopify orders into QuickBooks: when it stops being worth it",
        "seo_title": "Retyping Shopify orders into QuickBooks: when to stop",
        "desc": ("What retyping Shopify orders into QuickBooks really costs, the cheaper ways to stop, and the point "
                 "where a back office pays for itself."),
        "checked": "2026-11-13",
        "short": ("Retyping is cheap at ten orders a week and expensive at a hundred, mostly because of the mistakes "
                  "it adds. Start by syncing daily summaries or payouts instead of each order. Move to a back office "
                  "when stock, purchasing or wholesale also live in spreadsheets, because then the typing is only part "
                  "of the cost."),
        "body": """
## What the typing costs

Count it for one normal week: how many orders get entered by hand, how long each takes with checking, and who does it. Then add the time spent finding and fixing the ones that went in wrong. The second number is often larger than the first, and it lands at month-end, when the books don't tie out.

Put your own figures into the calculator in [What a Shopify and Odoo setup costs](/guides/shopify-odoo-project-cost). It turns weekly minutes into hours and dollars a year.

## Cheaper ways to stop

1. Stop entering orders one by one. For many stores, the books need daily or per-payout totals of sales, tax, fees and refunds, not every order. Ask your bookkeeper what level of detail they actually use.
2. Use an accounting app built for Shopify. Several bring payouts or daily summaries into QuickBooks with the fees and refunds split out. Test one on a past month and compare the totals with your bank.
3. Clean up product and tax settings in Shopify first. Whatever you automate copies whatever is there, including mistakes.

## When retyping is a symptom

If the same person also updates stock in a spreadsheet, builds purchase orders from memory and invoices wholesale accounts by hand, the typing is one sign of a bigger gap: sales, stock and money live in different places. An app that syncs orders to QuickBooks won't touch the rest. That's the point where a back office that holds products, stock, purchasing and accounting together starts to pay.

## When to keep things as they are

A store with a few dozen orders a week, finished goods, and a bookkeeper happy with summary entries can keep QuickBooks and add an accounting app. Changing systems costs time and attention, and it's worth it only when the work it removes is bigger than the work it takes. [When you don't need an ERP yet](/guides/when-you-dont-need-an-erp) has the signs.
""",
        "faqs": [
            ("Do we need every Shopify order in QuickBooks?",
             "Often not. Many bookkeepers work from daily or per-payout totals, with the order detail staying in "
             "Shopify. If you invoice wholesale accounts or need customer balances, those orders do need to be in the "
             "books individually."),
            ("Will moving to Odoo mean leaving QuickBooks?",
             "Usually, because Odoo includes accounting. You can keep QuickBooks read-only for past years. Moving "
             "only the open items and opening balances keeps the switch small; years of history is a separate job."),
            ("What's the first step if we want to stop retyping next month?",
             "Ask your bookkeeper which totals they need, then test an accounting app on last month's data. If the "
             "totals match the bank, switch. If they don't, the mismatch tells you what needs cleaning first."),
        ],
        "sources": [],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["odoo-vs-quickbooks-and-an-inventory-app", "quickbooks-to-odoo-data", "shopify-payouts-dont-match-bank", "when-you-dont-need-an-erp"],
        "notes": ["No app names or QuickBooks prices; neither was checked on a live page."],
    },
    {
        "slug": "opening-a-second-location",
        "platform": "shopify",
        "status": "draft",
        "title": "Opening a second shop: registers, transfers and counts",
        "seo_title": "Opening a second shop on Shopify POS: what to set up",
        "desc": ("What changes in Shopify when you open a second shop: locations, POS Pro, staff logins, stock "
                 "transfers and counts. Shopify limits and prices checked on shopify.com."),
        "checked": CHECKED,
        "short": ("A second shop is a new stock location, a new register and new staff logins. Set it up in Shopify "
                  "before opening day, move stock with transfers you receive, and count both shops in the first "
                  "month. Basic, Grow and Advanced each allow up to 10 locations, so the plan rarely has to change."),
        "body": """
## What a second shop changes

With one shop, the stock in Shopify and the stock in the building are close to the same thing. With two, every unit has to be in the right place on paper as well as on the shelf. Sales at each counter take from that shop's count, online orders take from whichever locations you let fulfill them, and moving stock between the two needs a record every time.

## Set up before opening day

1. Add the shop as a location in Shopify, with its own address. Basic, Grow and Advanced each allow up to 10 inventory locations (shopify.com/pricing, checked Nov 11, 2026).
2. Decide whether the new shop fills online orders. Many stores keep online fulfillment at one location at first.
3. Set up the register and card reader for the new shop and run a test sale and a test refund.
4. Give staff their own logins. Grow includes 5 staff accounts and Advanced 15, while Basic has none beyond the owner. If staff at the counter need different permissions, that's POS Pro, at $89 a month per location (checked Nov 11, 2026).
5. Move the opening stock with a transfer, and receive it at the new shop when it arrives.

## Running two shops

- Every move between shops is a transfer, created when it leaves and received when it arrives. A transfer that's never received leaves stock counted nowhere useful.
- Returns go back into the shop that takes them, so each shop's count reflects what's really there.
- Count the fast sellers at both shops weekly for the first month. Early counts catch setup mistakes before they spread.
- Check sales by location each week. It's the quickest way to see whether stock sits in the wrong shop.

## When two shops need more than Shopify

Shopify handles two shops well when you sell finished goods and reorder from a handful of vendors. Purchasing for both shops from sales history, landed costs, wholesale accounts and accounting by location are where stores add a back office. If your second shop also brings a stockroom or a warehouse, read [Shopify POS or Odoo POS for a two-location retailer](/guides/shopify-pos-vs-odoo-pos) before choosing registers.
""",
        "faqs": [
            ("Do we need a higher Shopify plan for a second shop?",
             "Usually not for the shop itself, since Basic, Grow and Advanced each allow up to 10 locations "
             "(checked Nov 11, 2026). The usual reasons to move up are staff accounts and card rates, so count how "
             "many people need their own login."),
            ("Should the new shop fill online orders?",
             "Not at first, for most stores. Keep online orders shipping from one place until both shops' counts "
             "have been accurate for a month, then add the second location if it shortens delivery."),
            ("How do we move stock between shops?",
             "Create a transfer in Shopify when the stock leaves, and receive it at the other shop when it arrives. "
             "Until it's received, the units are in transit and neither shop can sell them."),
        ],
        "sources": [("Shopify pricing", "https://www.shopify.com/pricing", CHECKED)],
        "services": ["store-move", "connection"],
        "related": ["shopify-pos-vs-odoo-pos", "shopify-plan-for-pos-pro", "shopify-stock-doesnt-match-shelf"],
        "notes": ["Transfer 'in transit' wording should be checked in the demo store before approval."],
    },
    {
        "slug": "landed-cost-and-shopify-margins",
        "platform": "both",
        "status": "draft",
        "title": "Why Shopify margins read high when freight and duty are left out",
        "seo_title": "Shopify margins and landed cost: freight and duty",
        "desc": ("How freight, duty and broker fees change what a product really costs you. A worked example with "
                 "sample numbers, and where landed cost belongs once you import regularly."),
        "checked": "2026-11-13",
        "short": ("Shopify's profit figures use the cost per item you type in, which is usually the vendor's price. "
                  "Freight, duty and brokerage sit on separate bills, so margins look better than they are. Add "
                  "those charges to each shipment's cost, or keep cost in a back office that does it on receipt."),
        "body": """
## What the cost field leaves out

Each Shopify variant has a cost per item field, and Shopify's margin and profit figures are built from it. Most stores fill it in once, from the vendor's price list, and never touch it again. The freight bill, the customs duty and the broker's fee arrive weeks later, get paid from the bank and land in the books as general expenses. The product never hears about them.

For a store that buys locally, the gap is small. For one that imports by the container or the pallet, it can be the difference between a product that pays for itself and one that only looks like it does.

## A worked example

Sample numbers, for illustration only. A shipment of 400 units costs $6.00 each from the vendor, so $2,400. Freight is $480, duty is $240 and the customs broker charges $60.

| Cost | Total | Per unit |
| Vendor price | $2,400 | $6.00 |
| Freight, duty and broker | $780 | $1.95 |
| Landed cost | $3,180 | $7.95 |

Sold at $19.00, the margin on the vendor price alone reads 68%. On the landed cost it's 58%. Ten points of margin are missing from every report, and the product's ranking against others can flip once every item carries its own shipping and duty.

## Spreading the extra charges

A shipment usually holds more than one product, so the extra charges have to be shared out. The usual ways are by quantity, by value, by weight or by volume. Value is a sensible default for duty, since duty is charged on value. Weight or volume suits freight, because a carton of light, bulky goods takes the same space whatever it's worth. Pick one rule for each kind of charge and use it every time, so costs are comparable from one shipment to the next.

## Keeping it in Shopify

With a few products and a few shipments a year, a spreadsheet works. List the shipment, split the charges, work out the landed cost per unit and type it into the cost per item field. When a new shipment arrives at a different cost, decide whether to overwrite the old figure or average the two, and do the same every time.

The weak point is that it depends on someone remembering. A shipment that never gets entered leaves last year's cost on the product, and nothing in Shopify will flag it.

## When the back office should hold the cost

Once you import several times a year or carry more than a few dozen products, cost belongs in the system that receives the stock. Odoo can add freight, duty and other charges to a receipt and split them across the products in it, so each unit's cost includes what it took to reach your shelf. Your accounts then show the same cost your margins use. Shopify can still show the price customers pay, while the cost lives in Odoo with the stock.
""",
        "faqs": [
            ("Does Shopify include shipping and duty in product cost?",
             "No. Shopify uses the cost per item entered on each variant. Unless you add freight, duty and other "
             "charges to that figure yourself, they aren't part of the margins Shopify shows."),
            ("Should we average costs or update them with each shipment?",
             "Either works if you pick one and stick to it. Averaging smooths out price changes; replacing the cost "
             "with the newest shipment reacts faster when prices rise. Mixing the two makes reports hard to trust."),
            ("What counts as landed cost?",
             "Anything you pay to get the goods onto your shelf: the vendor's price, freight, insurance in transit, "
             "duty, broker fees and any handling charges at the port or warehouse."),
        ],
        "sources": [],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["when-to-reorder-best-sellers", "shopify-odoo-inventory-sync", "retyping-shopify-orders-into-quickbooks", "when-you-dont-need-an-erp"],
        "notes": ["Practice-based. Odoo 20 split options (equal, quantity, current cost, weight, volume) confirmed in the stock_landed_costs source on Nov 13, 2026."],
    },
    {
        "slug": "shopify-overselling",
        "platform": "both",
        "status": "draft",
        "title": "Overselling on Shopify: where the extra orders come from",
        "seo_title": "Overselling on Shopify: causes and how to stop it",
        "desc": ("The settings and habits that let a Shopify store sell stock it doesn't have, checks you can run "
                 "today, and when a buffer or a back office is the better fix."),
        "checked": "2026-11-13",
        "short": ("Most overselling comes from a few settings and habits: variants set to keep selling at zero, stock "
                  "shared across channels that update late, counts typed over during a sale, and returns put back "
                  "on the shelf before they're back in Shopify. Check each one before adding software."),
        "body": """
## Check the product settings first

Open a product that oversold and look at the variant. Two settings matter. If quantity isn't tracked, Shopify has no count to stop at. If the variant is set to continue selling when out of stock, it will take orders past zero on purpose. Both are easy to switch on by accident during an import, and both are easy to miss on a store with hundreds of variants. Filter the product list for them before looking anywhere else.

## Where else extra orders come from

1. Several channels share one count. A marketplace, a wholesale portal or a second store that copies stock from Shopify only knows what it was last told. If it updates every 15 minutes, a busy quarter hour can sell the same units twice.
2. Counts typed over during trading. Someone counts a shelf in the morning and enters the number at lunch, overwriting the sales made in between. Adjusting by the difference avoids this.
3. Returns restocked on the shelf but not in Shopify, or the other way round.
4. Bundles and kits. If a gift set and the single items draw on the same stock but are counted separately, either can sell what the other already sold.
5. Locations set to fill online orders that don't actually hold the stock, such as a pop-up or a closed shop.

## A buffer while you fix the cause

Holding back a few units of fast sellers, so online shows a little less than the shelf holds, is a reasonable stopgap. It costs a few sales at the very end of a product's stock and saves the refunds and apologies. Treat it as temporary. A buffer that hides a sync problem will hide it until the next big sale.

## When one stock record is the better fix

When stock is sold in more than one place, overselling usually comes from more than one system each keeping its own count. The fix is a single record of stock that every channel reads from, updated as orders arrive. For some stores that's Shopify itself, with other channels connected to it. For stores that also sell wholesale, buy from many vendors or hold stock in a warehouse, the record usually moves to a back office such as Odoo, with Shopify sent what it can sell. [How stock moves between Shopify and Odoo](/guides/shopify-odoo-inventory-sync) covers which way each number travels.
""",
        "faqs": [
            ("Why does Shopify let customers buy items that are out of stock?",
             "Usually because the variant is set to continue selling when out of stock, or because quantity isn't "
             "tracked for it. Both are per-variant settings and can be changed in bulk."),
            ("Can a marketplace sync cause overselling?",
             "Yes. Any channel that copies stock from Shopify on a schedule can sell units that have already gone "
             "elsewhere. The longer the gap between updates, the bigger the risk during busy periods."),
            ("Should we keep a safety buffer on every product?",
             "Only on fast sellers, and only while you fix the cause. A buffer on everything ties up stock you could "
             "sell and makes counts harder to check."),
        ],
        "sources": [],
        "services": ["connection", "odoo-launch"],
        "related": ["shopify-stock-doesnt-match-shelf", "shopify-odoo-inventory-sync", "retail-and-wholesale-one-stock-count"],
        "notes": ["Practice-based. Shopify setting names (track quantity, continue selling when out of stock) should be checked in the demo store before approval."],
    },
    {
        "slug": "shopify-vs-woocommerce-with-a-back-office",
        "platform": "shopify",
        "status": "draft",
        "title": "Shopify or WooCommerce when you also need stock and accounting",
        "seo_title": "Shopify vs WooCommerce with inventory and accounting",
        "desc": ("How Shopify and WooCommerce compare once inventory and accounting sit in a back office. Who "
                 "looks after what, and when WooCommerce is the better choice."),
        "checked": "2026-11-13",
        "short": ("Shopify is a hosted platform you rent; WooCommerce is free software you run on your own WordPress "
                  "site. Once stock and accounting live in a back office, the bigger difference is upkeep: who keeps "
                  "the store, the plugins and the connector working. Stores without a developer usually do better on "
                  "Shopify."),
        "body": """
## Rented or run yourself

Shopify hosts the store for a monthly fee. Updates, security fixes and checkout changes happen on Shopify's side, and you add features with apps. WooCommerce is a free plugin for WordPress. You choose the host, install the updates, keep backups and decide which extensions to trust. That freedom is real, and so is the work that comes with it.

## What changes when a back office joins

Once inventory, purchasing and accounting move to a system such as Odoo, the storefront's own stock and reporting features matter less. What matters more is the link between the two systems.

- On Shopify, connectors use Shopify's published API, which changes on a published schedule. Connector vendors update for it, and you mostly don't see it.
- On WooCommerce, the connector depends on your WordPress version, the WooCommerce version and every plugin that touches orders or products. An update to any of them can change what the connector sees. Someone has to test after updates.
- Either way, the back office should hold the stock count and the storefront should be told what it can sell. [How stock moves between Shopify and Odoo](/guides/shopify-odoo-inventory-sync) explains the usual directions.

## Who looks after it

On Shopify, the person who runs the store can usually handle the store. Apps are installed from Shopify's app store and billed through Shopify. On WooCommerce, it pays to have a developer or a hosting company on call for updates, plugin conflicts and speed problems, especially in the weeks before a busy season. Count that time or that contract in the cost, because it's the part owners tend to leave out.

## Money and checkout

Shopify includes its own payment processing, and using another provider can add a fee on top. WooCommerce works with many payment providers through extensions, and you pay each one's rates. Compare card costs at your own sales volume rather than on headline rates, since the totals depend on your mix of online, in-person and wholesale orders.

## When WooCommerce is the better choice

WooCommerce tends to win when the website is mostly content and the shop is a smaller part of it, when you already have a WordPress developer you trust, or when checkout needs rules that Shopify won't allow and you're prepared to maintain the code. Stores in that position should stay put and make the connection to their back office solid. If you're moving from WooCommerce to Shopify, test orders, redirects and customer accounts before launch, and carry over the order history your accountant needs.
""",
        "faqs": [
            ("Is WooCommerce cheaper than Shopify?",
             "The plugin is free, but hosting, paid extensions, payments and developer time are not. For a store "
             "without its own developer, the yearly total is often closer than it looks, so price the upkeep as "
             "well as the software."),
            ("Can WooCommerce connect to Odoo?",
             "Through third-party connectors, yes. Check which Odoo hosting the connector needs, since Odoo Online "
             "runs only Odoo's standard apps, and test it after every WordPress or WooCommerce update."),
            ("Should we move from WooCommerce to Shopify before adding a back office?",
             "Not always. If the WooCommerce store is stable and someone maintains it, connect it first. If it "
             "breaks after updates or nobody owns it, moving first is usually cheaper than connecting twice."),
        ],
        "sources": [],
        "services": ["store-move", "connection"],
        "related": ["shopify-connectors-odoo-online", "odoo-online-vs-odoo-sh", "who-to-hire-for-shopify-and-odoo"],
        "notes": ["Practice-based. No WooCommerce or hosting prices; Shopify third-party payment fee wording should be checked on shopify.com before approval."],
    },
    {
        "slug": "when-to-reorder-best-sellers",
        "platform": "both",
        "status": "draft",
        "title": "Running out of best sellers: setting reorder points that hold up",
        "seo_title": "When to reorder: reorder points for small retailers",
        "desc": ("How to work out when to reorder each product from sales and supplier lead times, with sample "
                 "numbers. Where a spreadsheet stops and reordering rules in a back office take over."),
        "checked": "2026-11-13",
        "short": ("Reorder when the stock left covers what you'll sell while the next order is on its way, plus a "
                  "small cushion. That point comes from two numbers per product: daily sales and the supplier's "
                  "lead time. Work it out for your best sellers first; they cause most of the lost sales."),
        "body": """
## Why best sellers run out first

Most stores reorder by walking the shelf or scrolling the product list. That works for slow lines and fails for the fast ones, because by the time a gap is visible the next shipment is weeks away. The products that sell fastest are also the ones that go out of stock the longest, and they're usually the ones customers come for.

## The two numbers you need

For each product, you need average daily sales and the supplier's lead time, from the day you place the order to the day it's on your shelf. Use the last 8 to 12 weeks of sales, leaving out days the product was out of stock, since those show zero sales for the wrong reason. Ask suppliers for their usual lead time, then check it against your last few deliveries.

## Working out the reorder point

Sample numbers, for illustration only. A product sells 6 units a day and the supplier takes 14 days.

| Item | Units |
| Sold while the order is on its way (6 x 14) | 84 |
| Cushion for a busy week or a late delivery | 30 |
| Reorder point | 114 |

When stock falls to 114, place the order. How much to order depends on cash, shelf space and the supplier's minimums; enough for four to eight weeks of sales is a common starting point. Revisit the cushion after a season. If you never touch it, it can be smaller. If you still run out, it's too small or the lead time is longer than the supplier says.

## Keeping it in a spreadsheet

A spreadsheet with sales, lead time and reorder point per product works for a few dozen lines. Export sales from Shopify each week, update the averages and flag anything below its reorder point. It breaks down when the export is skipped, when products have many variants, or when stock sits in more than one place.

## When a back office should do it

Once you carry hundreds of variants, buy from several suppliers or sell wholesale as well as retail, the reorder check belongs in the system that holds the stock. In Odoo, reordering rules hold a minimum and maximum per product and location. When forecast stock drops below the minimum, Odoo suggests or creates a purchase order up to the maximum, using the supplier and lead time on the product. The weekly export goes away, and the numbers move as sales do.
""",
        "faqs": [
            ("How much safety stock should a small store keep?",
             "Enough to cover a busy week or a late delivery on your best sellers, and very little on slow lines. "
             "Start with a week of sales for the top products and adjust after a season."),
            ("Should reorder points change with the seasons?",
             "Yes, for products whose sales swing. Recalculate before each busy period from the same weeks last "
             "year, and lower them again afterward so you don't carry extra stock into the quiet months."),
            ("Can Shopify reorder stock automatically?",
             "Shopify tracks stock and can warn you when it runs low through its reports and apps, but most stores "
             "that want purchase orders raised from sales and lead times do it in a back office such as Odoo."),
        ],
        "sources": [],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["shopify-overselling", "shopify-stock-doesnt-match-shelf", "landed-cost-and-shopify-margins"],
        "notes": ["Practice-based. Odoo 20 reordering rule fields (minimum, maximum, auto or manual trigger, lead days) confirmed in stock_orderpoint source Nov 13, 2026. Shopify low-stock FAQ answer kept general on purpose."],
    },
    {
        "slug": "clean-product-data-before-moving",
        "platform": "both",
        "status": "draft",
        "title": "Cleaning up SKUs and product data before you change systems",
        "seo_title": "Clean up SKUs and product data before a migration",
        "desc": ("What to fix in your product list before moving to Shopify or adding Odoo: SKUs, variants, "
                 "barcodes, units and costs. The order to do it in, and what can wait."),
        "checked": "2026-11-13",
        "short": ("Every product needs one unique SKU, the right variants, a unit you buy and sell in, and a cost. "
                  "Fix those before a move, in a copy of your product export, and leave descriptions and photos "
                  "for later. Messy product data is the most common reason a new system's stock numbers are wrong "
                  "from day one."),
        "body": """
## Why it matters before a move

A new system trusts the product list you give it. Two products sharing a SKU, a variant created as a separate product, or a case of 12 entered as one unit will all import without complaint and then break counts, orders and costs for months. Cleaning up beforehand costs days. Cleaning up afterward means fixing sales, stock moves and invoices that already used the bad records.

## What to fix, in order

1. SKUs. One per variant, unique, and never reused for a different item. Pick a simple pattern and write it down. Leave old SKUs in a separate column so past orders can still be matched.
2. Variants. Size and color of the same item should be variants of one product, not separate products. Separate products that are really variants split sales history and make reordering harder.
3. Barcodes. Where you scan at a counter or in a warehouse, each variant needs its own barcode, and no two items can share one.
4. Units. Decide the unit you count and sell in, and record how suppliers sell it, such as cases of 12. Mixing cases and singles in one count is a common reason stock never matches.
5. Costs. A current cost for every item, ideally including freight and duty. See [Why Shopify margins read high](/guides/landed-cost-and-shopify-margins).
6. Dead products. Archive anything you won't sell again. Moving it costs time and clutters every search.

## How to do it without breaking the live store

Work in an export, not the live store. Export products to a spreadsheet, fix the columns above, and keep the original export untouched next to it. Sort by SKU to find duplicates, and by product name to find variants entered as products. Check the cleaned file with whoever counts stock, since they know which items are really the same.

## What can wait

Descriptions, photos, tags and search wording affect how products sell, and they can be improved after the move. Stock counts should be taken close to the switch, and a full count just before go-live is better than a cleaned-up count from a month earlier.

## When it's worth getting help

A few hundred products with consistent SKUs can be cleaned in-house over a week or two. When there are thousands of variants, several sales channels with their own product lists, or SKUs that differ between the website, the shop and the supplier, the cleanup becomes part of the project. In that case it should be scoped and mapped before any data moves.
""",
        "faqs": [
            ("Should we change our SKUs when we move systems?",
             "Only if the current ones aren't unique or follow no pattern. If you do change them, keep the old SKU "
             "in a separate field so past orders, supplier codes and reports can still be matched."),
            ("Do variants need their own barcodes?",
             "Yes, wherever you scan. Each size and color is a different item on the shelf, so each needs its own "
             "barcode. Shared barcodes are one of the quickest ways to make counts drift."),
            ("How long does a product data cleanup take?",
             "For a few hundred products with fairly consistent data, about a week or two alongside normal work. "
             "Thousands of variants across several channels can take longer and are best planned with the move."),
        ],
        "sources": [],
        "services": ["store-move", "systems-roadmap"],
        "related": ["quickbooks-to-odoo-data", "shopify-stock-doesnt-match-shelf", "odoo-implementation-timeline"],
        "notes": ["Practice-based. No vendor facts. US spelling."],
    },
    {
        "slug": "odoo-vs-quickbooks-and-an-inventory-app",
        "platform": "odoo",
        "status": "draft",
        "title": "Odoo or QuickBooks plus an inventory app, for a Shopify store",
        "seo_title": "Odoo vs QuickBooks with an inventory app",
        "desc": ("Comparing one back office with a stack of QuickBooks, an inventory app and Shopify. Where each "
                 "number lives, what breaks between them, and the signs it's time to move."),
        "checked": "2026-11-13",
        "short": ("QuickBooks plus an inventory app works while stock is simple and one person owns the links between "
                  "them. Odoo puts stock, purchasing, sales and accounting in one database, so there are fewer copies "
                  "to keep in step. Move when the gaps between apps cost more than a setup project would."),
        "body": """
## Two ways to run the back office

In the stack, Shopify takes orders, an inventory app holds stock and purchase orders, and QuickBooks keeps the books. Each tool is good at its job and you can swap one without touching the others. The price is that the same order, product and cost exist in three places, and connectors keep them in step.

With one system, Shopify still takes orders and Odoo holds stock, purchasing, wholesale invoicing and accounting together. A product's cost, its stock and the journal entry for a sale come from the same record. You still need one connector, between Shopify and Odoo.

## Where each number lives

| Number | The stack | Odoo |
| Stock on hand | Inventory app, copied to Shopify | Odoo, sent to Shopify |
| Product cost | Inventory app, sometimes QuickBooks too | Odoo |
| Purchase orders | Inventory app | Odoo |
| Wholesale invoices | QuickBooks or the inventory app | Odoo |
| Inventory value in the books | QuickBooks, from what the app sends | Odoo, from stock moves |

Inventory value is where stacks most often drift. If the inventory app sends sales but not adjustments, or sends costs at a different moment than QuickBooks expects, the stock value on the balance sheet stops matching the stock in the building.

## What breaks between apps

- A connector stops quietly after a password change or an app update, and nobody notices for a week.
- A product is renamed in one app and matched as a new item in another.
- Returns are restocked in the inventory app but not credited in QuickBooks, or the other way round.
- Month-end needs someone who understands all three tools and the links between them. When that person is away, the close waits.

None of these is a reason to change on its own. Together, they're the work an owner usually means by "our systems don't talk to each other."

## When QuickBooks plus an app is the right call

Keep the stack when you sell finished goods from one or two locations, buy from a handful of vendors, and someone checks each month that stock value in QuickBooks matches the inventory app. It's cheaper to start, your bookkeeper probably knows QuickBooks already, and each piece can be replaced on its own.

## When one system pays off

Odoo tends to win when you sell wholesale and retail from the same stock, buy from many vendors with landed costs, run more than one warehouse or stockroom, or spend days each month matching the three apps. The move is a project, with data to clean and a cutover to plan. [Moving from QuickBooks to Odoo](/guides/quickbooks-to-odoo-data) lists what to collect before you start.
""",
        "faqs": [
            ("Can QuickBooks track inventory by itself?",
             "QuickBooks Online tracks quantities and cost on its higher plans, which suits a simple product list. "
             "Stores with variants, several locations or purchase orders tied to sales usually add an inventory app."),
            ("Is Odoo harder to learn than QuickBooks?",
             "For the accounting alone, it's about the same. Odoo covers more ground, so staff learn the parts they "
             "use: the warehouse learns receipts and deliveries, and the bookkeeper learns invoices and the "
             "reconciliation screens."),
            ("Can we keep QuickBooks for accounting and use Odoo only for inventory?",
             "It's possible, but it brings back the same gap between stock value and the books. Most stores that "
             "move stock to Odoo move accounting too, and keep QuickBooks read-only for past years."),
        ],
        "sources": [],
        "services": ["systems-roadmap", "odoo-launch"],
        "related": ["retyping-shopify-orders-into-quickbooks", "quickbooks-to-odoo-data", "when-you-dont-need-an-erp", "shopify-odoo-inventory-sync"],
        "notes": ["Practice-based. QuickBooks Online inventory tracking on higher plans is from general knowledge; check intuit.com plan page before approval. No QuickBooks or app prices."],
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
