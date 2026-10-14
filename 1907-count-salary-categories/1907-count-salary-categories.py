import pandas as pd

def count_salary_categories(df: pd.DataFrame) -> pd.DataFrame:
    low_sal = len(df[df['income']<20000])
    avg_sal = len(df[(df['income']>=20000) & (df['income']<=50000)])
    high_sal = len(df[df['income']>50000])
    res = pd.DataFrame({
        'category':['Low Salary','Average Salary','High Salary'],
        'accounts_count':[low_sal,avg_sal,high_sal]
    })
    return res

    