import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    order_19 = orders[orders['order_date'].dt.year==2019]
    order_count = order_19.groupby('buyer_id')['order_id'].count().reset_index(name='orders_in_2019')
    res = pd.merge(users , order_count , left_on = 'user_id',right_on ='buyer_id',how ='left').drop(columns=['buyer_id'])
    res['orders_in_2019'] = res['orders_in_2019'].fillna(0).astype(int)
    res = res.rename(columns={'user_id':'buyer_id'})
    return res[['buyer_id','join_date','orders_in_2019']]

    