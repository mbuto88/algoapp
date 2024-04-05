import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame
from config import API_KEY, API_SECRET, BASE_URL

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def fetch_data_online(ticker, start_date='2023-01-01', end_date='2023-01-31'):
    """
    Fetches historical stock data for the given ticker from Alpaca within the specified date range.
    """
    # Updated to use get_bars instead of get_barset.
    data = api.get_bars(ticker, TimeFrame.Day, start=start_date, end=end_date).df
    return data['close']

def read_data_from_excel(file_path):
    """
    Reads stock price data from an Excel file. Assumes the data is in the first column.
    """
    df = pd.read_excel(file_path)
    return df[df.columns[0]]
