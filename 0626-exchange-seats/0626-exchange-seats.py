import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    df = seat.copy()
    total = len(df)
    df['id'] = seat['id'].apply(lambda x: x+1 if x%2!=0 and x<total else x-1 if x%2==0 else x)
    df = df.sort_values(by = 'id' , ascending = True ).reset_index(drop = True)
    return df
    