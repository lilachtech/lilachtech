import pandas as pd

tempt_df = pd.read_csv('pilot_data_temptation.csv')
tempt_df = tempt_df.query("profitable_side != true_side")
# tempt_df['condition'].replace(['high_enforcement','low_enforcement', 'no_enforcement'],[1, 2, 3],inplace=True)

tempt_df['error'] = tempt_df.apply(lambda row: 0 if (row['choice_correct'] == 1) else 1, axis=1)
cheating_rates = tempt_df.groupby('user_id')['error'].sum()
# cheating_rates = df.groupby(['user_id', 'block_number', 'error']).sum()
print(cheating_rates)
print(type(cheating_rates))


# cheating_rate = tempt_df.choice_correct.sum()
# print(cheating_rate)



#tempt_df.to_csv(r'temptation.csv', index=False)