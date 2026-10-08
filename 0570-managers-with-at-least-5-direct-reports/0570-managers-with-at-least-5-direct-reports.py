import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    rc = employee.groupby('managerId').size().reset_index(name = 'rc')
    pop_em = rc[rc['rc']>=5]
    res = pop_em.merge(employee , left_on = 'managerId',right_on= 'id')
    return res[['name']]
    