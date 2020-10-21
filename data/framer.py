from keychain.keyset import POLYGON_API_KEY
from polygon import RESTClient

import pandas as pd

from datetime import datetime, timedelta


def csvframer(ticker: str, folder: str) -> list():
    with RESTClient(POLYGON_API_KEY) as client:
        response = client.stocks_equities_aggregates(
            ticker, 1, "DAY", "1111-11-11", "2019-12-12")
    data = response.results
    df = pd.DataFrame(data)
    start = ((datetime.today() - timedelta(days=2)) -
             timedelta(days=len(data)))
    starter = start.strftime('%Y-%m-%d')
    df.index = pd.to_datetime(
        df.index, origin=pd.Timestamp(starter), unit='d')
    df.rename(columns={"o": "Open", "h": "High", "l": "Low",
                       "c": "Close", "v": "Volume"}, inplace=True)
    df.index.name = 'Date'
    del df['vw']
    del df['t']
    del df['n']
    df = df[['Open', 'High', 'Low', 'Close', 'Close', 'Volume']]
    df.to_csv(folder + ticker + ".csv")
