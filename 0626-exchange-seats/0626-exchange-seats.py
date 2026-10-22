import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat['id'] = np.where( seat['id']%2==0 , seat['id'] -1 , np.where(seat['id']==seat['id'].max() , seat['id'] , seat['id']+1) )
    return seat.sort_values('id')
    