import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    val_user = users[users['mail'].str.contains(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$' , regex =True)]
    return val_user
    