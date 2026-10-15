import pandas as pd

def rearrange_products_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(df, id_vars=['product_id'], value_vars=['store1', 'store2','store3'] , var_name ='store',value_name='price').dropna()
    