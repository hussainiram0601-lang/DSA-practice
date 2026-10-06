import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    h_sal = employee['salary'].drop_duplicates().sort_values(ascending= False)
    if len(h_sal)>=N and N>0:
        n_sal = h_sal.iloc[N-1]
        return pd.DataFrame({f'getNthHighestSalary({N})' : [n_sal] })
    
    return pd.DataFrame({f'getNthHighestSalary({N})' :[None] })