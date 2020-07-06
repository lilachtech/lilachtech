import pandas as pd

df = pd.read_csv('rows_export_pilot_1_2.csv')  # need to change file number

user_data = df.groupby(['user_id', 'conditions', 'final_payoff']).sum()

print(user_data)  # need to change
user_data.reset_index().to_csv(r'pilot_1_2_bonus.csv', header=True, index=False)  # need to change val and file name