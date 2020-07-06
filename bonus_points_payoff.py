import pandas as pd

# open file
df = pd.read_csv('rows_export_pilot_2_3.csv')
# user_id = df['user_id'].unique()

# print(user_id)
# df = df[df.user_id == '5ec29601269fcc072b89c5c8']
# b1_rates = df['b1_sum'].value_counts()
bonus_points = df.groupby(['user_id', 'bonus']).sum()

print(bonus_points)

bonus_points.reset_index().to_csv(r'pilot_2_3_bonus_payoff.csv', header=True, index=False)
