import pandas as pd
import yfinance as yf

def fetch_data_online(ticker):
    data = yf.download(ticker, period="30d")
    return data['Close']

def read_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df[df.columns[0]]
