import pandas as pd

# open file
df = pd.read_csv('full_pilot1_b1_b2.csv')

'''
user_id = df['user_id'].unique()

for i in user_id:
    
    df = df[df.user_id == i]
    blocks_rates = df.groupby(['block_number', 'b1_sum', 'b2_sum']).sum()
    blocks_rates.reset_index().to_csv(r'CCCC_output_summary.csv', header=True, index=False)
    print(blocks_rates)
'''

df = df[df.user_id == '5ec29601269fcc072b89c5c8']
# b1_rates = df['b1_sum'].value_counts()
b1_rates = df.groupby(['block_number', 'b1_sum', 'b2_sum']).sum()
# b1_rates = df.query('block_number==1')['b1_sum']

b1_rates.reset_index().to_csv(r'CCCC_output_summary.csv', header=True, index=False)

print(b1_rates)
print(type(b1_rates))

