# Company filter catalog API: filters, sort and listing columns

[All endpoints](README.md) · [Workflow guide](../guides/company-search-api.md)

Discover the supported company search inputs, categorical values, typeahead availability, sort choices, pagination bounds and result-column names.

## Route, authentication and credits

**`POST /v1/companies/filters`** · MCP tool **`company_filter_catalog`** · key scope **`companies`**.
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
curl --fail-with-body -X POST "$RADAR_API_URL/v1/companies/filters" \
  -H "Authorization: Bearer $RADAR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{}'
```

MCP clients call the tool with a single `request` argument containing the same body:

<!-- mcp-request: company_filter_catalog -->
```json
{
  "name": "company_filter_catalog",
  "arguments": {
    "request": {}
  }
}
```

The object above is the `params` for `tools/call`, not a complete HTTP handshake.
Use an MCP SDK to initialize the connection; see [transport examples](transports.md).

## Actual captured output

<!-- response-example: company_filter_catalog -->
```json
{
  "ok": true,
  "feature": "company_filter_catalog",
  "data": {
    "filters": [
      {
        "field": "company_names",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Company Names",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "industries",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Industries",
          "type": "array"
        },
        "options": [
          "3D Printing",
          "Accounting & Tax Services",
          "AdTech",
          "Advertising",
          "Aeronautics Aerospace & Defence",
          "Agri-Tech",
          "Agriculture",
          "AI",
          "Airport Operations",
          "Alternative/Renewable Energy",
          "Animation",
          "Application Development",
          "Architecture Interior Design",
          "Art",
          "Augmented Reality (AR) & Virtual Reality (VR)",
          "Automation",
          "Automotive",
          "Aviation & Others",
          "Banking & Financial Services",
          "Beauty & Personal Care",
          "Big Data",
          "Bioinformatics",
          "Biotechnology",
          "BPO",
          "Branding",
          "Building Materials",
          "Business Intelligence",
          "Business Services",
          "Chemicals",
          "Childcare",
          "Clean Technology",
          "Cloud",
          "Coaching",
          "Commercial Printing Services",
          "Commodity Chemicals",
          "Comparison Shopping",
          "Computer Vision",
          "Construction",
          "Construction Materials",
          "Construction Supplies & Fixtures",
          "Consulting",
          "Consumer Services",
          "Coworking Spaces",
          "Crafts",
          "Crowdfunding",
          "Cryptocurrency & Blockchain",
          "CXM",
          "Cyber Security",
          "Cybersecurity",
          "Dairy Farming",
          "Data Analytics",
          "Data Science",
          "Dating Matrimonial",
          "Design",
          "Digital Marketing",
          "Digital Media",
          "Digital Media Publishing",
          "Discovery",
          "Drones and UAVs",
          "E-Commerce & Internet Business",
          "E-Learning",
          "Ed-Tech",
          "Education",
          "Elderly Care Services",
          "Electrical",
          "Electronics",
          "Embedded",
          "Employment Services",
          "Energy",
          "Engineering",
          "Enterprise Mobility",
          "Enterprise Software",
          "Entertainment",
          "Environmental Services & Equipment",
          "ERP",
          "Esports",
          "EV",
          "Events",
          "Experiential Travel",
          "Facility Management",
          "Fashion",
          "FinTech",
          "FinTech Lending",
          "Fisheries",
          "FMCG",
          "Food & Beverages",
          "Food Processing",
          "Food Production",
          "Food Service Contractors",
          "FoodTech",
          "Foreign Exchange",
          "Forestry",
          "Gaming",
          "Gas",
          "Gas & Consumable Fuels",
          "Geospatial",
          "Government & Public Administration",
          "Government Contracting",
          "Green Hydrogen",
          "Handicraft",
          "Health & Wellness",
          "Healthcare & Lifesciences",
          "Home Care",
          "Home Security Solutions",
          "Homebuilding",
          "Horticulture",
          "Hospitality",
          "Hospitality & Tourism",
          "Hotel",
          "House-Hold Services",
          "Housing",
          "Human Resources & Staffing",
          "Indic Language Startups",
          "Industrial Design",
          "Industrial Machinery & Equipment",
          "Infrastructure",
          "Insurance",
          "Integrated Communication Services",
          "Internet of Things",
          "Investment Management & Fund Operators",
          "IT Services",
          "Jewellery",
          "KPO",
          "Laundry",
          "Legal Services",
          "Leisure",
          "Leisure, Hospitality & Tourism",
          "Lifestyle",
          "Location Based",
          "Logistics",
          "Loyalty",
          "Machine Learning",
          "Manufacture of Electrical Equipment",
          "Manufacture of Machinery and Equipment",
          "Manufacturing (General/Industrial)",
          "Maritime (Shipping and Port Management)",
          "Market Research",
          "Marketing",
          "Media & Entertainment",
          "Medical Devices Biomedical",
          "Mental Health Tech",
          "Metaverse",
          "Microbrewery",
          "Microfinance",
          "Music",
          "Nanotechnology",
          "Network Technology Solutions",
          "New-Age Construction Technologies",
          "NGO",
          "NLP",
          "Non-Leather Textiles Goods",
          "Non-Renewable Energy",
          "Non-Profit / Charities",
          "Non-Profit Management",
          "Oil",
          "Oil & Gas Exploration and Production",
          "Oil & Gas Transportation Services",
          "Oil, Gas & Consumable Fuels",
          "Online Marketplaces",
          "OOH Media",
          "Organic Agriculture",
          "Others",
          "Passenger Experience",
          "Passenger Transportation Services",
          "Payment Platforms",
          "Personal Finance",
          "Personal Security",
          "Pet Services",
          "Pets & Animals",
          "Pharmaceuticals",
          "Photography",
          "Physical Toys and Games",
          "Plant-Based Foods",
          "Point of Sales",
          "Product Development",
          "Professional & Commercial Services",
          "Professional Information Services",
          "Project Management",
          "Public Citizen Security Solutions",
          "Public Relations",
          "Publishing",
          "Quantum Computing",
          "Real Estate & Property Management",
          "Recruitment Jobs",
          "RegTech",
          "Renewable Solar Energy",
          "Renewable Wind Energy",
          "Restaurants",
          "Retail",
          "Robotics",
          "Sales",
          "SCM",
          "Security Systems",
          "Semiconductor",
          "Smart Home & IoT",
          "Social",
          "Social Commerce",
          "Social Impact",
          "Social Media",
          "Software",
          "Space Technology & Services",
          "Specialty Chemicals",
          "Specialty Retailers",
          "Sports",
          "Sports Promotion and Networking",
          "Technology Hardware",
          "Telecommunication & Networking",
          "Telecommunications",
          "Testing",
          "Textile",
          "Textiles & Apparel",
          "Ticketing",
          "Tires & Rubber Products",
          "Toys and Games",
          "Trade",
          "Training",
          "Training & Development",
          "Translation & Linguistic Services",
          "Transportation & Storage",
          "Utilities (Electric",
          "Utilities (Electric, Gas, Water)",
          "Venture Capital & Private Equity",
          "Waste Management",
          "Waste Management & Environmental Services",
          "Water",
          "Wearables",
          "Web Design",
          "Web Development",
          "Weddings",
          "Wholesale Trade",
          "Wireless"
        ],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "sectors",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Sectors",
          "type": "array"
        },
        "options": [
          "Enterprise Applications",
          "Enterprise Infrastructure",
          "High Tech",
          "Gig Economy",
          "Consumer",
          "Retail",
          "FinTech",
          "InsurTech",
          "HealthTech",
          "Life Sciences",
          "Energy Tech",
          "Mobile",
          "EdTech",
          "Semiconductors",
          "Travel and Hospitality Tech",
          "Real Estate and Construction Tech",
          "Aerospace, Maritime and Defense Tech",
          "Gaming",
          "Food and Agriculture Tech",
          "Telecom",
          "Auto Tech",
          "Media & Entertainment",
          "Transportation and Logistics Tech",
          "Chemicals and Materials Tech",
          "Conglomerates",
          "Industrial Goods and Manufacturing",
          "Mining",
          "Environment Tech",
          "Blockchain Technology"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "markets",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Markets",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "business_models",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Business Models",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "locations",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Locations",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "sizes",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Sizes",
          "type": "array"
        },
        "options": [
          "Small",
          "Medium-Small",
          "Medium",
          "Medium-Large",
          "Large",
          "Very Large",
          "Giant",
          "Super Giant"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "stages",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Stages",
          "type": "array"
        },
        "options": [
          "Most Recent",
          "Seed",
          "Series A",
          "Series B",
          "Series C",
          "Series D",
          "Series E",
          "Series F",
          "Series G",
          "Series H",
          "Series I",
          "Series J"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "technologies",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Technologies",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "products",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Products",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "skills",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Skills",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "event_types",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Event Types",
          "type": "array"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "financing_status",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Financing Status",
          "type": "array"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "ownership_status",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Ownership Status",
          "type": "array"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "revenue_bands",
        "schema": {
          "items": {
            "enum": [
              "under1m",
              "1m-10m",
              "10m-100m",
              "100m-1b",
              "1b+"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Revenue Bands",
          "type": "array"
        },
        "options": [
          "under1m",
          "1m-10m",
          "10m-100m",
          "100m-1b",
          "1b+"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "revenue_growth",
        "schema": {
          "items": {
            "enum": [
              "declining",
              "flat",
              "growing",
              "high",
              "hyper"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Revenue Growth",
          "type": "array"
        },
        "options": [
          "declining",
          "flat",
          "growing",
          "high",
          "hyper"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "profitability",
        "schema": {
          "items": {
            "enum": [
              "profitable",
              "loss"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Profitability",
          "type": "array"
        },
        "options": [
          "profitable",
          "loss"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "entity_type",
        "schema": {
          "default": "all",
          "enum": [
            "all",
            "investor",
            "incubator"
          ],
          "title": "Entity Type",
          "type": "string"
        },
        "options": [
          "all",
          "investor",
          "incubator"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "revenue_models",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Revenue Models",
          "type": "array"
        },
        "options": [
          "fee-for-service",
          "e-commerce - product",
          "e-commerce - service",
          "physical commerce",
          "advertising",
          "subscription",
          "commission on transaction",
          "donations",
          "sponsorship",
          "affiliate marketing",
          "renting / leasing",
          "lending",
          "freemium",
          "licensing",
          "interest",
          "selling data"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "business_approaches",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Business Approaches",
          "type": "array"
        },
        "options": [
          "traditional",
          "tech-enabled traditional",
          "little innovative",
          "unique & innovative"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "scalability",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Scalability",
          "type": "array"
        },
        "options": [
          "no or less scalability",
          "good scalability",
          "high scalability"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "growth_stages",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Growth Stages",
          "type": "array"
        },
        "options": [
          "Very Early Stage",
          "Early-Stage Scaling",
          "Early Stage with Growth Potential",
          "Stable Company",
          "Matured Company",
          "Consistent Growth",
          "Scaled Good",
          "Established and Scaling",
          "Steady Growth",
          "Scaling Super Fast",
          "Aggressively Scaling",
          "Funding Giant"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "operating_status",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Operating Status",
          "type": "array"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "organization_types",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Organization Types",
          "type": "array"
        },
        "options": [
          "Company",
          "Investor"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "deal_sizes",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Deal Sizes",
          "type": "array"
        },
        "options": [
          "0-10K",
          "10-100K",
          "1M-10M",
          "10M-100M",
          "100M-1B",
          "1B+"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "ages",
        "schema": {
          "items": {
            "enum": [
              "Most Recent",
              "< 5y",
              "5-10y",
              "10-25y",
              "25+y"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Ages",
          "type": "array"
        },
        "options": [
          "Most Recent",
          "< 5y",
          "5-10y",
          "10-25y",
          "25+y"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "founded_year_from",
        "schema": {
          "anyOf": [
            {
              "maximum": 2100,
              "minimum": 1800,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Founded Year From"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "founded_year_to",
        "schema": {
          "anyOf": [
            {
              "maximum": 2100,
              "minimum": 1800,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "title": "Founded Year To"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "positions",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Positions",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "verticals",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Verticals",
          "type": "array"
        },
        "options": [],
        "suggestions_available": true,
        "options_complete": false
      },
      {
        "field": "industrial_applications",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Industrial Applications",
          "type": "array"
        },
        "options": [
          "Internet of Things",
          "Artificial Intelligence",
          "Robotics",
          "AR VR",
          "Blockchain",
          "Big Data",
          "3D Printing",
          "Vertical SaaS",
          "Sustainability Tech"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "founders_background",
        "schema": {
          "items": {
            "enum": [
              "serial_entrepreneur",
              "first_time_founder",
              "founder_with_exit",
              "top_ranked_founder",
              "top_tier_university",
              "elite_alumni",
              "technical_founder",
              "ex_notable_employer",
              "c_level_exec",
              "seasoned_15y"
            ],
            "type": "string"
          },
          "maxItems": 10,
          "title": "Founders Background",
          "type": "array"
        },
        "options": [
          "serial_entrepreneur",
          "first_time_founder",
          "founder_with_exit",
          "top_ranked_founder",
          "top_tier_university",
          "elite_alumni",
          "technical_founder",
          "ex_notable_employer",
          "c_level_exec",
          "seasoned_15y"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "web_popularity",
        "schema": {
          "items": {
            "enum": [
              "high",
              "medium",
              "low"
            ],
            "type": "string"
          },
          "maxItems": 3,
          "title": "Web Popularity",
          "type": "array"
        },
        "options": [
          "high",
          "medium",
          "low"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "web_cwv",
        "schema": {
          "items": {
            "enum": [
              "pass",
              "needs_improvement",
              "poor"
            ],
            "type": "string"
          },
          "maxItems": 3,
          "title": "Web Cwv",
          "type": "array"
        },
        "options": [
          "pass",
          "needs_improvement",
          "poor"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "web_speed",
        "schema": {
          "items": {
            "enum": [
              "fast",
              "average",
              "slow"
            ],
            "type": "string"
          },
          "maxItems": 3,
          "title": "Web Speed",
          "type": "array"
        },
        "options": [
          "fast",
          "average",
          "slow"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "web_seo_maturity",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Web Seo Maturity",
          "type": "array"
        },
        "options": [
          "advanced",
          "good"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "web_sd_maturity",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Web Sd Maturity",
          "type": "array"
        },
        "options": [
          "rich",
          "basic"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "web_business_hints",
        "schema": {
          "items": {
            "maxLength": 200,
            "minLength": 1,
            "type": "string"
          },
          "maxItems": 20,
          "title": "Web Business Hints",
          "type": "array"
        },
        "options": [
          "ecommerce",
          "local_service",
          "saas",
          "content",
          "vertical:restaurant",
          "vertical:hotel",
          "vertical:auto_dealer",
          "vertical:real_estate",
          "vertical:retail"
        ],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "web_score",
        "schema": {
          "items": {
            "enum": [
              "80+",
              "60-80",
              "40-60",
              "<40"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Web Score",
          "type": "array"
        },
        "options": [
          "80+",
          "60-80",
          "40-60",
          "<40"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "mobile_downloads",
        "schema": {
          "items": {
            "enum": [
              "1k+",
              "100k+",
              "1m+",
              "10m+"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Mobile Downloads",
          "type": "array"
        },
        "options": [
          "1k+",
          "100k+",
          "1m+",
          "10m+"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "mobile_growth",
        "schema": {
          "items": {
            "enum": [
              "declining",
              "flat",
              "growing",
              "high",
              "hyper"
            ],
            "type": "string"
          },
          "maxItems": 1,
          "title": "Mobile Growth",
          "type": "array"
        },
        "options": [
          "declining",
          "flat",
          "growing",
          "high",
          "hyper"
        ],
        "suggestions_available": false,
        "options_complete": true
      },
      {
        "field": "hiring",
        "schema": {
          "anyOf": [
            {
              "$ref": "#/$defs/HiringFilter"
            },
            {
              "type": "null"
            }
          ],
          "default": null
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      },
      {
        "field": "radius_km",
        "schema": {
          "anyOf": [
            {
              "maximum": 250,
              "minimum": 21,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Explicit radius expansion around the selected location; source matching tiers apply",
          "title": "Radius Km"
        },
        "options": [],
        "suggestions_available": false,
        "options_complete": false
      }
    ],
    "definitions": {
      "HiringFilter": {
        "additionalProperties": false,
        "properties": {
          "is_hiring": {
            "default": true,
            "title": "Is Hiring",
            "type": "boolean"
          },
          "min_open_roles": {
            "default": 1,
            "maximum": 100000,
            "minimum": 1,
            "title": "Min Open Roles",
            "type": "integer"
          },
          "roles": {
            "items": {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            "maxItems": 20,
            "title": "Roles",
            "type": "array"
          },
          "cities": {
            "items": {
              "maxLength": 200,
              "minLength": 1,
              "type": "string"
            },
            "maxItems": 20,
            "title": "Cities",
            "type": "array"
          },
          "recency_days": {
            "default": 30,
            "maximum": 365,
            "minimum": 1,
            "title": "Recency Days",
            "type": "integer"
          }
        },
        "title": "HiringFilter",
        "type": "object"
      }
    },
    "sort_options": [
      "relevance",
      "valuation",
      "funding",
      "estimated_revenue",
      "financing_rounds",
      "latest_deal",
      "employees",
      "prominence",
      "finance",
      "scalability",
      "momentum",
      "innovation",
      "maturity"
    ],
    "sort_direction": "descending; relevance uses source ranking",
    "columns": [
      "founded_year",
      "employees",
      "total_funding",
      "latest_revenue",
      "valuation",
      "financing_rounds",
      "growth_stage",
      "funding_stage",
      "web_presence",
      "mobile_downloads",
      "mobile_growth",
      "revenue_model",
      "business_model",
      "industry",
      "country",
      "ownership"
    ],
    "page": {
      "first": 0,
      "max": 200,
      "limit_max": 100
    },
    "semantics": "Values generally OR within a filter and AND across filters. Structured search defaults to strict source matching; expanded mode exposes labelled fallback candidates. Inspect access and matching metadata. Band filters accept one value.",
    "column_note": "Selected columns are formatted display values, not precise financial statements. Empty values have unknown coverage; source suppresses zero/negative display values.",
    "contact_note": "Search returns availability only. Request emails or phones separately using an explicit contacts scope and an entitled linked Radar account."
  },
  "window": {
    "data_through": null
  },
  "meta": {
    "retrieved_at": "2026-09-23T03:40:41.770750+00:00",
    "partial": false,
    "notes": [],
    "provider": "Fliar BI"
  }
}
```

This is the captured **complete response**, HTTP **200**, from
**2026-09-23T03:40:41.771056+00:00**. Retained fields have their original values and types,
except explicitly redacted credentials. Hashes use parsed, sorted JSON after any
credential redaction; they are not hashes of HTTP wire bytes.
The [downloadable JSON example](../examples/company_filter_catalog.json) records provenance,
the exact request, omitted paths and a SHA-256 of the original response.
The documentation preserves captured business fields and all array rows. Any
remaining omitted prose is listed explicitly; original counts stay unchanged.

This response is generated from the validated gateway contract and reviewed Radar sidebar vocabulary. It does not query or count every company.

## Read the response

| Field | Meaning and handling |
|---|---|
| `data.filters` | Public field names, validation schemas and known options. |
| `data.sort_options` | Allowed descending sort choices; relevance uses source ranking. |
| `data.columns` | Allowlisted on-demand display columns. |
| `data.page` | Zero-based pagination bounds. |

Every data response includes `ok`, `feature`, `data`, `window` and `meta`.
`meta.retrieved_at` is gateway retrieval time. `window.data_through` describes
source coverage when known and may be null. HTTP 200 and `ok=true` do not imply
`meta.partial=false`, complete history or a current independently verified fact.
An error has `ok=false`, a structured `error.kind` and an explanatory message.

## Build the workflow

Inspect the request schema and returned coverage; use the related discovery response before selecting an identifier or field. Preserve access errors and unknown values in your application.

A successful HTTP response does not independently establish current accuracy or complete coverage. Contact access checks and source plan limits remain authoritative.

For `429`, honor `Retry-After` and reduce concurrent requests. For a source timeout,
use bounded backoff and a narrower query. For `401`/`403`, correct the credential,
scope or entitlement instead of retrying unchanged. A `503 service_unavailable`
requires operator connection setup. Preserve a failed or partial response in your
application state; never overwrite a known value with an invented zero.

Continue with the [workflow guide](../guides/company-search-api.md),
[data quality observations](../DATA_QUALITY.md), [error contract](../USER_GUIDE.md)
and [machine-readable schema](../openapi.json).
