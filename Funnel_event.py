from BA_PROJECT.USER_TABLE import users_df
from BA_PROJECT.Sessions_table import sessions_df
import numpy as np
import pandas as pd 
from datetime import timedelta

np.random.seed(45)
import pandas as pd
import numpy as np

# Import your existing sessions table
from BA_PROJECT.Sessions_table import sessions_df

np.random.seed(44)

# Define the exact sequential order matching your exit_pages
ordered_stages = ['landing', 'Category', 'Product', 'Cart', 'Checkout', 'Thank_you']

funnel_events = []
event_counter = 1

# Iterate through every session to build the chronological event trail
for index, row in sessions_df.iterrows():
    session_id = row['session_id']
    current_time = row['session_start']
    exit_page = row['exit_page']
    
    # Determine how many steps this user completed before dropping off
    exit_index = ordered_stages.index(exit_page)
    
    # Generate a sequential event for each stage reached
    for i in range(exit_index + 1):
        stage_name = ordered_stages[i]
        
        funnel_events.append({
            'event_id': f"EVT_{event_counter:06d}",
            'session_id': session_id,
            'stage': stage_name,
            'event_time': current_time
        })
        
        event_counter += 1
        
        # Add a natural browsing delay (15 to 120 seconds) before the next event
        current_time += pd.to_timedelta(np.random.randint(15, 120), unit="s")

# Assemble the final synthetic DataFrame
funnel_events_df = pd.DataFrame(funnel_events)

print(funnel_events_df.head(10))
funnel_events_df.to_csv('funnel_events_data.csv', index=False)
