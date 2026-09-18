import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
import statsmodels.stats.api as sms


# Step 1: Load the synthetic A/B test data CSV file
# Step 1: Load the synthetic A/B test data CSV file using the correct folder path
df = pd.read_csv('data-py-to-csv/ab_test_data.csv')

# Step 2: Group the data by Variant (A or B) to get totals
# Ensure 'Var' matches the exact capitalization of your CSV column header
summary_table = df.groupby('Var').agg(
    total_users=('user_exposed', 'sum'),
    total_conversions=('conversions', 'sum')
).reset_index()


print("--- Summary Table ---")
print(summary_table)
print("\n")

# Step 3: Extract the numbers into simple lists for our math functions
# 'conversions' becomes our success count, 'nobs' becomes our total sample size
conversions = summary_table['total_conversions'].values
nobs = summary_table['total_users'].values

# Step 4: Calculate actual conversion rates percentage
control_rate = conversions[0] / nobs[0]
variant_rate = conversions[1] / nobs[1]

print("Control (Variant A) Conversion Rate:", control_rate)
print("Variant (Variant B) Conversion Rate:", variant_rate)
print("\n")

# Step 5: Run the Two-Proportion Z-Test
# This tests if the difference between A and B is statistically real or just random luck
z_statistic, p_value = proportions_ztest(conversions, nobs)

print("--- Z-Test Results ---")
print("Z-Statistic:", z_statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Verdict: The difference is statistically significant!")
else:
    print("Verdict: The difference is NOT statistically significant (could be random chance).")
print("\n")

# Step 6: Calculate Confidence Intervals (95% range)
# proportion_confint returns lower and upper bounds for each variant
lower_bounds, upper_bounds = proportion_confint(conversions, nobs, alpha=0.05)

print("--- 95% Confidence Intervals ---")
print("Control Lower Bound:", lower_bounds[0])
print("Control Upper Bound:", upper_bounds[0])
print("Variant Lower Bound:", lower_bounds[1])
print("Variant Upper Bound:", upper_bounds[1])
print("\n")

# Step 7: Statistical Power Analysis
# This checks if our sample size was large enough to trust the test result
effect_size = sms.proportion_effectsize(control_rate, variant_rate)
statistical_power = sms.NormalIndPower().solve_power(
    effect_size=effect_size, 
    nobs1=nobs[0], 
    alpha=0.05, 
    ratio=nobs[1]/nobs[0]
)

print("--- Power Analysis ---")
print("Calculated Power:", statistical_power)

if statistical_power >= 0.80:
    print("Power Verdict: The test was adequately powered (>= 80%).")
else:
    print("Power Verdict: The test was underpowered (< 80%). Sample size was too small.")