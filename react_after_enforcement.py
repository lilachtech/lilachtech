import pandas as pd

low_df = pd.read_csv('low_only.csv')

# low_df = df[df.conditions == 'low_enforcement']

# df.to_csv("low_only.csv", index=False)


# for index, row in df.iterrows():
#   #  print(row['c1'], row['c2'])
# last = low_df.irow(0)
# first = low_df.irow
#
# for i in range(1, df.shape[0]):
#     print(last)
#     print(df.irow(i))
#     last = df.irow(i)
choice_results_after_inspection = []

for index, row in low_df.iterrows():
    if row['inspection'] == 1:
        before = row['choice_correct']
        trail_number = row['trial_number']
        print(index, before, trail_number)
        first = low_df.iloc[index + 1]['choice_correct']
        second = low_df.iloc[index + 2]['choice_correct']
        third = low_df.iloc[index + 3]['choice_correct']
        choice_results_after_inspection.append({"trial_num": trail_number, "results": [first, second, third]})

    else:
        print('none')

print (choice_results_after_inspection)

for i in range (0, len(choice_results_after_inspection)):
    print(choice_results_after_inspection[i]['results'])
