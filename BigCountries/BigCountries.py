import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    filtered_df = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    return filtered_df[["name","population","area"]]

