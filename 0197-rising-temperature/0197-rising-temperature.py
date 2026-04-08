import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)

    mask = (
        (weather['temperature']> weather['temperature'].shift(1)) &
        (weather['recordDate'] == weather['recordDate'].shift(1) + pd.Timedelta(days=1))
    )

    print(weather[mask]['id'])

    return pd.DataFrame({'id':weather[mask]['id']})