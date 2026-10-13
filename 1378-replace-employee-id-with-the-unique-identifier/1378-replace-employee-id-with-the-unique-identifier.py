import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employees ,employee_uni, how = 'left', on = 'id' )
    return res[['unique_id','name']]