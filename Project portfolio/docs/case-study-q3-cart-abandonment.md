# Q3 — Cart Abandonment Root-Cause & Prioritized Fix Backlog

## Situation
Of the 1,800 sessions in the dataset, 322 reached Cart or Checkout without completing
a purchase. Each abandoned session was tagged with a self-reported (synthetic)
abandonment reason, but no one had ranked these reasons by frequency or estimated
what fixing the top one is worth.

## Question
What are the dominant friction points causing cart abandonment, how much estimated
revenue is lost to each, and in what order should UX fixes be built?

## Method
- Isolated sessions exiting at Cart or Checkout (`Cart_abdn.py`).
- Tallied abandonment reasons with `value_counts()` (`Q3.py`) and visualized the
  distribution as a bar chart.
- Cross-referenced the average AOV of completed orders (`orders_data.csv`) to convert
  abandonment counts into a rough revenue-at-risk figure for the top reason.

## Finding
| Reason | Sessions | Share |
|---|---|---|
| Size/fit doubt | 146 | 45.3% |
| Shipping cost too high | 77 | 23.9% |
| Just browsing/saved for later | 48 | 14.9% |
| Found better price elsewhere | 23 | 7.1% |
| Payment method declined | 17 | 5.3% |
| Website technical error | 11 | 3.4% |

- **Size/fit doubt is the dominant, addressable reason**, accounting for nearly half
  of all abandoned carts — more than double the next reason (shipping cost).
- The top two reasons (size/fit doubt + shipping cost) together account for **69.2%**
  of all abandonment — a fix backlog targeting just these two addresses the large
  majority of the problem.
- "Website technical error" (3.4%) and "Payment method declined" (5.3%) are real but
  low-volume — worth fixing, but not where the biggest revenue is sitting.

## Recommendation
Prioritize a **size/fit confidence fix** first (e.g., a size guide, fit-predictor
widget, or customer-photo reviews at the PDP/cart stage) — it's the single highest-
leverage fix by volume. Follow with **shipping-cost transparency** (showing shipping
cost earlier in the funnel, before cart) as the second priority. Score both against
Ease/Confidence in the ICE model to sequence the actual build order.

## Estimated Impact
Using the completed-order average AOV of **$66.37**: if a size/fit fix recovers just
**10% of the 146 size/fit-doubt abandons** into completed orders, that's roughly
**15 additional orders**, or approximately **$969 in recovered revenue** over the
same window the abandonment data covers. Scaled to a full year of comparable traffic,
even a modest recovery rate on the top reason represents a non-trivial, low-cost win
relative to acquisition spend.

*(Figures are computed from the actual generated dataset — reproducible by re-running
`Cart_abdn.py`, `Orders_table.py`, and `Q3.py` with the fixed seeds.)*
