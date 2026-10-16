# Radar API use cases: 200 worked examples

[README](../../README.md) · [Keyword research](../research/KEYWORD_RESEARCH.md) · [Getting started](../GETTING_STARTED.md) · [Tested scenarios](../scenarios/README.md)

Each page answers one real search query with saved responses from the live Radar API and the
exact CLI, curl, Python and MCP calls. Topics were chosen by [keyword research](../research/KEYWORD_RESEARCH.md)
(India and US monthly searches) and kept only when the API returned populated results.

| Segment | Pages | Highest-demand pages |
| --- | ---: | --- |
| [Financial news research](financial-news/README.md) | 50 | [Stock Market News](financial-news/stock-market-news.md), [Crypto News](financial-news/crypto-news.md), [GST News](financial-news/gst-news.md) |
| [Company financials research](company-financials/README.md) | 50 | [Openai Revenue](company-financials/openai-revenue.md), [Anthropic Revenue](company-financials/anthropic-revenue.md), [Zoho Revenue](company-financials/zoho-revenue.md) |
| [Companies by industry](industry-companies/README.md) | 50 | [Automotive Companies in India](industry-companies/automotive-companies-in-india.md), [AI Companies in India](industry-companies/ai-companies-in-india.md), [Digital Marketing Companies in India](industry-companies/digital-marketing-companies-in-india.md) |
| [Founders and leadership research](founders-leadership/README.md) | 50 | [Anthropic CEO](founders-leadership/anthropic-ceo.md), [Zomato Founder](founders-leadership/zomato-founder.md), [Openai CEO](founders-leadership/openai-ceo.md) |

Captured 16 Oct 2026 from https://radar-api.fliarbi.com. News counts are lower bounds while part
of the news index is offline; company, financial and people data are unaffected.

Regenerate: `scripts/plan_use_cases.py` → `scripts/capture_scenarios.py` → `scripts/build_use_case_pages.py`.
