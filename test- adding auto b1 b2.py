import pandas as pd


def b1_sum(input_name, output_name):

    df = pd.read_csv(input_name)
    df = df[df.block_number == 1]
    df.drop(df.columns.difference(['user_id', 'block_number', 'b1_sum']), 1, inplace=True)

    b1_cheating = df.groupby(['user_id', 'block_number', 'b1_sum']).sum()

    print(b1_cheating)
    b1_cheating.reset_index().to_csv(output_name, header=True, index=False)


# b1_sum('pilot_2_3_temptation_ambiguous_b1_b2.csv', 'pilot_2_3_tempt_amb_b1.csv')
# b1_sum('pilot_2_3_temptation_clear_b1_b2.csv', 'pilot_2_3_tempt_clear_b1.csv')
# b1_sum('not_temptation_amb_b1_b2.csv', 'not_temptation_amb_b1.csv')
b1_sum('not_tempt_pilot1_clear_b1_b2.csv', 'not_tempt_pilot1_clear_b1.csv')
# b1_sum('not_tempt_pilot1_amb_b1_b2.csv', 'not_tempt_pilot1_amb_b1.csv')


def b2_sum(input_name, output_name):
    df = pd.read_csv(input_name)
    df = df[df.block_number == 2]
    df.drop(df.columns.difference(['user_id', 'block_number', 'b2_sum']), 1, inplace=True)

    b2_cheating = df.groupby(['user_id', 'block_number', 'b2_sum']).sum()  # need to change val name (naive/ cheat)

    print(b2_cheating)  # need to change
    b2_cheating.reset_index().to_csv(output_name, header=True, index=False)  # need to change val and file name


# b2_sum('pilot_2_3_temptation_ambiguous_b1_b2.csv', 'pilot_2_3_tempt_amb_b2.csv')
# b2_sum('pilot_2_3_temptation_clear_b1_b2.csv', 'pilot_2_3_tempt_clear_b2.csv')
# b2_sum('not_temptation_amb_b1_b2.csv', 'not_temptation_amb_b2.csv')
b2_sum('not_tempt_pilot1_clear_b1_b2.csv', 'not_tempt_pilot1_clear_b2.csv')
# b2_sum('not_tempt_pilot1_amb_b1_b2.csv', 'not_tempt_pilot1_amb_b2.csv')
