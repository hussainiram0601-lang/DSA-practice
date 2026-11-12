import pandas as pd

def biggest_single_number(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(keep=False).max().to_frame(name = 'num')
    