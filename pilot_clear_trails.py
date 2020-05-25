import pandas as pd

# clear_df = pd.read_csv('temptation_only.csv')
# clear_df = clear_df[clear_df.trial_type == 'Clear_not_profit_side']

ambiguous_trails_df = pd.read_csv('temptation_only.csv')
ambiguous_trails_df = ambiguous_trails_df[ambiguous_trails_df.trial_type != 'Clear_not_profit_side']

# clear_df.to_csv(r'pilot_clear_trails.csv', index=False)
ambiguous_trails_df.to_csv(r'pilot_ambiguous_trails.csv', index=False)
