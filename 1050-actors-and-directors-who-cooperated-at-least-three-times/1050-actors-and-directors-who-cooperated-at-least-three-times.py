import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id','director_id']).filter(lambda x : len(x)>=3)[['actor_id','director_id']].drop_duplicates()
    return result
    