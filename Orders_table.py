from BA_PROJECT.USER_TABLE import users_df
from BA_PROJECT.Sessions_table import sessions_df
from BA_PROJECT.Funnel_event import funnel_events_df
import numpy as np
import pandas as pd 

np.random.seed(45)

# Define total orders 
total_orders = 850

# 1. Primary & Foreign Keys
order_id = [f"ORD_{i:05d}" for i in range(1, total_orders + 1)]
order_user_id = np.random.choice(users_df["user_id"], size=total_orders)

# 2. Order Dates within the 2025 timeline
start_ts = pd.to_datetime("2025-01-01").value // 10**9
end_ts = pd.to_datetime("2025-12-31").value // 10**9
random_ts = np.random.randint(start_ts, end_ts, size=total_orders)
order_date = pd.to_datetime(random_ts, unit="s")

# 3. Encoded Logic: Realistic AOV Distribution (Lognormal)
# mean=4.0 and sigma=0.6 creates a right-skewed distribution (median ~$55)
raw_aov = np.random.lognormal(mean=4.0, sigma=0.6, size=total_orders)
aov = np.round(raw_aov, 2)

# 4. Encoded Logic: Plausible discount-usage rate
# 30% of orders use a discount code (1), 70% do not (0)
discount_applied = np.random.choice([0, 1], size=total_orders, p=[0.70, 0.30])

# 5. Order Status
# 92% of initiated orders complete successfully, 8% fail (payment error, etc.)
is_completed = np.random.choice([0, 1], size=total_orders, p=[0.08, 0.92])

# Assemble synthetic DataFrame
orders_df = pd.DataFrame({
    "order_id": order_id,
    "user_id": order_user_id,
    "order_date": order_date,
    "aov": aov,
    "discount_applied": discount_applied,
    "is_completed": is_completed
})

print(orders_df)
orders_df.to_csv('orders_data.csv', index=False)