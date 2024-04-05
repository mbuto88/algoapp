from data_fetcher import fetch_data_online, read_data_from_excel
from decision_maker import DecisionMaker
from strategy import MovingAverageStrategy
from stock_selector import StockSelector

def main():
    selector = StockSelector()
    selected_stocks = selector.get_stock_symbols()  # Get selected stocks

    strategy = MovingAverageStrategy()
    decision_maker = DecisionMaker(strategy)

    # User input for data source selection
    data_source = input("Select data source - 'online' for Alpaca API, 'excel' for Excel file: ").strip().lower()

    if data_source == 'online':
        for stock_symbol in selected_stocks:
            try:
                prices = fetch_data_online(stock_symbol)
                decision = decision_maker.make_decision(prices)
                print(f"Decision for {stock_symbol}: {decision}")
            except Exception as e:
                print(f"Error fetching data online for {stock_symbol}: {e}")

    elif data_source == 'excel':
        ticker_or_path = input("Enter the full path to your Excel file: ").strip()
        try:
            prices = read_data_from_excel(ticker_or_path)
            decision = decision_maker.make_decision(prices)
            print(f"Decision for {ticker_or_path}: {decision}")
        except Exception as e:
            print(f"Error reading data from Excel file at {ticker_or_path}: {e}")
    else:
        print("Invalid data source selected. Please choose 'online' or 'excel'.")

if __name__ == "__main__":
    main()
