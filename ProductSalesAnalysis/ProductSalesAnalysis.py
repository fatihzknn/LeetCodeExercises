import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(sales,product, on = "product_id", how= "inner")
    return merged_df[["product_name","year","price"]]