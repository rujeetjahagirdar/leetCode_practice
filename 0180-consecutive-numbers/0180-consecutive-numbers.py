import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    mask = ((logs['num']==logs['num'].shift(1)) & (logs['num']==logs['num'].shift(2)))

    result = logs[mask]['num'].drop_duplicates()

    return(pd.DataFrame({'ConsecutiveNums': result}))