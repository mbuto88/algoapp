from data_fetcher import fetch_data_online, read_data_from_excel
from decision_maker import DecisionMaker
from strategy import MovingAverageStrategy

def main():
    strategy = MovingAverageStrategy()
    decision_maker = DecisionMaker(strategy)

    # User input for data source selection
    data_source = input("Select data source - 'online' for Yahoo Finance, 'excel' for Excel file: ").strip().lower()
    ticker_or_path = ""
    prices = None

    if data_source == 'online':
        ticker_or_path = input("Enter the stock ticker (e.g., 'AAPL'): ").strip()
        try:
            prices = fetch_data_online(ticker_or_path)
        except Exception as e:
            print(f"Error fetching data online for {ticker_or_path}: {e}")
    elif data_source == 'excel':
        ticker_or_path = input("Enter the full path to your Excel file: ").strip()
        try:
            prices = read_data_from_excel(ticker_or_path)
        except Exception as e:
            print(f"Error reading data from Excel file at {ticker_or_path}: {e}")
    else:
        print("Invalid data source selected. Please choose 'online' or 'excel'.")

    if prices is not None:
        decision = decision_maker.make_decision(prices)
        print(f"Decision for {ticker_or_path}: {decision}")
    else:
        print("No decision made due to previous errors or invalid input.")

if __name__ == "__main__":
    main()
