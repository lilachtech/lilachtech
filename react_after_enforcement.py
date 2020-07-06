import pandas as pd

df = pd.read_csv('study1_tempt.csv')

low_df = df[df.conditions == 'low_enforcement']

low_df.to_csv("low_only.csv", index=False)


# for index, row in df.iterrows():
  #  print(row['c1'], row['c2'])

for index, row in low_df.iterrows():
    if row['inspection'] == 1:
        before = row['choice_correct']
        trail_number = row['trial_number']
        index_num = index
        print(index_num, before, trail_number)
        for i in low_df:
                low_df['']
    else:
        print('none')
