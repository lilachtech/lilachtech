import pandas as pd


def b1_b2(input_name, output_name):
    df = pd.read_csv(input_name)

    df['b1_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 1 and row['error'] == 1) else 0, axis=1)
    df['b2_cheating'] = df.apply(lambda row: 1 if (row['block_number'] == 2 and row['error'] == 1) else 0, axis=1)

    df['b1_sum'] = df.groupby(['user_id', 'block_number'])['b1_cheating'].transform('sum')
    df['b2_sum'] = df.groupby(['user_id', 'block_number'])['b2_cheating'].transform('sum')

    df.to_csv(output_name, index=False)


# b1_b2('pilot_2_3_temptation_ambiguous.csv', 'pilot_2_3_temptation_ambiguous_b1_b2.csv')  # for ambiguous tempt
# b1_b2('pilot_2_3_temptation_clear.csv', 'pilot_2_3_temptation_clear_b1_b2.csv')  # for clear tempt
b1_b2('not_tempt_pilot1_clear.csv', 'not_tempt_pilot1_clear_b1_b2.csv')  # for clear not tempt
# b1_b2('not_tempt_pilot1_amb.csv', 'not_tempt_pilot1_amb_b1_b2.csv')  # for ambiguous not tempt
# b1_b2('not_tempt_pilot1.csv', 'pilot1_not_tempt_b1_b2.csv')  # b1 b2 for all not tempt
