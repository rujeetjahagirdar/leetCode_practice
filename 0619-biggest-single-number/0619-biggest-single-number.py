import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    single_numbers = counts[counts==1]
    result = single_numbers.index.max() if not single_numbers.empty else None
    return pd.DataFrame({"num": [result]})