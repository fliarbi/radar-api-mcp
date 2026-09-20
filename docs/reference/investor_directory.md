# Investor directory API: published profiles, lists and locations

[All endpoints](README.md) · [Workflow guide](../guides/investor-data-api.md)

Discover published investor pages without guessing URL slugs. The directory includes page counts and selected profiles, lists, cities and sectors. It is particularly useful when an application needs navigable investor research pages rather than a free-form company query.

## Route, authentication and credits

**`POST /v1/investors/directory`** · MCP tool **`investor_directory`** · key scope **`investors`**.
Use an API key in `Authorization: Bearer` or `X-API-Key`; a Radar browser session
is used for account management, not as a replacement data credential.
In account mode this operation costs one credit for a successful operation. REST and MCP share the account
budget and upstream plan gates. The live capture below used a local preview key,
so it contains no `meta.billing` charge. See [pricing](../guides/pricing-pay-per-use.md).

## Request parameters

This operation accepts an empty JSON object: `{}`.

Unknown fields are rejected. Domain fields take a website domain without a scheme,
path or port; a leading `www.` is removed. Text filters reject control characters,
quotes, backslashes and semicolons. Dates use `YYYY-MM-DD`; a start date/year must
not exceed its end. Model-valid filters can still be restricted by the linked plan.

## Run the captured request

Set `RADAR_API_URL` to your operator-supplied private base URL without a trailing
slash, and load `RADAR_API_KEY` from your secret store.

```bash
curl --fail-with-body -X POST "$RADAR_API_URL/v1/investors/directory" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: investor_directory -->
```json
{
  "name": "investor_directory",
  "arguments": {
    "request": {}
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: investor_directory -->
```json
{
  "ok": true,
  "feature": "investor_directory",
  "data": {
    "counts": {
      "investor_list": 7589,
      "investor_list_angel": 1450,
      "investor_profile": 5269
    },
    "top_lists": [
      {
        "slug": "fintech-investors-in-london",
        "city_display": "London",
        "companies": 1235,
        "family": "investors",
        "h1": "FinTech investors in London",
        "investors": 3878,
        "sector_display": "FinTech",
        "usd": 216769236909
      },
      {
        "slug": "fintech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 1062,
        "family": "investors",
        "h1": "FinTech investors in New York City",
        "investors": 3425,
        "sector_display": "FinTech",
        "usd": 289019143774
      },
      {
        "slug": "fintech-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 1045,
        "family": "investors",
        "h1": "FinTech investors in San Francisco",
        "investors": 3476,
        "sector_display": "FinTech",
        "usd": 408291418941
      },
      {
        "slug": "b2c-e-commerce-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 544,
        "family": "investors",
        "h1": "B2C E-Commerce investors in Bengaluru",
        "investors": 6413,
        "sector_display": "B2C E-Commerce",
        "usd": 383262209966
      },
      {
        "slug": "retail-tech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 517,
        "family": "investors",
        "h1": "Retail Tech investors in Bengaluru",
        "investors": 6127,
        "sector_display": "Retail Tech",
        "usd": 267547578231
      },
      {
        "slug": "fintech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 461,
        "family": "investors",
        "h1": "FinTech investors in Bengaluru",
        "investors": 5456,
        "sector_display": "FinTech",
        "usd": 91647148872
      },
      {
        "slug": "b2c-e-commerce-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 398,
        "family": "investors",
        "h1": "B2C E-Commerce investors in Mumbai",
        "investors": 5023,
        "sector_display": "B2C E-Commerce",
        "usd": 60311330698
      },
      {
        "slug": "artificial-intelligence-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 755,
        "family": "investors",
        "h1": "Artificial Intelligence investors in San Francisco",
        "investors": 2608,
        "sector_display": "Artificial Intelligence",
        "usd": 2065572563004
      },
      {
        "slug": "fintech-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 381,
        "family": "investors",
        "h1": "FinTech investors in Mumbai",
        "investors": 5086,
        "sector_display": "FinTech",
        "usd": 58018992803
      },
      {
        "slug": "retail-tech-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 345,
        "family": "investors",
        "h1": "Retail Tech investors in Mumbai",
        "investors": 4680,
        "sector_display": "Retail Tech",
        "usd": 54625183344
      },
      {
        "slug": "healthtech-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 681,
        "family": "investors",
        "h1": "HealthTech investors in San Francisco",
        "investors": 2018,
        "sector_display": "HealthTech",
        "usd": 167163563273
      },
      {
        "slug": "fintech-investors-in-singapore",
        "city_display": "Singapore",
        "companies": 587,
        "family": "investors",
        "h1": "FinTech investors in Singapore",
        "investors": 2231,
        "sector_display": "FinTech",
        "usd": 91825257442
      },
      {
        "slug": "b2c-e-commerce-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 309,
        "family": "investors",
        "h1": "B2C E-Commerce investors in Gurugram",
        "investors": 3610,
        "sector_display": "B2C E-Commerce",
        "usd": 76309560282
      },
      {
        "slug": "b2c-e-commerce-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 596,
        "family": "investors",
        "h1": "B2C E-Commerce investors in New York City",
        "investors": 1734,
        "sector_display": "B2C E-Commerce",
        "usd": 103644539068
      },
      {
        "slug": "b2c-e-commerce-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 302,
        "family": "investors",
        "h1": "B2C E-Commerce investors in Delhi",
        "investors": 3416,
        "sector_display": "B2C E-Commerce",
        "usd": 12650809837
      },
      {
        "slug": "healthtech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 552,
        "family": "investors",
        "h1": "HealthTech investors in New York City",
        "investors": 1847,
        "sector_display": "HealthTech",
        "usd": 133014537433
      },
      {
        "slug": "healthtech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 285,
        "family": "investors",
        "h1": "HealthTech investors in Bengaluru",
        "investors": 3563,
        "sector_display": "HealthTech",
        "usd": 25701924129
      },
      {
        "slug": "b2c-e-commerce-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 556,
        "family": "investors",
        "h1": "B2C E-Commerce investors in San Francisco",
        "investors": 1660,
        "sector_display": "B2C E-Commerce",
        "usd": 205013539460
      },
      {
        "slug": "retail-tech-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 283,
        "family": "investors",
        "h1": "Retail Tech investors in Gurugram",
        "investors": 3164,
        "sector_display": "Retail Tech",
        "usd": 59741257237
      },
      {
        "slug": "b2c-e-commerce-investors-in-london",
        "city_display": "London",
        "companies": 582,
        "family": "investors",
        "h1": "B2C E-Commerce investors in London",
        "investors": 1521,
        "sector_display": "B2C E-Commerce",
        "usd": 58492269115
      },
      {
        "slug": "life-sciences-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 526,
        "family": "investors",
        "h1": "Life Sciences investors in San Francisco",
        "investors": 1650,
        "sector_display": "Life Sciences",
        "usd": 240618012331
      },
      {
        "slug": "blockchain-investors-in-singapore",
        "city_display": "Singapore",
        "companies": 488,
        "family": "investors",
        "h1": "Blockchain investors in Singapore",
        "investors": 1732,
        "sector_display": "Blockchain",
        "usd": 27716744018
      },
      {
        "slug": "marketingtech-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 502,
        "family": "investors",
        "h1": "MarketingTech investors in San Francisco",
        "investors": 1461,
        "sector_display": "MarketingTech",
        "usd": 58868159269
      },
      {
        "slug": "life-sciences-investors-in-cambridge",
        "city_display": "Cambridge",
        "companies": 499,
        "family": "investors",
        "h1": "Life Sciences investors in Cambridge",
        "investors": 1421,
        "sector_display": "Life Sciences",
        "usd": 327243147548
      },
      {
        "slug": "retail-tech-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 257,
        "family": "investors",
        "h1": "Retail Tech investors in Delhi",
        "investors": 2665,
        "sector_display": "Retail Tech",
        "usd": 18407716969
      },
      {
        "slug": "edtech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 231,
        "family": "investors",
        "h1": "EdTech investors in Bengaluru",
        "investors": 2951,
        "sector_display": "EdTech",
        "usd": 62503381828
      },
      {
        "slug": "auto-tech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 203,
        "family": "investors",
        "h1": "Auto Tech investors in Bengaluru",
        "investors": 3170,
        "sector_display": "Auto Tech",
        "usd": 61101084841
      },
      {
        "slug": "blockchain-technology-investors-in-singapore",
        "city_display": "Singapore",
        "companies": 418,
        "family": "investors",
        "h1": "Blockchain Technology investors in Singapore",
        "investors": 1516,
        "sector_display": "Blockchain Technology",
        "usd": 24784714812
      },
      {
        "slug": "hrtech-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 396,
        "family": "investors",
        "h1": "HRTech investors in San Francisco",
        "investors": 1508,
        "sector_display": "HRTech",
        "usd": 99825986309
      },
      {
        "slug": "food-tech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 180,
        "family": "investors",
        "h1": "Food Tech investors in Bengaluru",
        "investors": 3142,
        "sector_display": "Food Tech",
        "usd": 152753753407
      },
      {
        "slug": "healthtech-investors-in-london",
        "city_display": "London",
        "companies": 419,
        "family": "investors",
        "h1": "HealthTech investors in London",
        "investors": 1255,
        "sector_display": "HealthTech",
        "usd": 40343131026
      },
      {
        "slug": "future-of-work-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 353,
        "family": "investors",
        "h1": "Future of Work investors in San Francisco",
        "investors": 1466,
        "sector_display": "Future of Work",
        "usd": 94864477350
      },
      {
        "slug": "investment-tech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 381,
        "family": "investors",
        "h1": "Investment Tech investors in New York City",
        "investors": 1322,
        "sector_display": "Investment Tech",
        "usd": 88304446484
      },
      {
        "slug": "investment-tech-investors-in-london",
        "city_display": "London",
        "companies": 366,
        "family": "investors",
        "h1": "Investment Tech investors in London",
        "investors": 1353,
        "sector_display": "Investment Tech",
        "usd": 33466567587
      },
      {
        "slug": "internet-first-brands-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 180,
        "family": "investors",
        "h1": "Internet First Brands investors in Bengaluru",
        "investors": 2637,
        "sector_display": "Internet First Brands",
        "usd": 22016477690
      },
      {
        "slug": "internet-first-brands-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 189,
        "family": "investors",
        "h1": "Internet First Brands investors in Mumbai",
        "investors": 2503,
        "sector_display": "Internet First Brands",
        "usd": 7948500446
      },
      {
        "slug": "marketingtech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 355,
        "family": "investors",
        "h1": "MarketingTech investors in New York City",
        "investors": 1312,
        "sector_display": "MarketingTech",
        "usd": 42344740584
      },
      {
        "slug": "web-3-0-investors-in-singapore",
        "city_display": "Singapore",
        "companies": 341,
        "family": "investors",
        "h1": "Web 3.0 investors in Singapore",
        "investors": 1337,
        "sector_display": "Web 3.0",
        "usd": 16913966509
      },
      {
        "slug": "commerce-enablers-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 167,
        "family": "investors",
        "h1": "Commerce Enablers investors in Bengaluru",
        "investors": 2536,
        "sector_display": "Commerce Enablers",
        "usd": 30656281796
      },
      {
        "slug": "blockchain-in-financial-services-investors-in-singapore",
        "city_display": "Singapore",
        "companies": 325,
        "family": "investors",
        "h1": "Blockchain in Financial Services investors in Singapore",
        "investors": 1278,
        "sector_display": "Blockchain in Financial Services",
        "usd": 21551097981
      },
      {
        "slug": "web-3-0-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 305,
        "family": "investors",
        "h1": "Web 3.0 investors in San Francisco",
        "investors": 1355,
        "sector_display": "Web 3.0",
        "usd": 68413348569
      },
      {
        "slug": "nbfc-lenders-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 157,
        "family": "investors",
        "h1": "NBFC Lenders investors in Mumbai",
        "investors": 2429,
        "sector_display": "NBFC Lenders",
        "usd": 54064602873
      },
      {
        "slug": "life-sciences-investors-in-san-diego",
        "city_display": "San Diego",
        "companies": 353,
        "family": "investors",
        "h1": "Life Sciences investors in San Diego",
        "investors": 1050,
        "sector_display": "Life Sciences",
        "usd": 158296315770
      },
      {
        "slug": "blockchain-in-financial-services-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 274,
        "family": "investors",
        "h1": "Blockchain in Financial Services investors in San Francisco",
        "investors": 1319,
        "sector_display": "Blockchain in Financial Services",
        "usd": 80872925467
      },
      {
        "slug": "artificial-intelligence-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 263,
        "family": "investors",
        "h1": "Artificial Intelligence investors in New York City",
        "investors": 1369,
        "sector_display": "Artificial Intelligence",
        "usd": 133653345916
      },
      {
        "slug": "cybersecurity-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 308,
        "family": "investors",
        "h1": "Cybersecurity investors in San Francisco",
        "investors": 1154,
        "sector_display": "Cybersecurity",
        "usd": 63363717270
      },
      {
        "slug": "commerce-enablers-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 297,
        "family": "investors",
        "h1": "Commerce Enablers investors in San Francisco",
        "investors": 1179,
        "sector_display": "Commerce Enablers",
        "usd": 146970616725
      },
      {
        "slug": "artificial-intelligence-investors-in-london",
        "city_display": "London",
        "companies": 268,
        "family": "investors",
        "h1": "Artificial Intelligence investors in London",
        "investors": 1189,
        "sector_display": "Artificial Intelligence",
        "usd": 109731665135
      },
      {
        "slug": "artificial-intelligence-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 179,
        "family": "investors",
        "h1": "Artificial Intelligence investors in Bengaluru",
        "investors": 1767,
        "sector_display": "Artificial Intelligence",
        "usd": 7680515708
      },
      {
        "slug": "fintech-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 156,
        "family": "investors",
        "h1": "FinTech investors in Gurugram",
        "investors": 2021,
        "sector_display": "FinTech",
        "usd": 26879076393
      },
      {
        "slug": "ai-as-a-service-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 253,
        "family": "investors",
        "h1": "AI as a Service investors in San Francisco",
        "investors": 1231,
        "sector_display": "AI as a Service",
        "usd": 1855704018006
      },
      {
        "slug": "hrtech-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 257,
        "family": "investors",
        "h1": "HRTech investors in New York City",
        "investors": 1206,
        "sector_display": "HRTech",
        "usd": 67719834373
      },
      {
        "slug": "hrtech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 170,
        "family": "investors",
        "h1": "HRTech investors in Bengaluru",
        "investors": 1767,
        "sector_display": "HRTech",
        "usd": 13910704456
      },
      {
        "slug": "hrtech-investors-in-london",
        "city_display": "London",
        "companies": 269,
        "family": "investors",
        "h1": "HRTech investors in London",
        "investors": 1053,
        "sector_display": "HRTech",
        "usd": 18513316209
      },
      {
        "slug": "biopharmaceuticals-investors-in-cambridge",
        "city_display": "Cambridge",
        "companies": 307,
        "family": "investors",
        "h1": "Biopharmaceuticals investors in Cambridge",
        "investors": 904,
        "sector_display": "Biopharmaceuticals",
        "usd": 218359905807
      },
      {
        "slug": "fintech-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 155,
        "family": "investors",
        "h1": "FinTech investors in Delhi",
        "investors": 1766,
        "sector_display": "FinTech",
        "usd": 7993196584
      },
      {
        "slug": "alternative-lending-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 122,
        "family": "investors",
        "h1": "Alternative Lending investors in Mumbai",
        "investors": 2227,
        "sector_display": "Alternative Lending",
        "usd": 32600072962
      },
      {
        "slug": "ai-infrastructure-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 250,
        "family": "investors",
        "h1": "AI Infrastructure investors in San Francisco",
        "investors": 1079,
        "sector_display": "AI Infrastructure",
        "usd": 1871108310994
      },
      {
        "slug": "energy-tech-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 132,
        "family": "investors",
        "h1": "Energy Tech investors in Bengaluru",
        "investors": 2000,
        "sector_display": "Energy Tech",
        "usd": 22255776411
      },
      {
        "slug": "healthcare-it-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 272,
        "family": "investors",
        "h1": "Healthcare IT investors in San Francisco",
        "investors": 969,
        "sector_display": "Healthcare IT",
        "usd": 54175062315
      }
    ],
    "top_angel_lists": [
      {
        "slug": "b2c-e-commerce-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 407,
        "family": "angel_investors",
        "h1": "B2C E-Commerce angel investors in Bengaluru",
        "investors": 4750,
        "sector_display": "B2C E-Commerce",
        "usd": 50146513809
      },
      {
        "slug": "retail-tech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 365,
        "family": "angel_investors",
        "h1": "Retail Tech angel investors in Bengaluru",
        "investors": 4438,
        "sector_display": "Retail Tech",
        "usd": 37764196690
      },
      {
        "slug": "fintech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 324,
        "family": "angel_investors",
        "h1": "FinTech angel investors in Bengaluru",
        "investors": 3876,
        "sector_display": "FinTech",
        "usd": 25225350661
      },
      {
        "slug": "b2c-e-commerce-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 289,
        "family": "angel_investors",
        "h1": "B2C E-Commerce angel investors in Mumbai",
        "investors": 3716,
        "sector_display": "B2C E-Commerce",
        "usd": 23641862308
      },
      {
        "slug": "fintech-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 279,
        "family": "angel_investors",
        "h1": "FinTech angel investors in Mumbai",
        "investors": 3612,
        "sector_display": "FinTech",
        "usd": 19361551353
      },
      {
        "slug": "retail-tech-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 243,
        "family": "angel_investors",
        "h1": "Retail Tech angel investors in Mumbai",
        "investors": 3483,
        "sector_display": "Retail Tech",
        "usd": 19995226550
      },
      {
        "slug": "healthtech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 222,
        "family": "angel_investors",
        "h1": "HealthTech angel investors in Bengaluru",
        "investors": 2746,
        "sector_display": "HealthTech",
        "usd": 7121750432
      },
      {
        "slug": "b2c-e-commerce-angel-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 223,
        "family": "angel_investors",
        "h1": "B2C E-Commerce angel investors in Gurugram",
        "investors": 2485,
        "sector_display": "B2C E-Commerce",
        "usd": 12942473180
      },
      {
        "slug": "b2c-e-commerce-angel-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 222,
        "family": "angel_investors",
        "h1": "B2C E-Commerce angel investors in Delhi",
        "investors": 2489,
        "sector_display": "B2C E-Commerce",
        "usd": 4593685854
      },
      {
        "slug": "fintech-angel-investors-in-london",
        "city_display": "London",
        "companies": 349,
        "family": "angel_investors",
        "h1": "FinTech angel investors in London",
        "investors": 1327,
        "sector_display": "FinTech",
        "usd": 12944946775
      },
      {
        "slug": "edtech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 187,
        "family": "angel_investors",
        "h1": "EdTech angel investors in Bengaluru",
        "investors": 2238,
        "sector_display": "EdTech",
        "usd": 8003609069
      },
      {
        "slug": "retail-tech-angel-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 190,
        "family": "angel_investors",
        "h1": "Retail Tech angel investors in Gurugram",
        "investors": 2202,
        "sector_display": "Retail Tech",
        "usd": 11963405297
      },
      {
        "slug": "retail-tech-angel-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 188,
        "family": "angel_investors",
        "h1": "Retail Tech angel investors in Delhi",
        "investors": 1873,
        "sector_display": "Retail Tech",
        "usd": 3710389921
      },
      {
        "slug": "food-tech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 149,
        "family": "angel_investors",
        "h1": "Food Tech angel investors in Bengaluru",
        "investors": 2276,
        "sector_display": "Food Tech",
        "usd": 26116535337
      },
      {
        "slug": "auto-tech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 146,
        "family": "angel_investors",
        "h1": "Auto Tech angel investors in Bengaluru",
        "investors": 2262,
        "sector_display": "Auto Tech",
        "usd": 14086234728
      },
      {
        "slug": "internet-first-brands-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 146,
        "family": "angel_investors",
        "h1": "Internet First Brands angel investors in Bengaluru",
        "investors": 1973,
        "sector_display": "Internet First Brands",
        "usd": 6929399797
      },
      {
        "slug": "fintech-angel-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 313,
        "family": "angel_investors",
        "h1": "FinTech angel investors in San Francisco",
        "investors": 918,
        "sector_display": "FinTech",
        "usd": 21091068388
      },
      {
        "slug": "internet-first-brands-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 148,
        "family": "angel_investors",
        "h1": "Internet First Brands angel investors in Mumbai",
        "investors": 1868,
        "sector_display": "Internet First Brands",
        "usd": 3826410936
      },
      {
        "slug": "artificial-intelligence-angel-investors-in-san-francisco",
        "city_display": "San Francisco",
        "companies": 249,
        "family": "angel_investors",
        "h1": "Artificial Intelligence angel investors in San Francisco",
        "investors": 824,
        "sector_display": "Artificial Intelligence",
        "usd": 33599100526
      },
      {
        "slug": "commerce-enablers-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 112,
        "family": "angel_investors",
        "h1": "Commerce Enablers angel investors in Bengaluru",
        "investors": 1810,
        "sector_display": "Commerce Enablers",
        "usd": 11651568834
      },
      {
        "slug": "fintech-angel-investors-in-new-york-city",
        "city_display": "New York City",
        "companies": 236,
        "family": "angel_investors",
        "h1": "FinTech angel investors in New York City",
        "investors": 706,
        "sector_display": "FinTech",
        "usd": 15946208418
      },
      {
        "slug": "nbfc-lenders-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 96,
        "family": "angel_investors",
        "h1": "NBFC Lenders angel investors in Mumbai",
        "investors": 1652,
        "sector_display": "NBFC Lenders",
        "usd": 16054662061
      },
      {
        "slug": "online-grocery-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 98,
        "family": "angel_investors",
        "h1": "Online Grocery angel investors in Bengaluru",
        "investors": 1579,
        "sector_display": "Online Grocery",
        "usd": 24550466136
      },
      {
        "slug": "fintech-angel-investors-in-gurugram",
        "city_display": "Gurugram",
        "companies": 118,
        "family": "angel_investors",
        "h1": "FinTech angel investors in Gurugram",
        "investors": 1291,
        "sector_display": "FinTech",
        "usd": 5813928023
      },
      {
        "slug": "hrtech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 116,
        "family": "angel_investors",
        "h1": "HRTech angel investors in Bengaluru",
        "investors": 1284,
        "sector_display": "HRTech",
        "usd": 1690590145
      },
      {
        "slug": "artificial-intelligence-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 117,
        "family": "angel_investors",
        "h1": "Artificial Intelligence angel investors in Bengaluru",
        "investors": 1217,
        "sector_display": "Artificial Intelligence",
        "usd": 3110331463
      },
      {
        "slug": "edtech-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 90,
        "family": "angel_investors",
        "h1": "EdTech angel investors in Mumbai",
        "investors": 1568,
        "sector_display": "EdTech",
        "usd": 4476417084
      },
      {
        "slug": "alternative-lending-angel-investors-in-mumbai",
        "city_display": "Mumbai",
        "companies": 88,
        "family": "angel_investors",
        "h1": "Alternative Lending angel investors in Mumbai",
        "investors": 1538,
        "sector_display": "Alternative Lending",
        "usd": 13192296630
      },
      {
        "slug": "investment-tech-angel-investors-in-bengaluru",
        "city_display": "Bengaluru",
        "companies": 93,
        "family": "angel_investors",
        "h1": "Investment Tech angel investors in Bengaluru",
        "investors": 1403,
        "sector_display": "Investment Tech",
        "usd": 13774281502
      },
      {
        "slug": "fintech-angel-investors-in-delhi",
        "city_display": "Delhi",
        "companies": 109,
        "family": "angel_investors",
        "h1": "FinTech angel investors in Delhi",
        "investors": 1191,
        "sector_display": "FinTech",
        "usd": 1951360917
      }
    ],
    "top_profiles": [
      {
        "slug": "anupam-mittal",
        "family": "investor",
        "h1": "Anupam Mittal",
        "usd": 263435545
      },
      {
        "slug": "kunal-bahl",
        "family": "investor",
        "h1": "Kunal Bahl",
        "usd": 1395040786
      },
      {
        "slug": "kunal-naresh-shah",
        "family": "investor",
        "h1": "Kunal Naresh Shah",
        "usd": 1951733143
      },
      {
        "slug": "rohit-bansal",
        "family": "investor",
        "h1": "Rohit Bansal",
        "usd": 1311629568
      },
      {
        "slug": "aman-gupta",
        "family": "investor",
        "h1": "Aman Gupta",
        "usd": 458683351
      },
      {
        "slug": "gokul-rajaram",
        "family": "investor",
        "h1": "Gokul Rajaram",
        "usd": 3271140407
      },
      {
        "slug": "abhishek-goyal",
        "family": "investor",
        "h1": "Abhishek Goyal",
        "usd": 447851368
      },
      {
        "slug": "raman-roy",
        "family": "investor",
        "h1": "Raman Roy",
        "usd": 150035129
      },
      {
        "slug": "naval-ravikant",
        "family": "investor",
        "h1": "Naval Ravikant",
        "usd": 1961532238
      },
      {
        "slug": "elad-gil",
        "family": "investor",
        "h1": "Elad Gil",
        "usd": 15667384549
      },
      {
        "slug": "ramakant-sharma",
        "family": "investor",
        "h1": "Ramakant Sharma",
        "usd": 1055720428
      },
      {
        "slug": "mark-cuban",
        "family": "investor",
        "h1": "Mark Cuban",
        "usd": 3550351615
      },
      {
        "slug": "namita-thapar",
        "family": "investor",
        "h1": "Namita Thapar",
        "usd": 42103347
      },
      {
        "slug": "paul-buchheit",
        "family": "investor",
        "h1": "Paul Buchheit",
        "usd": 793747950
      },
      {
        "slug": "rajan-anandan",
        "family": "investor",
        "h1": "Rajan Anandan",
        "usd": 229671396
      },
      {
        "slug": "anand-ladsariya",
        "family": "investor",
        "h1": "Anand Ladsariya",
        "usd": 126435129
      },
      {
        "slug": "scott-belsky",
        "family": "investor",
        "h1": "Scott Belsky",
        "usd": 1783855422
      },
      {
        "slug": "peyush-bansal",
        "family": "investor",
        "h1": "Peyush Bansal",
        "usd": 324290318
      },
      {
        "slug": "ashish-gupta",
        "family": "investor",
        "h1": "Ashish Gupta",
        "usd": 661728955
      },
      {
        "slug": "sandeep-nailwal",
        "family": "investor",
        "h1": "Sandeep Nailwal",
        "usd": 700537151
      },
      {
        "slug": "marc-benioff",
        "family": "investor",
        "h1": "Marc Benioff",
        "usd": 3294202935
      },
      {
        "slug": "fabrice-grinda",
        "family": "investor",
        "h1": "Fabrice Grinda",
        "usd": 506543597
      },
      {
        "slug": "vineeta-tejpal-singh",
        "family": "investor",
        "h1": "Vineeta Tejpal Singh",
        "usd": 20690111
      },
      {
        "slug": "peter-thiel",
        "family": "investor",
        "h1": "Peter Thiel",
        "usd": 6286852880
      },
      {
        "slug": "balaji-srinivasan",
        "family": "investor",
        "h1": "Balaji Srinivasan",
        "usd": 1054204977
      },
      {
        "slug": "lachy-groom",
        "family": "investor",
        "h1": "Lachy Groom",
        "usd": 4150028542
      },
      {
        "slug": "sujeet-kumar",
        "family": "investor",
        "h1": "Sujeet Kumar",
        "usd": 749887659
      },
      {
        "slug": "nitin-agarwal",
        "family": "investor",
        "h1": "Nitin Agarwal",
        "usd": 76380962
      },
      {
        "slug": "charlie-songhurst",
        "family": "investor",
        "h1": "Charlie Songhurst",
        "usd": 499369841
      },
      {
        "slug": "kishore-kumar-ganji",
        "family": "investor",
        "h1": "Kishore Kumar Ganji",
        "usd": 62931798
      },
      {
        "slug": "binny-bansal",
        "family": "investor",
        "h1": "Binny Bansal",
        "usd": 1104824343
      },
      {
        "slug": "alexis-ohanian-s",
        "family": "investor",
        "h1": "Alexis Ohanian S",
        "usd": 1299151731
      },
      {
        "slug": "vikas-kuthiala",
        "family": "investor",
        "h1": "Vikas Kuthiala",
        "usd": 64185751
      },
      {
        "slug": "rajesh-sawhney",
        "family": "investor",
        "h1": "Rajesh Sawhney",
        "usd": 92731018
      },
      {
        "slug": "uday-chatterjee",
        "family": "investor",
        "h1": "Uday Chatterjee",
        "usd": 133965098
      },
      {
        "slug": "xavier-niel",
        "family": "investor",
        "h1": "Xavier Niel",
        "usd": 2787089935
      },
      {
        "slug": "nitin-singhal",
        "family": "investor",
        "h1": "Nitin Singhal",
        "usd": 57456051
      },
      {
        "slug": "jitendra-gupta",
        "family": "investor",
        "h1": "Jitendra Gupta",
        "usd": 430377958
      },
      {
        "slug": "nat-friedman",
        "family": "investor",
        "h1": "Nat Friedman",
        "usd": 4519156679
      },
      {
        "slug": "dylan-field",
        "family": "investor",
        "h1": "Dylan Field",
        "usd": 1713239529
      }
    ],
    "cities": [
      {
        "name": "San Francisco",
        "pages": 619,
        "investors": 3476
      },
      {
        "name": "London",
        "pages": 448,
        "investors": 3878
      },
      {
        "name": "New York City",
        "pages": 427,
        "investors": 3425
      },
      {
        "name": "Bengaluru",
        "pages": 396,
        "investors": 6413
      },
      {
        "name": "Mumbai",
        "pages": 229,
        "investors": 5086
      },
      {
        "name": "Singapore",
        "pages": 204,
        "investors": 2231
      },
      {
        "name": "Paris",
        "pages": 201,
        "investors": 896
      },
      {
        "name": "Berlin",
        "pages": 175,
        "investors": 729
      },
      {
        "name": "Gurugram",
        "pages": 151,
        "investors": 3610
      },
      {
        "name": "Beijing",
        "pages": 151,
        "investors": 560
      },
      {
        "name": "Delhi",
        "pages": 149,
        "investors": 3416
      },
      {
        "name": "Austin",
        "pages": 136,
        "investors": 711
      },
      {
        "name": "Boston",
        "pages": 135,
        "investors": 947
      },
      {
        "name": "Los Angeles",
        "pages": 133,
        "investors": 989
      },
      {
        "name": "Seoul",
        "pages": 125,
        "investors": 347
      },
      {
        "name": "Tel Aviv",
        "pages": 117,
        "investors": 531
      },
      {
        "name": "Toronto",
        "pages": 113,
        "investors": 810
      },
      {
        "name": "Palo Alto",
        "pages": 112,
        "investors": 737
      },
      {
        "name": "Seattle",
        "pages": 103,
        "investors": 475
      },
      {
        "name": "Shanghai",
        "pages": 101,
        "investors": 617
      },
      {
        "name": "Hyderabad",
        "pages": 98,
        "investors": 823
      },
      {
        "name": "Cambridge",
        "pages": 94,
        "investors": 1421
      },
      {
        "name": "Stockholm",
        "pages": 84,
        "investors": 423
      },
      {
        "name": "Chicago",
        "pages": 78,
        "investors": 554
      },
      {
        "name": "Shenzhen",
        "pages": 77,
        "investors": 357
      },
      {
        "name": "Pune",
        "pages": 69,
        "investors": 897
      },
      {
        "name": "Sydney",
        "pages": 68,
        "investors": 568
      },
      {
        "name": "Amsterdam",
        "pages": 68,
        "investors": 365
      },
      {
        "name": "San Diego",
        "pages": 67,
        "investors": 1050
      },
      {
        "name": "Mountain View",
        "pages": 66,
        "investors": 362
      },
      {
        "name": "Noida",
        "pages": 65,
        "investors": 727
      },
      {
        "name": "Sao Paulo",
        "pages": 62,
        "investors": 534
      },
      {
        "name": "Chennai",
        "pages": 60,
        "investors": 1030
      },
      {
        "name": "Barcelona",
        "pages": 59,
        "investors": 277
      },
      {
        "name": "Tokyo",
        "pages": 57,
        "investors": 180
      },
      {
        "name": "Dubai",
        "pages": 53,
        "investors": 563
      },
      {
        "name": "Munich",
        "pages": 52,
        "investors": 221
      },
      {
        "name": "Jakarta",
        "pages": 51,
        "investors": 497
      },
      {
        "name": "San Jose",
        "pages": 50,
        "investors": 382
      },
      {
        "name": "Hangzhou",
        "pages": 45,
        "investors": 275
      }
    ],
    "sectors": [
      {
        "name": "Life Sciences",
        "pages": 227,
        "investors": 1650
      },
      {
        "name": "FinTech",
        "pages": 184,
        "investors": 5456
      },
      {
        "name": "HealthTech",
        "pages": 164,
        "investors": 3563
      },
      {
        "name": "B2C E-Commerce",
        "pages": 119,
        "investors": 6413
      },
      {
        "name": "Biopharmaceuticals",
        "pages": 97,
        "investors": 904
      },
      {
        "name": "Artificial Intelligence",
        "pages": 95,
        "investors": 2608
      },
      {
        "name": "Healthcare IT",
        "pages": 92,
        "investors": 1162
      },
      {
        "name": "Medical Devices",
        "pages": 90,
        "investors": 545
      },
      {
        "name": "MarketingTech",
        "pages": 80,
        "investors": 1461
      },
      {
        "name": "HRTech",
        "pages": 80,
        "investors": 1767
      },
      {
        "name": "Commerce Enablers",
        "pages": 77,
        "investors": 2536
      },
      {
        "name": "Cybersecurity",
        "pages": 74,
        "investors": 1154
      },
      {
        "name": "Future of Work",
        "pages": 67,
        "investors": 1466
      },
      {
        "name": "Investment Tech",
        "pages": 62,
        "investors": 1908
      },
      {
        "name": "Blockchain in Financial Services",
        "pages": 57,
        "investors": 1319
      },
      {
        "name": "Industry 4.0",
        "pages": 57,
        "investors": 1134
      },
      {
        "name": "HealthTech SaaS",
        "pages": 56,
        "investors": 578
      },
      {
        "name": "Web 3.0",
        "pages": 55,
        "investors": 1355
      },
      {
        "name": "Payments",
        "pages": 55,
        "investors": 1028
      },
      {
        "name": "CFO Stack",
        "pages": 55,
        "investors": 995
      },
      {
        "name": "Logistics Tech",
        "pages": 54,
        "investors": 1646
      },
      {
        "name": "AgriTech",
        "pages": 51,
        "investors": 1305
      },
      {
        "name": "Oncology",
        "pages": 51,
        "investors": 644
      },
      {
        "name": "EdTech",
        "pages": 51,
        "investors": 2951
      },
      {
        "name": "Banking Tech",
        "pages": 49,
        "investors": 845
      },
      {
        "name": "Food Tech",
        "pages": 47,
        "investors": 3142
      },
      {
        "name": "Finance & Accounting Tech",
        "pages": 47,
        "investors": 839
      },
      {
        "name": "Alternative Lending",
        "pages": 46,
        "investors": 2227
      },
      {
        "name": "B2B AgriTech",
        "pages": 46,
        "investors": 982
      },
      {
        "name": "E-Commerce Enablers",
        "pages": 45,
        "investors": 1544
      },
      {
        "name": "Cryptocurrencies",
        "pages": 44,
        "investors": 1008
      },
      {
        "name": "Internet First Brands",
        "pages": 43,
        "investors": 2637
      },
      {
        "name": "NBFC Lenders",
        "pages": 42,
        "investors": 2429
      },
      {
        "name": "Decentralized Finance",
        "pages": 41,
        "investors": 1011
      },
      {
        "name": "Spatial Computing",
        "pages": 41,
        "investors": 625
      },
      {
        "name": "Crop Tech",
        "pages": 40,
        "investors": 1039
      },
      {
        "name": "IT Services",
        "pages": 39,
        "investors": 399
      },
      {
        "name": "Gig Employers",
        "pages": 39,
        "investors": 1539
      },
      {
        "name": "GRC Software",
        "pages": 39,
        "investors": 487
      },
      {
        "name": "Chronic Disease Management",
        "pages": 38,
        "investors": 856
      }
    ]
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-20T04:59:07.175811+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-20T04:58:42.493744+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/investor_directory.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

The live directory supplied anupam-mittal as a profile slug. That returned identifier was used for the separate successful investor-page capture. The source also returned counts for investor lists, angel lists and profiles; those categories should not be summed into a unique-investor estimate.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.counts` | Published-page counts by source category, not necessarily unique investor entities. |
| `data.top_profiles[].slug` | The identifier to use in the investor-page request. |
| `data.top_lists / top_angel_lists` | Published list references when available. |
| `data.cities / sectors` | Navigation categories with source counts that can overlap. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Request the directory with an empty JSON body, select a returned slug and pass it to get_investor_page. Keep the record's family or kind so your application can distinguish an investor profile from a curated list. Do not construct slugs by lowercasing a display name.

Directory metadata may be available even when the detailed roster behind a published page has another access gate. Do not imply that every directory entry includes an unrestricted investor dataset.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/investor-data-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
