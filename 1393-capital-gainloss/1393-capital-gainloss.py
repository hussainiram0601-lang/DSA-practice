import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    def helper_function(operation , price):
        if operation == 'Buy':
            return -int(price)
        else :
            return int(price)

    stocks['price'] = stocks.apply(lambda x: helper_function(x['operation'] , x['price']),axis =1)
    res = stocks.groupby('stock_name')['price'].sum().reset_index(name= 'capital_gain_loss')
    return res[['stock_name','capital_gain_loss']]    