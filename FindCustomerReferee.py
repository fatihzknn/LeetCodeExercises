import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filtered_df = customer[(customer["referee_id"] != 2) | (customer["referee_id"].isna())]

    return filtered_df.iloc[:, [1]]