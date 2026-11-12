import pandas as pd

def biggest_single_number(df: pd.DataFrame) -> pd.DataFrame:
    df['count'] = df['num'].map(df['num'].value_counts())
    single = df[df['count']==1]
    if single.empty:
        return pd.DataFrame({'num':[None]})

    max_single = single['num'].max()
    return pd.DataFrame({'num':[max_single]})
    
    