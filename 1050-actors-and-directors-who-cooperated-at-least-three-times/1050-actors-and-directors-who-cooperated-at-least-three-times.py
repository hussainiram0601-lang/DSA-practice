import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    res = actor_director.groupby(['actor_id','director_id']).size()
    res = res[res>=3].reset_index(name='cnt')
    return res[['actor_id','director_id']]
    