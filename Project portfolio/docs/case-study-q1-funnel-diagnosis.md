# Q1 — Funnel & Segment Diagnosis

## Situation
Crescent D2C tracks visitors through a five-stage funnel: Landing → Category (PLP) →
Product (PDP) → Cart → Checkout. Session-level and event-level data exist for 1,800
sessions across 1,000 users (80% new, 20% returning), but no one had broken down
*where* in the funnel drop-off is worst, or whether new and returning visitors behave
differently.

## Question
At which funnel stage is drop-off highest, and does the pattern differ between new
vs. returning visitors?

## Method
- Built `funnel_events` (one row per session per stage reached) and `sessions`/`users`
  tables in SQLite.
- Wrote a CTE + `LAG()` window-function query (`crescent_d2c_Q1a.sql`) to compute
  stage-by-stage traffic volume and drop-off % per segment.
- Wrote a self-join cohort query (`crescent_d2c_Q1b.sql`) to pivot new vs. returning
  volumes side by side for direct comparison.
- Normalized stage-name casing (`LOWER(stage)`) to reconcile inconsistent capitalization
  between the `sessions.exit_page` and `funnel_events.stage` columns.

## Finding
| Stage | New User Volume | New User Drop-off | Returning User Volume | Returning User Drop-off |
|---|---|---|---|---|
| Landing | 1,469 | — | 331 | — |
| Category | 900 | 38.7% | 182 | 45.0% |
| Product | 531 | 41.0% | 104 | 42.9% |
| Cart | 296 | 44.3% | 70 | 32.7% |
| Checkout | 149 | 49.7% | 30 | 57.1% |

- The single biggest new-user drop-off is **Cart → Checkout (49.7%)** — nearly half of
  users who add to cart never reach checkout.
- Returning users drop off *more* at Landing → Category (45.0% vs. 38.7%) but *less*
  at Cart (32.7% vs. 44.3%) — once a returning user reaches cart, they're more
  committed, but checkout is still their worst stage too (57.1%).
- Checkout is the weakest stage for both segments — this is where the funnel bleeds
  the most volume regardless of visitor type.

## Recommendation
Prioritize checkout-stage friction (payment options, guest checkout, shipping-cost
transparency, form length) over top-of-funnel acquisition fixes — the data shows
volume is reaching the bottom of the funnel and failing there, not failing to arrive
in the first place. For returning users specifically, investigate why Landing →
Category loses more of them than new users (possible stale landing-page relevance for
repeat visitors).

## Estimated Impact
Recovering even 10 percentage points of the 49.7% Cart → Checkout new-user drop-off
would move roughly **30 additional new-user sessions** into checkout per the current
296-session Cart cohort — a meaningful lift with no acquisition spend required, since
it's a conversion-path fix rather than a traffic fix.

*(Figures are computed from the actual generated dataset — reproducible by re-running
the `/data-generation` scripts and `/sql` queries with the fixed seeds.)*
