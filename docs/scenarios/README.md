# 50 executed Radar API questions and full response examples

Each page has an exact REST/MCP request, captured output, baseline comparison and
interpretation. These are bounded read-only tests, not a production capacity or
independent data-accuracy benchmark. Requests were fixed before repairs.

Read the [filter analysis](../FILTER_AUDIT.md) and [feedback and results](../SCENARIO_AUDIT.md).
**Observed** means contract and declared checks passed. **Qualified** means an
explicit source, coverage, freshness or completeness limitation remains.
**Failed** means a tested semantic condition was violated. **Unavailable** means
the operation did not successfully return data. None means all source truth was verified.

| Scenario | Business question | HTTP | Assessment |
|---|---|---:|---|
| [01-adtech-vocabulary](01-adtech-vocabulary.md) | Which industry value selects AdTech companies? | 200 | observed |
| [02-usa-vocabulary](02-usa-vocabulary.md) | Which location value selects the United States? | 200 | observed |
| [03-usa-adtech-under-10k](03-usa-adtech-under-10k.md) | Find US AdTech startups founded since 2021 with latest annual revenue below USD 10,000. | 200 | qualified |
| [04-usa-adtech-over-1m](04-usa-adtech-over-1m.md) | Find US AdTech companies with latest annual revenue of at least USD 1 million. | 200 | qualified |
| [05-india-profitable](05-india-profitable.md) | Find profitable Indian software companies with recorded revenue growth. | 200 | qualified |
| [06-under-1m-band](06-under-1m-band.md) | Find US AdTech candidates in Radar’s positive-revenue under-USD-1M band. | 200 | qualified |
| [07-10m-100m-band](07-10m-100m-band.md) | Find Indian software companies in the USD 10M–100M revenue band. | 200 | qualified |
| [08-high-growth](08-high-growth.md) | Find Indian software candidates with recorded 30–100% revenue growth. | 200 | qualified |
| [09-loss-making](09-loss-making.md) | Find Indian payments companies with recorded net losses. | 200 | qualified |
| [10-startup-age](10-startup-age.md) | Find US AdTech companies founded from 2021 through 2026 without assuming a funding stage. | 200 | observed |
| [11-seed-small-round](11-seed-small-round.md) | Find Indian seed-stage software companies with funding rounds in the USD 10K–100K band. | 200 | qualified |
| [12-subscription-model](12-subscription-model.md) | Find US software companies classified with subscription revenue models. | 200 | qualified |
| [13-balance-sheet](13-balance-sheet.md) | Retrieve Microsoft annual assets, liabilities and equity for 2024–2026. | 200 | qualified |
| [14-annual-income](14-annual-income.md) | Retrieve Microsoft’s FY2025 income figures without quarterly mixing. | 200 | qualified |
| [15-annual-cash-flow](15-annual-cash-flow.md) | Retrieve Microsoft annual operating cash flow, capex and free cash flow. | 200 | qualified |
| [16-quarterly-income](16-quarterly-income.md) | Retrieve Microsoft’s three latest accessible quarterly income periods. | 200 | qualified |
| [17-funding-rounds](17-funding-rounds.md) | Retrieve OpenAI funding rounds separately from revenue. | 200 | observed |
| [18-finance-columns](18-finance-columns.md) | Compare available revenue and funding display columns for Razorpay and Stripe. | 200 | observed |
| [19-precise-profit-screen](19-precise-profit-screen.md) | Check whether Microsoft has positive annual profit and revenue above USD 1B in its latest accessible year. | 200 | qualified |
| [20-financial-filter-definitions](20-financial-filter-definitions.md) | Discover exact financial thresholds, growth meanings and screening limits. | 200 | qualified |
| [21-razorpay-founders](21-razorpay-founders.md) | Retrieve Razorpay’s recorded founders with role descriptions. | 200 | qualified |
| [22-stripe-leadership](22-stripe-leadership.md) | Retrieve Stripe’s recorded key people and designations. | 200 | qualified |
| [23-swiggy-leadership](23-swiggy-leadership.md) | Retrieve Swiggy’s recorded key people and their roles. | 200 | qualified |
| [24-microsoft-team](24-microsoft-team.md) | Retrieve professional records with an exact current-company domain of microsoft.com. | 200 | qualified |
| [25-stripe-executives](25-stripe-executives.md) | Find Stripe professionals categorized as executives with exact domain affiliation. | 200 | qualified |
| [26-razorpay-chief](26-razorpay-chief.md) | Find Razorpay key people whose recorded designation contains CEO. | 200 | qualified |
| [27-founder-education](27-founder-education.md) | Find founders who studied at Stanford University. | 200 | qualified |
| [28-professional-skills](28-professional-skills.md) | Find Microsoft-associated professionals with Python skills. | 200 | qualified |
| [29-professional-experience](29-professional-experience.md) | Find Microsoft-associated professionals with at least ten years of experience. | 200 | qualified |
| [30-india-senior-executives](30-india-senior-executives.md) | Find India-based executives whose highest recorded seniority is director or above. | 200 | qualified |
| [31-company-apps](31-company-apps.md) | Which Google Play apps have swiggy.com as the developer website host? | 200 | qualified |
| [32-food-apps](32-food-apps.md) | Find Food & Drink apps with at least one million installs and rating at least four. | 200 | qualified |
| [33-app-growth](33-app-growth.md) | Retrieve Swiggy app growth together with the dated measurements and reliability flag. | 200 | qualified |
| [34-app-history-page](34-app-history-page.md) | Retrieve the second page of Swiggy install observations while retaining source duplicates. | 200 | qualified |
| [35-app-monetization](35-app-monetization.md) | Does Swiggy’s app record show ads, purchases, currency and paid/free status? | 200 | qualified |
| [36-app-ratings](36-app-ratings.md) | Retrieve Swiggy’s rating histogram and review counts. | 200 | qualified |
| [37-us-software-jobs](37-us-software-jobs.md) | Find observed US software engineer job postings. | 200 | observed |
| [38-normalized-interns](38-normalized-interns.md) | Find internship-type records from Shine using the public internship alias. | 200 | observed |
| [39-company-skill-jobs](39-company-skill-jobs.md) | Find Microsoft job listings mentioning Python skills. | 200 | observed |
| [40-salary-benchmark](40-salary-benchmark.md) | Retrieve the USD software-engineer salary benchmark for the US with sample size. | 200 | observed |
| [41-remote-part-time-interns](41-remote-part-time-interns.md) | Find observed remote part-time internships with explicit work-mode evidence. | 200 | qualified |
| [42-internship-employers](42-internship-employers.md) | Which source employers have Business Development internship listings? | 200 | qualified |
| [43-internship-stipend](43-internship-stipend.md) | Find observed internship listings with stipend value at least 10,000, preserving currency and unknown period. | 200 | qualified |
| [44-investor-fintech](44-investor-fintech.md) | Retrieve Anupam Mittal’s recorded FinTech portfolio entries. | 200 | qualified |
| [45-investor-co-backers](45-investor-co-backers.md) | Retrieve Anupam Mittal’s measured co-investor relationships. | 200 | qualified |
| [46-investor-directory](46-investor-directory.md) | Retrieve three investors from the reviewed Bengaluru FinTech directory. | 200 | qualified |
| [47-company-taxonomy](47-company-taxonomy.md) | Retrieve Razorpay sectors, primary feeds and other business classifications. | 200 | observed |
| [48-company-technologies](48-company-technologies.md) | Retrieve Stripe’s observed technologies with their available source structure. | 200 | observed |
| [49-company-traffic](49-company-traffic.md) | Retrieve Swiggy traffic and geography observations. | 200 | observed |
| [50-company-news](50-company-news.md) | Retrieve Microsoft business news for April 2026 and retain dates and source links. | 502 | unavailable |
