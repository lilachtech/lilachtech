import pandas as pd
import os

'''
import pandas as pd
# open file
df = pd.read_csv('new_5ec22961a5533967a888db87.csv')

# creating new column with final blocks errors
block_errors = df['block_errors'].value_counts()
extract_block_errors = block_errors.index.tolist()
b1_errors = extract_block_errors[0]  # b1 errors
b2_errors = extract_block_errors[1]  # b2 errors
final_errors = b1_errors + b2_errors  # full game errors
idx = 19
df.insert(loc=idx, column='final_errors', value=final_errors)


df.to_csv(r'new_5ec22961a5533967a888db87_final_errors.csv', index=False)
'''


fileNames = ['new_5ec22961a5533967a888db87_final_errors.csv', 'pilot_data_temptation.csv']

dfList = []

for f in fileNames:
    Dataframes = pd.read_csv(f, header=None)
    dfList.append(Dataframes)

concatDf = pd.concat(dfList, axis=0)
concatDf.to_csv('Combine_clean_pilot1.csv', index=None)
