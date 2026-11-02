import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department , left_on = 'departmentId' , right_on = 'id', suffixes = ('','_dept'))
    df['rank'] = df.groupby('departmentId')['salary'].rank(method = 'dense' , ascending = False)
    df = df[df['rank']<=3]
    res = df[['name_dept','name','salary']].copy()
    res.columns =['Department', 'Employee','Salary']
    return res
    