import numpy as np
import pandas as pd 
from USER_TABLE import users_df
np.random.seed(45)

total_sessions = 1800

session_id = ["SES_" + str(i).zfill(5) for i in range(1, total_sessions + 1)]
session_user_id = np.random.choice(users_df["user_id"], size=total_sessions)

start_ts = pd.to_datetime("2025-01-01").value // 10**9
end_ts = pd.to_datetime("2025-12-31").value // 10**9
random_ts = np.random.randint(start_ts, end_ts, size=total_sessions)
session_start = pd.to_datetime(random_ts, unit="s") 

devices = ['mobile', 'laptop', 'tablet']
device = np.random.choice(devices, total_sessions, p = [0.79, 0.10,0.11])

Landing_pages = ['Home', 'Category', 'Product', 'Ad_pdp']
Landing_page = np.random.choice(Landing_pages, size = total_sessions, p = [0.55, 0.25, 0.10, 0.10])

exit_pages = ['landing', 'Category', 'Product', 'Cart', 'Checkout', 'Thank_you']
exit_page = np.random.choice(exit_pages, size = total_sessions, p = [0.40, 0.25, 0.15, 0.10, 0.07, 0.03])

sessions_df = pd.DataFrame({'session_id': session_id,
                           'user_id': session_user_id,
                           'session_start': session_start,
                           'device': device,

                           'Landing_page': Landing_page,
                           'exit_page': exit_page})

print(sessions_df)
sessions_df.to_csv('sessions_data.csv', index=False)
print("sessions_data.csv")