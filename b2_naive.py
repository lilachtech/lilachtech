import pandas as pd

df = pd.read_csv('temptation_pilot_2_3_b1_b2.csv')  # need to change file number
df = df[df.block_number == 2]
df.drop(df.columns.difference(['user_id', 'block_number', 'b2_sum']), 1, inplace=True)

b2_cheating = df.groupby(['user_id', 'block_number', 'b2_sum']).sum()  # need to change val name (naive/ cheat)

print(b2_cheating)  # need to change
b2_cheating.reset_index().to_csv(r'pilot_2_3_b2_cheating.csv', header=True, index=False)  # need to change val and file name