import pandas as pd

def duplicate_emails(employee: pd.DataFrame) -> pd.DataFrame:
    group_emails = employee.groupby('email').filter(lambda x: len(x)>1)
    duplicate_emails = group_emails[['email']]
    result = duplicate_emails.drop_duplicates()
    return result