import pandas as pd

# open file
df = pd.read_csv('pilot_ambiguous_trails.csv')

df['b1_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 1 and row['error'] == 1) else 0, axis=1)
df['b2_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 2 and row['error'] == 1) else 0, axis=1)

df['b1_sum'] = df.groupby(['user_id', 'block_number'])['b1_cheating'].transform('sum')
df['b2_sum'] = df.groupby(['user_id', 'block_number'])['b2_cheating'].transform('sum')

cheating_rates = df.groupby(['user_id', 'block_number', 'error']).sum()
print(cheating_rates)


df.to_csv(r'pilot_ambiguous_b1_b2.csv', index=False)
