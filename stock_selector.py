import pandas as pd
from datetime import datetime, timedelta
from alpaca_trade_api.rest import REST, TimeFrame
from config import API_KEY, API_SECRET, BASE_URL


class StockSelector:
    def __init__(self):
        self.api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

    def fetch_tradable_assets(self):
        active_assets = self.api.list_assets(status='active')
        return [asset for asset in active_assets if asset.tradable and asset.exchange in ['NASDAQ', 'NYSE']]

    def get_stock_symbols(self, target_number=100):
        tradable_assets = self.fetch_tradable_assets()
        selected_stocks = []

        # Adjusted criteria
        min_volume = 1000000  # Starting point for volume threshold
        days_ago = 5
        start_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')  # Calculate '5 days ago' date

        while len(selected_stocks) < target_number and min_volume > 0:
            selected_stocks.clear()  # Reset the list for each iteration

            for asset in tradable_assets:
                if self.meets_criteria(asset.symbol, min_volume, start_date):
                    selected_stocks.append(asset.symbol)

            # Adjust criteria if fewer than target_number stocks are found
            if len(selected_stocks) < target_number:
                min_volume -= 100000  # Decrease volume threshold

        return selected_stocks

    def meets_criteria(self, symbol, min_volume, start_date):
        """Check if a stock meets all defined criteria."""
        try:
            # Fetch data from the start date to now
            bars = self.api.get_bars(symbol, TimeFrame.Day, start_date, datetime.now().strftime('%Y-%m-%d')).df
            if bars.empty:
                return False

            # Apply each criterion
            if not self.volume_criterion(bars, min_volume):
                return False
            if not self.price_change_criterion(bars):
                return False

            return True
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return False

    def volume_criterion(self, bars, min_volume):
        """Volume criterion."""
        avg_volume = bars['volume'].mean()
        return avg_volume >= min_volume

    def price_change_criterion(self, bars):
        """Price change criterion."""
        price_change = bars['close'].iloc[-1] - bars['close'].iloc[0]
        return price_change >= 0
