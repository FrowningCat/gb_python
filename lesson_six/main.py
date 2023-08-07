from portfolio import colculate_porfolio_value as value, calculate_portfolio_return as c_return, \
    get_most_profitable_stock as stock

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

print(value(stocks, prices))
print(c_return(10000.0, 15000.0))
print(stock(stocks, prices))
