import numpy as np
import pandas as pd
from datetime import timedelta

# Set seed for reproducible results
np.random.seed(45)

# Dataset volume
total_records = 1000

# 1. Primary Key: user_id
user_id = ["USR_" + str(i).zfill(5) for i in range(1, total_records + 1)]

# 2. Date Column: signup_date across a 1-year timeline
start_date = pd.to_datetime("2025-01-01")
end_date = pd.to_datetime("2025-12-31")
days_difference = (end_date - start_date).days
random_days = np.random.randint(0, days_difference, size=total_records)
signup_date = start_date + pd.to_timedelta(random_days, unit="D")

# 3. Encoded Logic: 80/20 New vs Returning Users Split
# (0 = New User [80%], 1 = Returning User [20%])
is_returning = np.random.choice([0, 1], size=total_records, p=[0.80, 0.20])

# 4. Encoded Logic: Acquisition Channel Mix
channels = ["organic", "paid", "social", "direct"]
channel_weights = [0.35, 0.30, 0.20, 0.15]
acquisition_channel = np.random.choice(
    channels, size=total_records, p=channel_weights
)

# 5. Country Demographics
countries = ["US", "UK", "CA", "DE", "IN"]
country_weights = [0.45, 0.20, 0.15, 0.10, 0.10]
country = np.random.choice(countries, size=total_records, p=country_weights)

# Assemble synthetic DataFrame
users_df = pd.DataFrame(
    {
        "user_id": user_id,
        "signup_date": signup_date,
        "is_returning": is_returning,
        "acquisition_channel": acquisition_channel,
        "country": country,
    }
)

# Inspect first few rows
users_df.to_csv('users_data.csv', index=False)



