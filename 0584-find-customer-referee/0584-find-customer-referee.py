import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # temp = pd.merge(customer, customer, left_on="referee_id", right_on="id", how="left", suffixes= ("_cust","_ref"))

    # print(temp)

    # result = temp[(temp["referee_id_cust"].isna()) | (temp['referee_id_cust']!=2)]

    # return(pd.DataFrame({'name':result['name_cust']}))

    result = customer[(customer['referee_id'].isna()) | (customer['referee_id']!=2)]

    return pd.DataFrame({"name": result['name']})