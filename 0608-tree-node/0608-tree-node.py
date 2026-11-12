import pandas as pd

def tree_node(df: pd.DataFrame) -> pd.DataFrame:
    parents = df['p_id'].unique()
    conditions = [
        df['p_id'].isna() ,
        df['id'].isin(parents) ]    
    choice = ['Root', 'Inner']
    df['type'] =np.select(conditions , choice, default = 'Leaf')
    return df[['id','type']]

    