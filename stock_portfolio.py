import yfinance as yf
import datetime
# Strategy class to store stock/ETFs information
class Strategy:
    def __init__(self, symbol, name, strategy):
        self.symbol = symbol
        self.name = name
        self.strategy = strategy


# Define investment strategy for 3 different stocks/ETFs 
strategies = [
    # Index Investing stocks
    Strategy("VTI", "Vanguard Total Stock Market ETF", "Index Investing"),
    Strategy("IXUS", "iShares Core MSCI Total International Stock ETF", "Index Investing"),
    Strategy("ILTB", "iShares Core 10+ Year USD Bond ETF", "Index Investing"),
    # Ethical Investing stocks
    Strategy("AAPL", "Apple Inc.", "Ethical Investing"),
    Strategy("ADBE", "Adobe Inc.", "Ethical Investing"),
    Strategy("NSRGY", "Nestle S.A.", "Ethical Investing"),
    # Growth Investing stocks
    Strategy("AMZN", "Amazon.com Inc.", "Growth Investing"),
    Strategy("GOOGL", "Alphabet Inc.", "Growth Investing"),
    Strategy("NVDA", "NVIDIA Corporation", "Growth Investing"),
    # Quality Investing stocks
    Strategy("MSFT", "Microsoft Corporation", "Quality Investing"),
    Strategy("MCD", "McDonald's Corporation", "Quality Investing"),
    Strategy("V", "Visa Inc. Class A", "Quality Investing"),
    # Value Investing stocks
    Strategy("JPM", "JPMorgan Chase & Co.", "Value Investing"),
    Strategy("WMT", "Walmart Inc.", "Value Investing"),
    Strategy("PFE", "Pfizer Inc.", "Value Investing"),
]


# Get stock data using yf library
def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period="30d")

    # stock_data = stock.history(period="1d", interval="1m")
    # Can't use info to get current price due to
    # Exception: yfinance failed to decrypt Yahoo data response --> .info

    # print(stock_data)
    return stock_data


# Create a portfolio based on user's selected strategies and investment amount
def create_portfolio(investment_amount, selected_strategies):
    # create new list for the 3 stocks/ETFs mapped on the selected strategies
    selected_stocks = [x for x in strategies if x.strategy in selected_strategies]
    # Divide the investment amount evenly for each stock
    investment_per_stock = investment_amount / len(selected_stocks)
    portfolio = []

    # Loop through the selected stocks to store data in portfolio
    for stock in selected_stocks:
        # Get the stock data from yf
        stock_data = get_stock_data(stock.symbol)
        # Get the current price of the stock
        current_price = float(stock_data["Close"].iloc[-1])
        # Number of shares to buy
        num_shares = investment_per_stock / current_price
        # Add the stock data to the portfolio
        portfolio.append(
            {
                "stock": stock,
                "investment": investment_per_stock,
                "num_shares": num_shares,
                "current_price": current_price,
                "stock_data": stock_data,
            }
        )

    # print(portfolio)
    return portfolio


# Get the weekly history of the portfolio value
def calculate_weekly_trend(portfolio):
    weekly_trend = []

    # keep 5 days history of the overall portfolio value (No Weekend)
    for i in range(7):
        # Get the date for each day
        date = datetime.date.today() - datetime.timedelta(days=i + 1)
        daily_value = 0

        # Loop through the stocks in the portfolio
        for stock_info in portfolio:
            # Get the stock data from yf
            stock_data = stock_info["stock_data"]
            # Get the stock's closing price for the day
            price_data = stock_data[stock_data.index.date == date]["Close"]
            # Check if there is data available for the specific date
            if not price_data.empty:
                price = float(price_data.iloc[0])
                # Get value of the portfolio for the day
                daily_value += stock_info["num_shares"] * price

        # Add the daily value and date to the weekly trend list
        if daily_value > 0:
            weekly_trend.append({"date": date, "value": daily_value})

    # print(weekly_trend)
    # return list from the oldest to the newest date
    return weekly_trend[::-1]
