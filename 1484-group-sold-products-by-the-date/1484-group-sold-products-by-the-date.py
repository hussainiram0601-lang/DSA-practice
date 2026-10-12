import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    res = activities.drop_duplicates().groupby('sell_date')['product'].agg( num_sold = 'count' , products = list).reset_index()
    res.products = res.products.apply( lambda x : ',' .join(sorted(x)))
    return res
    