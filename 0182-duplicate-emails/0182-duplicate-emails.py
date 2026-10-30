import pandas as pd

def duplicate_emails(employee: pd.DataFrame) -> pd.DataFrame:
    grouped_emails = employee.groupby("email")
    duplicate_groups = grouped_emails.filter(lambda group: len(group) > 1)
    duplicate_emails = duplicate_groups[["email"]]
    result = duplicate_emails.drop_duplicates()
    return result