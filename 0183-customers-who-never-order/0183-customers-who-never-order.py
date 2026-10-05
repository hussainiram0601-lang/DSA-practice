import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge_df = orders['customerId']
    null_cust = customers[~customers['id'].isin(merge_df)]
    return null_cust[['name']].rename(columns ={'name':'Customers'})
  
    