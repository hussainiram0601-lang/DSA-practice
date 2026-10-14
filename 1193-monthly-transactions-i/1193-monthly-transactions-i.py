import pandas as pd

def monthly_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df['month']= df['trans_date'].astype(str).str.slice(0,7)
    df['is_appr'] = (df['state']=='approved')
    df['appr_amt'] = df['amount']*df['is_appr']
    res = df.groupby(['month','country'],dropna=False).agg(
        trans_count=('id','count'),
        approved_count=('is_appr','sum'),
        trans_total_amount =('amount','sum'),
        approved_total_amount=('appr_amt','sum')
    ).reset_index()
    return res
    