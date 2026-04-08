import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders["count"] = orders.groupby("customer_number")["order_number"].transform("count")

    # print(orders)
    result = orders[orders["count"]==max(orders["count"])]["customer_number"].drop_duplicates()
    return(pd.DataFrame({"customer_number": result}))