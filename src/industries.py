"""Industry pages. One entry per industry: the problems that cost that kind of business the most, and the fix.

Facts here are checked against a primary source or our own Odoo 20 sandbox before they ship (see `sources`).
Problems are written from what owners in each trade ask about most; no figures from vendor blogs.
Media keys point at config.ODOO_CLIPS / ODOO_REEL (clip) or config.SCREENS (screen); a missing key is skipped.
"""

INDUSTRIES = [
    {
        "slug": "apparel", "short": "Apparel and footwear", "scene": "apparel", "screen": "scene-locations", "color": "c-coral",
        "title": "Shopify and Odoo for apparel and footwear brands",
        "h1": "Shopify and Odoo for apparel and footwear brands",
        "desc": ("Size and color stock that stays right across your store, your shops and wholesale. Shopify and "
                 "Odoo set up and connected for apparel brands, for a fixed fee."),
        "lead": ("One style can run to dozens of sizes and colors, sold online, in your own shops and to wholesale "
                 "accounts at once. Trouble starts when each of those keeps its own count."),
        "card": "The last medium in navy sells twice: once online, once at the counter.",
        "problems": [
            ("One size sells out twice",
             "An online order comes in for a medium that already sold at the counter. You refund it, apologize, "
             "and that customer shops somewhere else next season.",
             "Odoo keeps one count for each size and color in each location and sends Shopify what is actually free "
             "to sell, shop by shop. A confirmed wholesale order holds its stock straight away.",
             ("clip", "locations")),
            ("Returns that never make it back to stock",
             "A returned jacket sits in a bin by the door. The refund went out days ago, but the jacket isn't "
             "counted until someone finds it.",
             "A return becomes a receipt in Odoo. The item goes back into stock once it's checked, or into a "
             "damaged location if it can't be sold, and the credit note follows from the same record.",
             ("clip", "return")),
            ("Reordering a style when a size ran out",
             "The best-selling sizes sell through while the slow ones pile up, because reorders are placed for "
             "the style as a whole.",
             "Reorder rules sit on each size and color, with a minimum, a maximum and the vendor's lead time. "
             "Odoo drafts the purchase order from what actually sold.",
             ("clip", "purchase")),
            ("Purchase orders with nowhere to live",
             "Shopify retired its Stocky app on August 31, 2026. Brands that ran purchase orders and transfers "
             "in Stocky moved them back into spreadsheets.",
             "Purchasing, receipts and transfers between shops run in Odoo, and Shopify gets the new counts after "
             "each one.",
             None),
        ],
        "start": ("connection", "odoo-launch",
                  "Already on Odoo? Store to Back Office Sync connects it to your shops. Starting from "
                  "spreadsheets? Back Office Launch sets Odoo up first."),
        "faqs": [
            ("Can Shopify handle all our sizes and colors?",
             "For selling, yes. Where it runs short is stock and purchasing across several channels, and that "
             "part moves to Odoo."),
            ("We only sell online. Do we need Odoo?",
             "Probably not yet. One channel, one or two locations and no wholesale usually run fine on Shopify "
             "with an inventory app. Our guide on when you don't need an ERP covers the signs that change it."),
            ("Where do wholesale orders go?",
             "Either into Shopify B2B, which every Shopify plan has had since April 2, 2026, or straight into "
             "Odoo as quotations. Both take stock from the same count."),
        ],
        "guides": ["when-you-dont-need-an-erp", "shopify-odoo-inventory-sync"],
        "sources": [
            ("Shopify changelog: key B2B features on non-Plus plans",
             "https://changelog.shopify.com/posts/key-b2b-features-now-available-on-non-plus-plans"),
        ],
    },
    {
        "slug": "home-and-furniture", "short": "Home and furniture", "scene": "furniture", "screen": "scene-landed", "color": "c-lilac",
        "title": "Shopify and Odoo for furniture and home goods sellers",
        "h1": "Shopify and Odoo for furniture and home goods sellers",
        "desc": ("Landed costs, made-to-order pieces and long lead times handled in Odoo and shown in Shopify. "
                 "Set up and connected for furniture sellers, for a fixed fee."),
        "lead": ("Big pieces, long lead times and freight bills that arrive after the sale. A furniture business "
                 "can look profitable in Shopify and still lose money on the delivery."),
        "card": "The sofa's margin looks fine until the freight bill arrives a month later.",
        "problems": [
            ("Margins that leave out freight and duty",
             "A sofa's real cost includes the ocean freight, the duty and the truck to your warehouse. When those "
             "bills never reach the product cost, every margin report is too high.",
             "Landed costs in Odoo spread freight, duty and handling across the pieces they came with, so cost "
             "of goods and margin show what you actually paid.",
             ("clip", "landed")),
            ("Special orders tracked in email",
             "A customer orders a chair in a fabric you don't stock. Someone emails the maker, notes it in a "
             "spreadsheet, and three weeks later nobody knows where it stands.",
             "With make-to-order and dropship routes, the sale creates the purchase order to the maker, linked to "
             "the customer's order. Anyone can see where it stands from either record.",
             None),
            ("Long lead times and empty showrooms",
             "Pieces that take twelve weeks to arrive run out before anyone notices the reorder date has passed.",
             "Vendor lead times and reorder rules on each product. Odoo shows what's on order and when it lands, "
             "so you reorder in time and quote honest delivery dates.",
             ("clip", "purchase")),
            ("Damaged deliveries",
             "A table arrives with a cracked leg. The replacement goes out, but the broken one stays in your "
             "stock count.",
             "Damaged pieces come back into their own location, to be repaired, sold as seconds or written off, "
             "with the credit note tied to the order.",
             ("clip", "return")),
        ],
        "start": ("odoo-launch", "systems-roadmap",
                  "Back Office Launch sets up Odoo with landed costs and your makers as vendors. With several "
                  "showrooms or a wholesale channel, a Systems Roadmap comes first."),
        "faqs": [
            ("Can Odoo send orders straight to our makers?",
             "Yes. A dropship route turns the customer's order into a purchase order to the maker, who ships to "
             "the customer. The order and the purchase stay linked."),
            ("Can Shopify show a delivery estimate for each piece?",
             "Yes, as product information on the page. Whether it updates from Odoo on its own depends on the "
             "connector, so we check that before you pick one."),
            ("Do you set up delivery routes and truck scheduling?",
             "We set up delivery orders, dates and the carriers you use. Route planning for your own trucks needs "
             "a separate tool, and we'll say so on the first call if you need one."),
        ],
        "guides": ["odoo-standard-vs-custom-plan", "odoo-implementation-timeline"],
        "sources": [],
    },
    {
        "slug": "food-and-beverage", "short": "Food and beverage", "scene": "food", "screen": "scene-lots", "color": "c-mint",
        "title": "Shopify and Odoo for food and beverage brands",
        "h1": "Shopify and Odoo for food and beverage brands",
        "desc": ("Lot numbers, best-by dates and oldest-first picking in Odoo, with Shopify selling from the same "
                 "count. Set up for food and beverage brands, for a fixed fee."),
        "lead": ("Every case has a lot number and a best-by date. Shopify doesn't track either on its own, so the "
                 "oldest stock waits at the back while fresh stock ships first."),
        "card": "A recall call comes in, and the lot numbers are in four spreadsheets.",
        "problems": [
            ("No lot or best-by date on what you sell",
             "Lots get written on the case and nowhere else. When a customer asks which batch they received, "
             "nobody can say.",
             "Odoo records the lot and its dates when stock is received and carries them onto every delivery, so "
             "each order shows exactly which lot went out.",
             ("clip", "lots")),
            ("Fresh stock ships before old stock",
             "Pickers grab the case at the front. The older lot expires on the shelf and gets thrown out.",
             "First-expiry-first-out picking: Odoo reserves the lot that expires soonest, and a report shows what "
             "is close to its date while there's still time to sell it.",
             None),
            ("A recall means a day in spreadsheets",
             "A supplier flags an ingredient. You need every customer who received the affected lot, today.",
             "Odoo traces a lot forward to every delivery and customer in a few clicks, and back to the receipt "
             "it came from.",
             None),
            ("Wholesale accounts at their own prices",
             "Grocers and cafes each pay a different price, and the price list lives in someone's inbox.",
             "Price lists for each account or group, with payment terms, in Odoo. Wholesale buyers can order "
             "through Shopify B2B at their own prices.",
             ("clip", "pricelist")),
        ],
        "start": ("odoo-launch", "systems-roadmap",
                  "Back Office Launch sets up lots, dates and oldest-first picking. If you make your own product "
                  "or use a co-packer, a Systems Roadmap comes first to plan that part."),
        "faqs": [
            ("Do you handle FDA or food safety compliance?",
             "No. We set up the records that compliance work depends on: lots, dates and where each lot went. "
             "The compliance program itself stays with you and your advisors."),
            ("Do you work with alcohol brands?",
             "No. Alcohol has its own licensing and shipping rules, and it's outside the work we take on."),
            ("Can online customers see best-by dates?",
             "Not by default. If it matters for what you sell, we can show it as product information, kept up to "
             "date when stock changes."),
        ],
        "guides": ["when-you-dont-need-an-erp", "quickbooks-to-odoo-data"],
        "sources": [],
    },
    {
        "slug": "health-and-beauty", "short": "Health and beauty", "scene": "beauty", "screen": "scene-purchase", "color": "c-blue",
        "title": "Shopify and Odoo for health and beauty brands",
        "h1": "Shopify and Odoo for health and beauty brands",
        "desc": ("Batches, expiry dates, kits and packaging stock in Odoo, with one count behind Shopify and your "
                 "other channels. Set up for beauty brands, for a fixed fee."),
        "lead": ("Batches with expiry dates, gift sets made from other products, and bottles, pumps and labels "
                 "that run out before the product does. Most of it ends up in spreadsheets beside Shopify."),
        "card": "A full batch is ready to fill, and the pumps are three weeks away.",
        "problems": [
            ("Batches and expiry dates",
             "A customer reports a reaction and asks which batch they bought. The answer is in a notebook, if "
             "anywhere.",
             "Lot numbers and expiry dates recorded on receipt, carried onto every order, and the oldest batch "
             "picked first.",
             ("clip", "lots")),
            ("Gift sets and bundles",
             "A holiday set sells out on the site while its parts sit on the shelf, or the parts sell out and the "
             "set keeps selling.",
             "In Odoo a set is a kit: selling one takes each part out of stock, and Shopify only shows as many "
             "sets as the parts allow.",
             None),
            ("Packaging that stops a ready batch",
             "The product is made, but the bottles or labels haven't arrived, and nothing ships.",
             "Bottles, pumps and labels are tracked as stock too, with reorder rules from your sales forecast, "
             "so a purchase order goes out before they run short.",
             ("clip", "purchase")),
            ("A different count on every channel",
             "Shopify, a marketplace and two retailers each think they know how much you have.",
             "One count in Odoo. Shopify and other connected channels sell from it, and wholesale orders reserve "
             "from it.",
             ("clip", "locations")),
        ],
        "start": ("systems-roadmap", "odoo-launch",
                  "A Systems Roadmap maps your channels, kits and packaging first. Back Office Launch then sets "
                  "it up in Odoo."),
        "faqs": [
            ("Do you handle product registration or labeling rules?",
             "No. We set up the records that work depends on, such as batches and expiry dates. Registration and "
             "labeling stay with you and your advisors."),
            ("Can Odoo take orders from Amazon?",
             "Yes, through a connector. Which one fits depends on your Odoo plan and hosting, and we compare them "
             "in writing before you buy."),
            ("Do you set up subscriptions?",
             "We connect Shopify subscription orders to Odoo like any other order. The subscription app itself "
             "stays in Shopify."),
        ],
        "guides": ["shopify-connectors-odoo-online", "odoo-online-vs-odoo-sh"],
        "sources": [],
    },
    {
        "slug": "wholesale", "short": "Wholesale and distribution", "scene": "wholesale", "screen": "scene-pricelist", "color": "c-yellow",
        "title": "Shopify and Odoo for wholesalers and distributors",
        "h1": "Shopify and Odoo for wholesalers and distributors",
        "desc": ("Account price lists, payment terms and orders entered once. Shopify B2B and Odoo set up and "
                 "connected for small wholesalers and distributors, for a fixed fee."),
        "lead": ("Orders arrive by email, phone and spreadsheet, each account has its own prices, and someone "
                 "retypes it all into QuickBooks. That's a back office problem before it's a website problem."),
        "card": "Every order gets typed twice, and one account keeps getting last year's price.",
        "problems": [
            ("The wrong price on the wrong account",
             "A good customer gets charged list price, or a small one gets the big account's discount, and you "
             "find out at month end.",
             "Price lists for each account or group in Odoo. Shopify B2B, on every plan since April 2, 2026, "
             "shows each buyer their own catalog, with up to three catalogs below Shopify Plus.",
             ("clip", "pricelist")),
            ("Net terms and credit kept in your head",
             "One account pays in 30 days, another in 60, and a third is two invoices behind but still ordering.",
             "Payment terms and credit limits on each account, a warning when an order goes over, and an aged "
             "receivables report that shows who owes what.",
             ("clip", "invoice")),
            ("Orders typed in twice",
             "An order comes in by email, gets typed into a spreadsheet, then into QuickBooks for the invoice.",
             "An order entered once, in Shopify or in Odoo, becomes the delivery and the invoice. Odoo does the "
             "accounting, so there is nothing to retype.",
             ("clip", "sale")),
            ("A large retailer asks for EDI",
             "A chain wants purchase orders and invoices by EDI, and nobody on the team knows where to start.",
             "Odoo doesn't send US retail EDI on its own. When you need it, we scope a third-party EDI provider "
             "in the Systems Roadmap and connect it to Odoo.",
             None),
        ],
        "start": ("systems-roadmap", "odoo-launch",
                  "A Systems Roadmap sorts out price lists, terms, channels and EDI first. Back Office Launch "
                  "then sets it up."),
        "faqs": [
            ("Should wholesale buyers order on Shopify or in Odoo?",
             "If they like to order online, Shopify B2B. If your team takes orders by phone or email, Odoo. Many "
             "wholesalers use both, from the same stock and the same price lists."),
            ("Can you move us off QuickBooks?",
             "Yes. Odoo takes over invoicing and accounting, and we move customers, vendors, products and open "
             "balances. Our guide on moving from QuickBooks lists what to gather first."),
            ("Do you set up EDI?",
             "We scope it and connect a third-party EDI provider to Odoo. The provider charges its own fees, and "
             "we list them in the Roadmap before you commit."),
        ],
        "guides": ["quickbooks-to-odoo-data", "odoo-standard-vs-custom-plan"],
        "sources": [
            ("Shopify changelog: key B2B features on non-Plus plans",
             "https://changelog.shopify.com/posts/key-b2b-features-now-available-on-non-plus-plans"),
        ],
    },
]

BY_SLUG = {i["slug"]: i for i in INDUSTRIES}
