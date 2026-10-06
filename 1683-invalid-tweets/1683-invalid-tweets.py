import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    inval = tweets[tweets['content'].str.len()>15]
    return inval[['tweet_id']]
    
    