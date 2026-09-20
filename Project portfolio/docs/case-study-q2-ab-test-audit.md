# Q2 — A/B Test Statistical Re-Audit

## Situation
A redesigned checkout variant (B) was tested against the existing control (A) over a
91-day window (Apr 1 – Jun 30, 2025), with daily traffic split roughly evenly between
the two. Variant B was expected to outperform Control based on pre-launch design
intuition, but the raw numbers showed the opposite.

## Question
Was the observed difference between Control and Variant statistically significant,
was the test adequately powered, and what's the confidence interval on the effect?

## Method
- Aggregated daily `user_exposed` / `conversions` by variant (`Q2.py`).
- Ran a two-proportion z-test (`statsmodels.stats.proportion.proportions_ztest`) to
  test whether the conversion-rate difference is real or noise.
- Computed 95% confidence intervals for each variant's conversion rate.
- Ran a post-hoc power analysis (`NormalIndPower`) to check whether the sample size
  was even large enough to detect an effect of this size.

## Finding
| Metric | Control (A) | Variant (B) |
|---|---|---|
| Users exposed | 102,712 | 103,511 |
| Conversions | 3,248 | 3,165 |
| Conversion rate | 3.162% | 3.058% |
| 95% CI | [3.055%, 3.269%] | [2.953%, 3.163%] |

- **Z-statistic: 1.368, p-value: 0.171** — the difference is **not statistically
  significant** at the conventional 5% threshold. We cannot conclude Variant B
  actually underperforms Control; the gap is plausibly noise.
- **Observed effect size (Cohen's h): 0.006** — this is a very small effect.
- **Statistical power: 27.7%** — the test was **badly underpowered** to detect an
  effect this small. A properly powered test (80% power) at this effect size would
  need several times the current sample.

## Recommendation
Do **not** ship or kill Variant B based on this data — the confidence intervals for A
and B overlap substantially, and the test lacked the power to distinguish a real
effect from chance. Before making a launch decision, either (a) run the test longer
to accumulate the sample size a proper power analysis calls for, or (b) accept that
this effect size (if real) is too small to matter commercially and redirect testing
effort to a change with a larger expected lift.

## Estimated Impact
Shipping Variant B on the current evidence risks a false-negative decision — killing
a redesign that costs nothing in conversion rate (95% CIs overlap) while losing
whatever UX/maintenance benefits motivated the redesign in the first place. The real
cost here isn't the ~3% relative gap; it's the **27.7% power**, which means this test
answered "we don't know yet," not "B loses."

*(Figures are computed from the actual generated dataset — reproducible by re-running
`ab_test.py` and `Q2.py` with the fixed seed.)*
