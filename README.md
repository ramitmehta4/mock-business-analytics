# Crescent D2C: E-Commerce CRO & Analytics Case Study
**Author:** Ramit Mahata 

> **Synthetic Data Policy:** All data utilized in this repository is 100% synthetically generated using Python (Faker, NumPy, Pandas) with fixed random seeds. This project contains zero real client data, proprietary metrics, screenshots, or brand identifiers from external companies or previous employers. 

## Project Overview
This repository contains an end-to-end Business Analyst case study for **Crescent D2C**, a fictional e-commerce brand specializing in women's apparel and accessories. Designed to mirror realistic digital marketing and conversion rate optimization (CRO) scenarios, this project moves from raw data generation to actionable insight, concluding with a prioritized backlog and estimated revenue impact.

## Core Business Questions Addressed
This analysis flexes three core analytical muscles—funnel segmentation, statistical rigor, and impact prioritization—to answer the following:

1. **Funnel & Segment Diagnosis:** At which funnel stage (Landing → PLP → PDP → Cart → Checkout) is drop-off highest, and how does this behavior differ between new vs. returning visitors and various traffic sources?
2. **A/B Test Statistical Re-Audit:** Given a recent design variant that intuitively 'should' have won but underperformed the control, was the result statistically significant, adequately powered, and what is the confidence interval on the effect size?
3. **Cart Abandonment Root-Cause & Prioritized Fix Backlog:** What are the dominant friction points causing cart abandonment (e.g., size/fit doubt, shipping costs), how much estimated revenue is lost to each, and in what order should UX fixes be deployed?

## Tool Stack & Methodology
* **Python (`pandas`, `scipy.stats`):** Programmatic synthetic data generation, A/B test significance testing (two-proportion z-test), and frequency clustering for cart abandonment reasons.
* **SQL (SQLite/Postgres):** Advanced querying utilizing CTEs and Window Functions (`LAG`/`LEAD`) to calculate stage-by-stage funnel drop-offs across user cohorts.
* **Excel:** Dynamic ICE/PIE prioritization scoring matrix and a revenue-impact what-if calculator built with live `XLOOKUP`/`INDEX-MATCH` formulas.
* **Tableau:** Interactive final dashboard featuring calculated fields, parameter controls, and segmented visual storytelling.

## Repository Structure
* `/data-generation`: Python scripts (`USER_TABLE.py`, `Sessions_table.py`, etc.) generating the foundational CSV datasets.
* `/sql`: Queries demonstrating cohort splits and retention tracking.
* `/python`: Jupyter Notebooks executing the statistical A/B test audit and clustering.
* `/excel`: The prioritization scoring model and dynamic revenue calculator.
* `/tableau`: Dashboard files and visual assets.
* `/docs`: Detailed write-ups formatted as *Situation → Question → Method → Finding → Recommendation → Estimated Impact*.

---
*For detailed data generation logic and seed constraints, please refer to the `DATA_NOTE.md` file in the `/docs` folder.*
