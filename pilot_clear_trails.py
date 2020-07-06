import pandas as pd


def ambiguous_trails(file_name_input, file_name_output):
    ambiguous_trails_df = pd.read_csv(file_name_input)  # file of all tempt
    ambiguous_trails_df = ambiguous_trails_df[ambiguous_trails_df.trial_type != 'Clear_profit_side']  # when tempt != clear_not_profit_side when not tempt != 'Clear_profit_side'

    ambiguous_trails_df.to_csv(file_name_output, index=False)


# ambiguous_trails('temptation_pilot_2_3.csv', "temptation_amb.csv")
ambiguous_trails('not_tempt_pilot1.csv', "not_tempt_pilot1_amb.csv")


def clear_trails(file_name_input, file_name_output):
    clear_df = pd.read_csv(file_name_input)
    clear_df = clear_df[clear_df.trial_type == 'Clear_profit_side']  # when tempt need != when not tempt need to ==
    clear_df.to_csv(file_name_output, index=False)


# clear_trails('temptation_pilot_2_3.csv', "temptation_clear.csv")
clear_trails('not_tempt_pilot1.csv', "not_tempt_pilot1_clear.csv")
