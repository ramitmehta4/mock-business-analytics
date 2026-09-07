# Data Generation Module & Synthetic Data Policy

**Data Note:** All data used in this project is 100% synthetically generated via Python. It contains zero real client data, proprietary metrics, screenshots, or brand identifiers from external companies.

**Business Context**
The synthetic datasets emulate a fictional D2C women's ethnic apparel brand. The distributions, session behaviors, and funnel drop-off patterns are informed by realistic performance marketing metrics (simulating traffic from Meta ads and standard Adobe/Google Analytics funnel stages) but are entirely generated through code.

**Generation Scripts & Logic**
The following tables were built using Python (Pandas, NumPy) with fixed random seeds to ensure total reproducibility:

*   **`USER_TABLE.py`:** Generates a user base with a realistic 80/20 split of new vs. returning visitors and assigns acquisition channels.
*   **`Sessions_table.py`:** Simulates mobile-majority traffic and assigns funnel entry/exit stages as ordered categoricals.
*   **`Funnel_event.py`:** Creates monotonically decreasing counts per funnel stage (Landing → PLP → PDP → Cart → Checkout) to emulate real-world drop-off.
*   **`Orders_table.py`:** Generates completed transactions using a lognormal AOV distribution and plausible discount-usage rates.
*   **`Cart_abdn.py`:** Randomly assigns abandonment reasons (e.g., size/fit doubt, shipping costs) weighted heavily toward typical e-commerce friction points.
*   **`ab_test.py`:** Outputs a dataset for two design variants with a deliberately close, non-obvious conversion split for later statistical auditing.
*   **`review.py`:** Generates synthetic VOC-style text covering motivation, value, and anxiety themes for NLP clustering.

**Execution**
Execute these scripts sequentially in the terminal to generate the raw CSV snapshots required for the subsequent SQL and Python epics.
