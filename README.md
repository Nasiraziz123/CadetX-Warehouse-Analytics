# Heavy Supplier, Inventory & Warehouse Analytics

**CadetX Virtual Work Experience | Data Analytics & Data Science**

## Project Overview

This project focuses on analyzing supplier, purchasing, inventory, warehouse, and sales operations using real-world-style supply chain datasets provided for the CadetX Virtual Work Experience program.

The objective is to assess data quality, develop reliable analytical datasets, investigate operational performance, identify business insights, and support data-driven decision-making through the project.

The work is organized into weekly sprints, with documentation and deliverables maintained in GitHub throughout the project.

## Project Objectives

- Understand the structure and relationships of the available datasets.
- Assess data quality, completeness, consistency, and reliability.
- Investigate supplier, purchasing, inventory, warehouse, and sales operations.
- Develop meaningful operational KPIs and analytical insights.
- Identify data issues that could affect business reporting.
- Communicate findings through clear documentation and analytical reports.

## Tools and Technologies

- **Python** — data exploration, profiling, and analysis.
- **Pandas** — tabular data processing, validation, and analytical calculations.
- **Git and GitHub** — version control, project organization, and documentation.

Additional tools will be documented as they are used during subsequent project stages.

## Dataset Overview

The project includes 12 primary datasets covering:

| Area | Datasets |
|---|---|
| Business entities | Customers, branches, products, suppliers |
| Inventory | Inventory master, stock ledger |
| Purchasing | Purchase order headers, purchase order lines |
| Sales | Sales order headers, sales order lines |
| Financial transactions | Invoices, payments |

The raw datasets are maintained locally in the `Data/` directory and excluded from Git where configured by `.gitignore`.

## Project Progress

The project follows a 12-week sprint structure. This section is updated as each sprint is completed.

### Week 1 — Project Setup and Data Understanding

**Status: Completed**

- Established the project repository and initial folder structure.
- Explored the available datasets and their structures.
- Reviewed dataset dimensions, columns, data types, missing values, and duplicate records.
- Began documenting the datasets and initial project findings.

**Documentation:** [Week 1 README](week_1/README.md)

### Week 2 — Data Quality Assessment

**Status: Documentation prepared; final Git validation pending**

The second week focused on assessing the reliability of the 12 primary datasets and documenting issues that could affect downstream analysis.

Key findings included:

- **Missing values:** 2,370 missing purchase-order receipt dates, all associated with cancelled orders.
- **Missing stock-ledger balances:** 180 first-movement records with missing previous and expected balances.
- **Repeated identifiers:** 196 repeated invoice IDs and 201 repeated payment IDs, requiring further investigation.
- **Inventory anomaly:** All 180 inventory records had current stock greater than maximum stock.
- **Stock-ledger checks:** 54,876 records carried the existing mismatch flag. Additional checks examined inbound and outbound balance calculations and sequential balance links.

No unsupported corrections were applied. Ambiguous values and repeated identifiers were retained for investigation rather than changed without evidence.

Working copies were validated against the original row counts and missing-value counts. Corrected CSV exports and a reusable cleaning script were not produced during this stage.

**Documentation:**

- [Week 2 README](week_2/README.md)
- [Week 2 Data Quality Assessment Report](week_2/DOCS/week_2_data_quality_report.md)

### Week 3 — Data Integration and KPI Development

**Status: Completed**

The third week focused on integrating relevant datasets and preparing analytical features and KPIs to support subsequent business analysis.

Key activities included:

- Data integration and relationship development.
- Preparation of analytical datasets.
- Feature engineering.
- Development of relevant operational KPIs.
- Documentation of integration decisions and analytical calculations.

**Documentation:**

- [Week 3 README](week_3/README.md)
- [Week 3 Data Integration Report](week_3/DOCS/week_3_data_integration_report.md)
- [Week 3 Feature Engineering and KPI Report](week_3/DOCS/week_3_feature_engineering_and_kpi_report.md)
- [Week 3 Sprint Notes](week_3/DOCS/week_3_sprint_notes.md)

### Week 4 — Product Analytics

**Status: Completed**

Week 4 focused on evaluating product-level sales performance and historical demand patterns using product and sales datasets.

The analysis was performed using Python and Pandas.

Key activities and findings included:

- Validated the products, sales orders header, and sales orders lines datasets.
- Evaluated all 30 products using quantity sold, revenue, order frequency, and revenue contribution.
- Identified relatively high- and low-performing products based on quantity sold and order frequency.
- Performed ABC / Pareto classification using delivered sales revenue.
- Analyzed monthly demand across 72 months, from January 2019 to December 2024.
- Compared annual demand and year-over-year changes.
- Examined individual product demand patterns across the six-year period.
- Prepared business findings and recommendations.

**Key findings:**

- P015 Engine Block EB-600 recorded the highest product revenue, contributing approximately 21.16% of delivered sales revenue.
- The top two products by revenue contributed approximately 35.92% of total delivered sales revenue.
- ABC Category A contained 10 products and accounted for approximately 81.53% of revenue.
- 2020 recorded the highest annual quantity and revenue.
- 2024 recorded the lowest annual quantity and revenue across the six-year analysis period.
- 21 products experienced more annual decreases than increases in quantity sold, while 9 experienced more annual increases than decreases.

Product movement rankings were treated as relative comparisons. Actual dead-stock identification was not claimed because inventory age and stock-level evidence was not part of this analysis.

**Documentation:**

- [Week 4 README](week_4/README.md)
- [Week 4 Product Analytics Report](week_4/DOCS/week_4_product_analytics_report.md)
- [Week 4 ABC Classification and Demand Trend Analysis Report](week_4/DOCS/week_4_feature_engineering_and_demand_analysis_report.md)
- [Week 4 Sprint Notes](week_4/DOCS/week_4_sprint_notes.md)

### Weeks 5–12 — Upcoming Sprints

The remaining weekly sections will be added as the corresponding tasks are completed. Progress, findings, and deliverables will reflect the work actually performed during each sprint.

## Repository Structure

```text
CadetX_Warehouse_Analytics/
│
├── .gitignore
├── Data/                           # Local raw datasets
│
├── Src/                            # Shared project scripts
│   └── data_profiling.py
│
├── week_1/
│   └── README.md
│
├── week_2/
│   ├── README.md
│   └── DOCS/
│       └── week_2_data_quality_report.md
│
├── week_3/
│   ├── README.md
│   └── DOCS/
│       ├── week_3_data_integration_report.md
│       ├── week_3_feature_engineering_and_kpi_report.md
│       └── week_3_sprint_notes.md
│
├── week_4/
│   ├── README.md
│   └── DOCS/
│       ├── week_4_product_analytics_report.md
│       ├── week_4_feature_engineering_and_demand_analysis_report.md
│       └── week_4_sprint_notes.md
│
└── README.md                       # Main project documentation
```

The structure will evolve as new weekly deliverables are added. The shared `Src/` directory will remain at the project root, and each weekly folder will maintain its own README and supporting documentation.

## Data Handling Principles

- Preserve the original datasets.
- Validate assumptions before correcting questionable values.
- Do not invent missing balances or replacement identifiers without supporting evidence.
- Document unresolved data-quality issues and their potential analytical impact.
- Validate transformations and retain a clear record of analytical decisions.

## Final Deliverables

The repository will progressively contain:

- Weekly project documentation.
- Data profiling and quality assessments.
- Data integration and feature engineering.
- Analytical scripts and calculations.
- Operational KPIs and product performance analysis.
- Business findings and recommendations.
- Final analytical reports and visualizations where appropriate.

The final project summary and conclusions will be expanded as the remaining sprints are completed.

---

**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Program:** CadetX Virtual Work Experience  
**Duration:** 12 weeks