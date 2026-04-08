import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # counts = person['email'].value_counts()
    # print(type(counts))
    # print(counts)

    # result = counts[counts>1].index
    # print(result)

    # return pd.DataFrame({'Email': result})

    counts = person.groupby('email')['email'].count()
    result = counts[counts>1]
    print(result)
    return pd.DataFrame({'Email': result.index})

    # person['email_counts'] = person.groupby('email')['email'].transform('count')

    # print(person)