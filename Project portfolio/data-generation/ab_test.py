import pandas as pd
import numpy as np

# Set fixed seed for reproducibility
np.random.seed(42)

# Match the timeline from the previous file: April 1, 2025 to June 30, 2025 (91 days)
dates = pd.date_range(start='2025-04-01', end='2025-06-30')

# Realistic e-commerce conversion rates (around 3%)
# Narrative: Control (A) intuitively outperforms the redesign Variant (B)
cr_control = 0.0315  # 3.15% 
cr_variant = 0.0305  # 3.05%

data = []

# Generate daily aggregated traffic instead of millions of individual rows
for date in dates:
    # Simulate ~1000 to ~1250 daily users per variant
    users_a = np.random.randint(1000, 1250)
    users_b = np.random.randint(1000, 1250)
    
    # Use binomial distribution to generate realistic daily conversion fluctuations
    conv_a = np.random.binomial(users_a, cr_control)
    conv_b = np.random.binomial(users_b, cr_variant)
    
    # Format date as YYYY-MM-DD
    date_str = date.strftime('%Y-%m-%d')
    
    # Append daily record for Control (A)
    data.append({
        'Var': 'A', 
        'metric_date': date_str, 
        'user_exposed': users_a, 
        'conversions': conv_a
    })
    
    # Append daily record for Variant (B)
    data.append({
        'Var': 'B', 
        'metric_date': date_str, 
        'user_exposed': users_b, 
        'conversions': conv_b
    })

# Convert to DataFrame
df_ab_test = pd.DataFrame(data)

# Export to your output folder
df_ab_test.to_csv('data-py-to-csv/ab_test_data.csv', index=False)

print("Realistic daily A/B test data generated successfully!")
print(f"Total Date Range: {df_ab_test['metric_date'].min()} to {df_ab_test['metric_date'].max()}")
