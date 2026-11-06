import pandas as pd

def find_investments(df: pd.DataFrame) -> pd.DataFrame:
    df1 = df[(df.duplicated(subset = ['tiv_2015'], keep= False))]
    df2 = df1[~df.duplicated(subset=['lat','lon'],keep=False)]
    return pd.DataFrame({'tiv_2016':[round(df2['tiv_2016'].sum(), 2)]})
    
    