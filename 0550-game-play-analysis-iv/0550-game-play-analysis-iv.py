import pandas as pd

def gameplay_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df['event_date'] = pd.to_datetime(df['event_date'])
    first_login = df.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id','first_login']
    first_login['next_date'] = first_login['first_login'] + pd.Timedelta(days=1)
    df2 = df.merge(first_login , on='player_id' , how='left')
    return pd.DataFrame({'fraction':[round(df2[df2['event_date']==df2['next_date']]['player_id'].nunique() / df['player_id'].nunique() , 2) ]})


    