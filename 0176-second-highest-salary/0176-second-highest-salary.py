import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    highest_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(highest_salary)<2:
        return pd.DataFrame({f'SecondHighestSalary':[None]})
    second_highest = highest_salary.iloc[1]
    return pd.DataFrame({f'SecondHighestSalary':[second_highest]})
    