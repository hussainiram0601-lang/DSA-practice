import pandas as pd

def not_boring_movies(df: pd.DataFrame) -> pd.DataFrame:
    df = df[(df['id']%2!=0) & (df['description']!='boring')].sort_values(by='rating',ascending = False)
    return df
    