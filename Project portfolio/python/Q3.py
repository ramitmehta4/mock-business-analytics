import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Cart Abandonment Data
df_cart = pd.read_csv('data-py-to-csv/cart_abandonment_reasons_data.csv')

# 2. Count the frequency of each pre-defined reason
# value_counts() automatically tallies up how many times each reason appears
reason_summary = df_cart['reason_category'].value_counts().reset_index()
reason_summary.columns = ['Abandonment Reason', 'Frequency']

print("--- Top Cart Abandonment Reasons ---")
print(reason_summary)
print("\n")

# 3. Visualize the distribution as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(reason_summary['Abandonment Reason'], reason_summary['Frequency'], color='steelblue')
plt.title('Crescent D2C: Cart Abandonment Reasons Distribution')
plt.xlabel('Reason')
plt.ylabel('Number of Abandoned Sessions')

# Rotate the text labels on the bottom so they don't overlap
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the chart to your folder so you can add it to your portfolio presentation
plt.savefig('cart_abandonment_chart.png')
print("Visualization saved successfully as 'cart_abandonment_chart.png'")