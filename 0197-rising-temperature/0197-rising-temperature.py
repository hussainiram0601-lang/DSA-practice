import pandas as pd

def rising_temperature(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values('recordDate')
    res = (df['temperature'] > df['temperature'].shift(1)) &  (df['recordDate'] - df['recordDate'].shift(1) == pd.Timedelta(days =1))
    return df[res][['id']]

    
    