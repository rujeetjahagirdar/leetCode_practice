import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first_login'] = activity.groupby('player_id')['event_date'].transform('min')
    print(activity)
    result = activity[activity['event_date']==activity['first_login']+pd.Timedelta(days=1)]
    # print(result['player_id'])

    no_of_result = result['player_id'].nunique()
    total_players = activity['player_id'].nunique()

    return pd.DataFrame({'fraction': [round(no_of_result/total_players, 2)]})