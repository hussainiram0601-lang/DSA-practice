import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    salar_map = employee.set_index('id')['salary']
    employee['man_sal'] = employee['managerId'].map(salar_map)
    res = employee[employee['salary']>employee['man_sal']]
    return res[['name']].rename(columns={'name':'Employee'})
    