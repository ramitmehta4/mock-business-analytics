import numpy as np
import pandas as pd 

np.random.seed(45)

dates = pd.date_range("2025-04-01", "2025-06-30")
days = len(dates)

#constructing variants 
Var_1_df = pd.DataFrame({'Var':'A',
                         'metric_date': dates })
Var_1_df['user_exposed'] = np.random.randint(1000,1200 , size = days)
Var_1_df['conversions'] = np.random.binomial(n = Var_1_df['user_exposed'], p = 0.50)


Var_2_df = pd.DataFrame({'Var':'B',
                         'metric_date': dates })

Var_2_df['user_exposed'] = np.random.randint(1000,1200 , size = days)
Var_2_df['conversions'] = np.random.binomial(n = Var_2_df['user_exposed'], p = 0.52)

ab_test_df = pd.concat([Var_1_df,Var_2_df]).sort_values('metric_date')

print(ab_test_df)
ab_test_df.to_csv('ab_test_data.csv', index=False)