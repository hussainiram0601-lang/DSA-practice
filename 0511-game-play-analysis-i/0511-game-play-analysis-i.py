import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity.sort_values(by=['player_id','event_date']).groupby(['player_id']).min().reset_index()
    res.rename(columns={'event_date':'first_login'},inplace=True)
    return res[['player_id','first_login']]