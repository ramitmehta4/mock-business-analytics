import pandas as pd
import numpy as np

# Set a fixed random seed so the data generates exactly the same way every time
np.random.seed(42)

# Simulate realistic e-commerce traffic volume
n_control = 99577
n_variant = 100162

# Set realistic conversion rates (around 3%) where Control slightly beats Variant
# Control (A) = ~3.15% | Variant (B) = ~3.05%
control_conversions = np.random.choice([0, 1], size=n_control, p=[0.9685, 0.0315])
variant_conversions = np.random.choice([0, 1], size=n_variant, p=[0.9695, 0.0305])

# Build the Control dataframe
df_control = pd.DataFrame({
    'Var': ['A'] * n_control,
    'user_exposed': [1] * n_control,
    'conversions': control_conversions
})

# Build the Variant dataframe
df_variant = pd.DataFrame({
    'Var': ['B'] * n_variant,
    'user_exposed': [1] * n_variant,
    'conversions': variant_conversions
})

# Combine and export to your data folder
df_ab_test = pd.concat([df_control, df_variant], ignore_index=True)
df_ab_test.to_csv('data-py-to-csv/ab_test_data.csv', index=False)


print("Realistic A/B test data generated successfully!")
