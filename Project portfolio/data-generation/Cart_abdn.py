import numpy as np
import pandas as pd 
from Sessions_table import sessions_df

np.random.seed(45)

Abandoned_sessions = sessions_df[sessions_df['exit_page'].isin(['Cart', 'Checkout'])].copy()
sessions_num = len(Abandoned_sessions)

reason = [
    "Size/fit doubt", 
    "Shipping cost too high", 
    "Just browsing/saved for later", 
    "Found better price elsewhere", 
    "Payment method declined", 
    "Website technical error"
]

reason_category = np.random.choice(reason, size= sessions_num, p = [0.45, 0.25, 0.15, 0.08, 0.05, 0.02])

time_delays = pd.to_timedelta(np.random.randint(2, 15, size=sessions_num), unit="m")
reported_at = Abandoned_sessions['session_start'] + time_delays

Cart_abdn_rsn_df = pd.DataFrame({'Session_id': Abandoned_sessions['session_id'].values,
                             'reason_category': reason_category,
                             'reported_at': reported_at})

print(Cart_abdn_rsn_df)
Cart_abdn_rsn_df.to_csv('cart_abandonment_reasons_data.csv', index=False)
