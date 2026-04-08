import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    temp = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId', suffixes=("_cust", "_ord"))

    result = temp[temp['id_ord'].isna()]

    print(result['name'])

    return pd.DataFrame({'Customers': result['name']})