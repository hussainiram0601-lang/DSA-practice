import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_count = employee.groupby(['managerId']).size().reset_index(name = 'report_count')
    popular_man = report_count[report_count['report_count']>=5]
    result = popular_man.merge(employee , left_on= 'managerId',right_on = 'id')
    return result[['name']]
    