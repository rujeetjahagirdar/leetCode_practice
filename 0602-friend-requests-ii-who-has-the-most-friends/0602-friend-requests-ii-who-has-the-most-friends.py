import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # req_counts = request_accepted["requester_id"].value_counts()
    # accep_counts = request_accepted["accepter_id"].value_counts()

    # total_counts = req_counts.add(accep_counts, fill_value=0)

    # print(total_counts)

    # return pd.DataFrame({"id": [total_counts.idxmax()], "num": [total_counts.max()]})

    temp = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']]).value_counts()

    return pd.DataFrame({"id": [temp.idxmax()], "num": [temp.max()]})