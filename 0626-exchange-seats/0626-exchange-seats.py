import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    total = len(seat)
    seat['id'] = seat['id'].apply(lambda x: x+1 if x%2!=0 and x < total else x-1 if x%2==0 else x)
    seat = seat.sort_values(by ='id' , ascending = True).reset_index(drop =True)
    return seat
    