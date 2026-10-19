import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filt = activity[
        (activity['activity_date'] >= '2019-06-28')&
        (activity['activity_date'] <= '2019-07-27')
    ]
    df = filt.groupby('activity_date')['user_id'].nunique().reset_index().drop_duplicates()
    df.columns = ['day','active_users']
    return df
    