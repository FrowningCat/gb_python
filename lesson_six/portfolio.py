_total_cost = {"AAPL": 1502.50, "GOOGL": 12503.75, "MSFT": 2404}


def colculate_porfolio_value(stocks: dict, prices: dict) -> float:
    cost = 0
    for i in stocks:
        cost = cost + (float(stocks[i]) * float(prices[i]))
        # _total_cost[i] = cost
    return cost


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    if initial_value > current_value:
        percent = ((initial_value - current_value) / current_value) * 100
    else:
        percent = ((current_value - initial_value) / initial_value) * 100
    return percent


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    stock = ""
    global _total_cost
    stonks = float(list(_total_cost.values())[0]) - (float(list(stocks.values())[0]) * float(list(prices.values())[0]))
    for i in stocks:
        cost = float(stocks[i]) * float(prices[i])
        if stonks < cost:
            stonks = float(_total_cost[i]) - (float(stocks[i]) * float(prices[i]))
            x = stocks[i]
            stock = {i for i in stocks if stocks[i] == x}
    return stock
