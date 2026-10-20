import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    out_q1 = sales[
        (sales['sale_date']<'2019-01-01')|(sales['sale_date']>'2019-03-31')
    ]['product_id'].unique()
    in_q1 = sales[
        (sales['sale_date']>='2019-01-01')&(sales['sale_date']<='2019-03-31')
    ]['product_id'].unique()
    val_id = set(in_q1) - set(out_q1)
    return product[product['product_id'].isin(val_id)][['product_id','product_name']]