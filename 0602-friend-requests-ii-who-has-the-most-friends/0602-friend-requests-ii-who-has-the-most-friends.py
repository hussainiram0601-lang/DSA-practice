import pandas as pd

def most_friends(df: pd.DataFrame) -> pd.DataFrame:
    ids = pd.concat([df['requester_id'],df['accepter_id']]) 
    res = ids.value_counts().reset_index().rename(columns={'index':'id', 0:'num','count':'num'}).head(1)
    return res[['id','num']]

    