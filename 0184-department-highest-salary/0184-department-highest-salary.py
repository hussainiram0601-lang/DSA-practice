import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee[employee['salary']==employee.groupby('departmentId')['salary'].transform('max')]
    result = employee.merge(department, left_on = 'departmentId',right_on = 'id').rename(
        columns={
            'name_x': 'Employee',
            'name_y': 'Department',
            'salary': 'Salary'
        }
    )
    return result[['Department','Employee','Salary']]