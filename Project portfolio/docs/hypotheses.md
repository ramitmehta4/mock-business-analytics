# Problem Statements & Hypotheses

Written before running the analysis for each module — the intent is to state what I
expected to find and why, so the eventual finding can be compared against the
starting hypothesis rather than reverse-engineered after the fact.

## Q1 — Funnel & Segment Diagnosis

**Problem statement:** We don't know which stage of the funnel is losing the most
visitors, or whether new and returning visitors fail at different points.

**Hypothesis:** Given mobile-majority traffic (~79% of sessions) and a multi-step
checkout flow, I expect the **Cart → Checkout** transition to show the highest
drop-off — checkout forms are typically where friction (shipping cost reveal,
account creation, payment entry) is highest. I also expect **returning users to
convert better than new users at every stage**, since they already have trust and
familiarity with the brand.

*(Result: the Cart → Checkout hypothesis held for both segments. The "returning
users convert better everywhere" hypothesis was only partially correct — returning
users actually dropped off more at Landing → Category than new users did.)*

## Q2 — A/B Test Statistical Re-Audit

**Problem statement:** A checkout redesign (Variant B) was expected to outperform
the existing Control based on design intuition, but raw conversion numbers suggest
otherwise. We don't know if that gap is real or noise, or whether the test even had
enough data to tell.

**Hypothesis:** I expect the observed gap to **not be statistically significant**
given how close typical e-commerce conversion-rate differences are (often <0.5
percentage points) relative to the sample sizes typically run in a 90-day window —
and I expect the test to be **underpowered**, since teams rarely run formal power
calculations before launching a test.

*(Result: both parts of the hypothesis held — p = 0.171, not significant; power =
27.7%, confirmed underpowered.)*

## Q3 — Cart Abandonment Root-Cause & Prioritized Fix Backlog

**Problem statement:** We know sessions abandon at Cart/Checkout, but we don't know
which reason dominates or whether the backlog should be built in the order the team
currently assumes.

**Hypothesis:** Based on common e-commerce patterns for apparel specifically, I
expect **size/fit doubt** to be the dominant reason (apparel has no in-person
try-on), followed by **shipping cost** as the second most common friction point —
and I expect these two reasons combined to account for the clear majority of
abandonment, meaning the backlog only needs to prioritize two fixes to address most
of the problem.

*(Result: hypothesis confirmed — size/fit doubt at 45.3%, shipping cost at 23.9%,
combined 69.2% of all abandonment.)*
