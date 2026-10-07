import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    is_consicutive = (
        (logs['num']==logs['num'].shift(1)) &
        (logs['num']==logs['num'].shift(2))
    )
    result = logs.loc[is_consicutive,'num'].drop_duplicates()
    return pd.DataFrame({f'ConsecutiveNums':result})
    