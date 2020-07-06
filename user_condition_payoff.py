import pandas as pd

df = pd.read_csv('Combine_clean_pilot1.csv')  # need to change file number

user_data = df.groupby(['user_id', 'conditions', 'final_payoff']).sum()

print(user_data)  # need to change
user_data.reset_index().to_csv(r'Combine_clean_pilot1_details.csv', header=True, index=False)  # need to change val and file name