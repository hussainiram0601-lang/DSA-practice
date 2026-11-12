import pandas as pd

def triangle_judgement(df: pd.DataFrame) -> pd.DataFrame:
    # max(x,y,z) == sqrt()
    condi =(
        (df['x'] + df['y'] > df['z']) &
        (df['x'] + df['z'] > df['y']) &
        (df['z'] + df['y'] > df['x'])
    )
    df['triangle'] = np.where(condi , 'Yes' , 'No')
    return df