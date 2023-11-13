
from scipy.stats import norm
from math import log, sqrt, exp

def call_price(spot_price, strike_price, time_to_expiry, risk_free_rate, volatility):
    """
    Calculates the price of a call option using the Black-Scholes model.
    
    Parameters:
    spot_price (float): The current price of the underlying asset.
    strike_price (float): The strike price of the call option.
    time_to_expiry (float): The time to expiry of the option in years.
    risk_free_rate (float): The risk-free interest rate.
    volatility (float): The volatility of the underlying asset.
    
    Returns:
    float: The price of the call option.
    """
    
    d1 = (log(spot_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_expiry) / (volatility * sqrt(time_to_expiry))
    d2 = d1 - volatility * sqrt(time_to_expiry)
    
    call_price = spot_price * norm.cdf(d1) - strike_price * exp(-risk_free_rate * time_to_expiry) * norm.cdf(d2)
    
    return call_price

def put_price(spot_price, strike_price, time_to_expiry, risk_free_rate, volatility):
    """
    Calculates the price of a put option using the Black-Scholes model.
    
    Parameters:
    spot_price (float): The current price of the underlying asset.
    strike_price (float): The strike price of the put option.
    time_to_expiry (float): The time to expiry of the option in years.
    risk_free_rate (float): The risk-free interest rate.
    volatility (float): The volatility of the underlying asset.
    
    Returns:
    float: The price of the put option.
    """
    
    d1 = (log(spot_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_expiry) / (volatility * sqrt(time_to_expiry))
    d2 = d1 - volatility * sqrt(time_to_expiry)
    
    put_price = strike_price * exp(-risk_free_rate * time_to_expiry) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
    
    return put_price

def iron_condor(buy_call_strike, sell_call_strike, sell_put_strike, buy_put_strike, expiration_date, underlying_price):
    """
    Implements an Iron Condor strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Iron Condor strategy.
    float: The maximum loss of the Iron Condor strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Iron Condor strategy
    max_profit = (sell_call_strike - buy_call_strike) + (sell_put_strike - buy_put_strike)
    max_loss = (sell_call_strike - buy_call_strike) - (underlying_price - sell_put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def bull_call_spread(buy_call_strike, sell_call_strike, expiration_date, underlying_price):
    """
    Implements a Bull Call Spread strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Bull Call Spread strategy.
    float: The maximum loss of the Bull Call Spread strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Bull Call Spread strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(sell_call_strike - buy_call_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def bear_call_spread(buy_call_strike, sell_call_strike, expiration_date, underlying_price):
    """
    Implements a Bear Call Spread strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Bear Call Spread strategy.
    float: The maximum loss of the Bear Call Spread strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Bear Call Spread strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(sell_call_strike - buy_call_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def bull_put_spread(buy_put_strike, sell_put_strike, expiration_date, underlying_price):
    """
    Implements a Bull Put Spread strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Bull Put Spread strategy.
    float: The maximum loss of the Bull Put Spread strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Bull Put Spread strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(sell_put_strike - buy_put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def bear_put_spread(buy_put_strike, sell_put_strike, expiration_date, underlying_price):
    """
    Implements a Bear Put Spread strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Bear Put Spread strategy.
    float: The maximum loss of the Bear Put Spread strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Bear Put Spread strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(sell_put_strike - buy_put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def covered_call(buy_stock_price, sell_call_strike, expiration_date, underlying_price):
    """
    Implements a Covered Call strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    sell_call_strike (float): The strike price of the call option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Covered Call strategy.
    float: The maximum loss of the Covered Call strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Covered Call strategy
    max_profit = sell_call_strike - buy_stock_price
    max_loss = -(buy_stock_price - underlying_price + sell_call_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def covered_put(buy_stock_price, sell_put_strike, expiration_date, underlying_price):
    """
    Implements a Covered Put strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    sell_put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns:
    float: The maximum profit of the Covered Put strategy.
    float: The maximum loss of the Covered Put strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Covered Put strategy
    max_profit = buy_stock_price - sell_put_strike
    max_loss = -(underlying_price - buy_stock_price + sell_put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def protective_call(buy_stock_price, buy_call_strike, expiration_date, underlying_price):
    """
    Implements a Protective Call strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    buy_call_strike (float): The strike price of the call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Protective Call strategy.
    float: The maximum loss of the Protective Call strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Protective Call strategy
    max_profit = float('inf')
    max_loss = -(buy_stock_price - buy_call_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def protective_put(buy_stock_price, buy_put_strike, expiration_date, underlying_price):
    """
    Implements a Protective Put strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    buy_put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Protective Put strategy.
    float: The maximum loss of the Protective Put strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Protective Put strategy
    max_profit = float('inf')
    max_loss = -(buy_put_strike - buy_stock_price)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call(call_strike, expiration_date, underlying_price):
    """
    Implements a Long Call strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to buy.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Call strategy.
    float: The maximum loss of the Long Call strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call strategy
    max_profit = float('inf')
    max_loss = -(call_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put(put_strike, expiration_date, underlying_price):
    """
    Implements a Long Put strategy using options.
    
    Parameters:
    put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Put strategy.
    float: The maximum loss of the Long Put strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put strategy
    max_profit = float('inf')
    max_loss = -(underlying_price - put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call(call_strike, expiration_date, underlying_price):
    """
    Implements a Short Call strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to sell.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Short Call strategy.
    float: The maximum loss of the Short Call strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call strategy
    max_profit = call_strike
    max_loss = -(float('inf'))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put(put_strike, expiration_date, underlying_price):
    """
    Implements a Short Put strategy using options.
    
    Parameters:
    put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Short Put strategy.
    float: The maximum loss of the Short Put strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put strategy
    max_profit = put_strike
    max_loss = -(float('inf'))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call_butterfly(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Long Call Butterfly strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Call Butterfly strategy.
    float: The maximum loss of the Long Call Butterfly strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call Butterfly strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put_butterfly(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Long Put Butterfly strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Put Butterfly strategy.
    float: The maximum loss of the Long Put Butterfly strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put Butterfly strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call_butterfly(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Short Call Butterfly strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Short Call Butterfly strategy.
    float: The maximum loss of the Short Call Butterfly strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call Butterfly strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put_butterfly(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Short Put Butterfly strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Short Put Butterfly strategy.
    float: The maximum loss of the Short Put Butterfly strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put Butterfly strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call_condor(buy_call_strike, sell_call_strike, sell_call_strike2, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Long Call Condor strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    sell_call_strike2 (float): The strike price of the second call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Call Condor strategy.
    float: The maximum loss of the Long Call Condor strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call Condor strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike2 - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put_condor(buy_put_strike, sell_put_strike, sell_put_strike2, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Long Put Condor strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    sell_put_strike2 (float): The strike price of the second put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns:
    float: The maximum profit of the Long Put Condor strategy.
    float: The maximum loss of the Long Put Condor strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put Condor strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike2 - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call_condor(buy_call_strike, sell_call_strike, sell_call_strike2, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Short Call Condor strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    sell_call_strike2 (float): The strike price of the second call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Short Call Condor strategy.
    float: The maximum loss of the Short Call Condor strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call Condor strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike2 - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put_condor(buy_put_strike, sell_put_strike, sell_put_strike2, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Short Put Condor strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    sell_put_strike2 (float): The strike price of the second put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Short Put Condor strategy.
    float: The maximum loss of the Short Put Condor strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put Condor strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike2 - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call_calendar(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Long Call Calendar strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Long Call Calendar strategy.
    float: The maximum loss of the Long Call Calendar strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call Calendar strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put_calendar(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Long Put Calendar strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Long Put Calendar strategy.
    float: The maximum loss of the Long Put Calendar strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put Calendar strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call_calendar(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Short Call Calendar strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

     Returns: 
    float: The maximum profit of the Short Call Calendar strategy.
    float: The maximum loss of the Short Call Calendar strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call Calendar strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put_calendar(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Short Put Calendar strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

     Returns: 
    float: The maximum profit of the Short Put Calendar strategy.
    float: The maximum loss of the Short Put Calendar strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put Calendar strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call_diagonal(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Long Call Diagonal strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Call Diagonal strategy.
    float: The maximum loss of the Long Call Diagonal strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call Diagonal strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put_diagonal(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Long Put Diagonal strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Put Diagonal strategy.
    float: The maximum loss of the Long Put Diagonal strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put Diagonal strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call_diagonal(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a Short Call Diagonal strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Call Diagonal strategy.
    float: The maximum loss of the Short Call Diagonal strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call Diagonal strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put_diagonal(buy_put_strike, sell_put_strike, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements a Short Put Diagonal strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    buy_put_strike2 (float): The strike price of the second put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Put Diagonal strategy.
    float: The maximum loss of the Short Put Diagonal strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put Diagonal strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(buy_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_call_ratio(buy_call_strike, sell_call_strike, sell_call_strike2, expiration_date, underlying_price):
    """
    Implements a Long Call Ratio strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    sell_call_strike2 (float): The strike price of the second call option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Call Ratio strategy.
    float: The maximum loss of the Long Call Ratio strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Call Ratio strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(sell_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike) + (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_put_ratio(buy_put_strike, sell_put_strike, sell_put_strike2, expiration_date, underlying_price):
    """
    Implements a Long Put Ratio strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    sell_put_strike2 (float): The strike price of the second put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Put Ratio strategy.
    float: The maximum loss of the Long Put Ratio strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Put Ratio strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(sell_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike) + (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_call_ratio(buy_call_strike, sell_call_strike, sell_call_strike2, expiration_date, underlying_price):
    """
    Implements a Short Call Ratio strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    sell_call_strike2 (float): The strike price of the second call option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Call Ratio strategy.
    float: The maximum loss of the Short Call Ratio strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Call Ratio strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(sell_call_strike2 - sell_call_strike - (sell_call_strike - buy_call_strike) + (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_put_ratio(buy_put_strike, sell_put_strike, sell_put_strike2, expiration_date, underlying_price):
    """
    Implements a Short Put Ratio strategy using options.
    
    Parameters:
    buy_put_strike (float): The strike price of the put option to buy.
    sell_put_strike (float): The strike price of the put option to sell.
    sell_put_strike2 (float): The strike price of the second put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Put Ratio strategy.
    float: The maximum loss of the Short Put Ratio strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Put Ratio strategy
    max_profit = sell_put_strike - buy_put_strike
    max_loss = -(sell_put_strike2 - sell_put_strike - (sell_put_strike - buy_put_strike) + (sell_put_strike - buy_put_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_straddle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Long Straddle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to buy.
    put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Straddle strategy.
    float: The maximum loss of the Long Straddle strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Straddle strategy
    max_profit = float('inf')
    max_loss = -(call_strike + put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_straddle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Short Straddle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to sell.
    put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Straddle strategy.
    float: The maximum loss of the Short Straddle strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Straddle strategy
    max_profit = call_strike + put_strike
    max_loss = -(float('inf'))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_strangle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Long Strangle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to buy.
    put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Strangle strategy.
    float: The maximum loss of the Long Strangle strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Strangle strategy
    max_profit = float('inf')
    max_loss = -(call_strike + put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_strangle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Short Strangle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to sell.
    put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Strangle strategy.
    float: The maximum loss of the Short Strangle strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Strangle strategy
    max_profit = call_strike + put_strike
    max_loss = -(float('inf'))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def long_guts(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Long Guts strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to buy.
    put_strike (float): The strike price of the put option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Long Guts strategy.
    float: The maximum loss of the Long Guts strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Long Guts strategy
    max_profit = float('inf')
    max_loss = -(call_strike - put_strike)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def short_guts(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Short Guts strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option to sell.
    put_strike (float): The strike price of the put option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
     Returns: 
    float: The maximum profit of the Short Guts strategy.
    float: The maximum loss of the Short Guts strategy.
    """
    
    # Calculate the maximum profit and maximum loss of the Short Guts strategy
    max_profit = call_strike - put_strike
    max_loss = -(float('inf'))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
     # Return the maximum profit and maximum loss
    return max_profit, max_loss

def vertical_spread(buy_strike, sell_strike, expiration_date, underlying_price, buy_option_type='call', sell_option_type='call'):
    """
    Implements a Vertical Spread strategy using options.
    
    Parameters:
    buy_strike (float): The strike price of the option to buy.
    sell_strike (float): The strike price of the option to sell.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    buy_option_type (str): The type of option to buy, either 'call' or 'put'. Defaults to 'call'.
    sell_option_type (str): The type of option to sell, either 'call' or 'put'. Defaults to 'call'.
    
    Returns: 
    float: The maximum profit of the Vertical Spread strategy.
    float: The maximum loss of the Vertical Spread strategy.
    """
    
    # Determine the option types
    buy_option = buy_option_type.lower()
    sell_option = sell_option_type.lower()
    
    # Determine the option prices
    if buy_option == 'call':
        buy_price = call_price(buy_strike, expiration_date, underlying_price)
    else:
        buy_price = put_price(buy_strike, expiration_date, underlying_price)
        
    if sell_option == 'call':
        sell_price = call_price(sell_strike, expiration_date, underlying_price)
    else:
        sell_price = put_price(sell_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Vertical Spread strategy
    max_profit = (sell_price - buy_price) * 100
    max_loss = (buy_price - sell_price) * 100
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def combination(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Combination strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option.
    put_strike (float): The strike price of the put option.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns: 
    float: The maximum profit of the Combination strategy.
    float: The maximum loss of the Combination strategy.
    """
    
    # Determine the option prices
    call_price = call_price(call_strike, expiration_date, underlying_price)
    put_price = put_price(put_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Combination strategy
    max_profit = float('inf')
    max_loss = -1 * (call_price + put_price)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def collar(buy_stock_price, sell_call_strike, buy_put_strike, expiration_date, underlying_price):
    """
    Implements a Collar strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was bought.
    sell_call_strike (float): The strike price of the call option sold.
    buy_put_strike (float): The strike price of the put option bought.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns: 
    float: The maximum profit of the Collar strategy.
    float: The maximum loss of the Collar strategy.
    """
    
    # Determine the option prices
    call_price = call_price(sell_call_strike, expiration_date, underlying_price)
    put_price = put_price(buy_put_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Collar strategy
    max_profit = call_price + (buy_stock_price - buy_put_strike) - put_price
    max_loss = buy_stock_price - buy_put_strike - call_price
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")
    
    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def risk_reversal(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a Risk Reversal strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option.
    put_strike (float): The strike price of the put option.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Risk Reversal strategy.
    float: The maximum loss of the Risk Reversal strategy.
    """
    
    # Determine the option prices
    call_price = call_price(call_strike, expiration_date, underlying_price)
    put_price = put_price(put_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Risk Reversal strategy
    max_profit = float('inf')
    max_loss = -1 * (call_price - put_price)
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def box_spread(buy_call_strike, sell_call_strike, buy_put_strike, sell_put_strike, expiration_date, underlying_price):
    """
    Implements a Box Spread strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option bought.
    sell_call_strike (float): The strike price of the call option sold.
    buy_put_strike (float): The strike price of the put option bought.
    sell_put_strike (float): The strike price of the put option sold.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Box Spread strategy.
    float: The maximum loss of the Box Spread strategy.
    """
    
    # Determine the option prices
    call_price = call_price(buy_call_strike, expiration_date, underlying_price)
    put_price = put_price(buy_put_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Box Spread strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_put_strike - sell_put_strike - (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def iron_butterfly(buy_call_strike, sell_call_strike, sell_call_strike2, buy_call_strike2, buy_put_strike, sell_put_strike, sell_put_strike2, buy_put_strike2, expiration_date, underlying_price):
    """
    Implements an Iron Butterfly strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option bought.
    sell_call_strike (float): The strike price of the call option sold.
    sell_call_strike2 (float): The strike price of the second call option sold.
    buy_call_strike2 (float): The strike price of the second call option bought.
    buy_put_strike (float): The strike price of the put option bought.
    sell_put_strike (float): The strike price of the put option sold.
    sell_put_strike2 (float): The strike price of the second put option sold.
    buy_put_strike2 (float): The strike price of the second put option bought.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The maximum profit of the Iron Butterfly strategy.
    float: The maximum loss of the Iron Butterfly strategy.
    """
    
    # Determine the option prices
    call_price = call_price(buy_call_strike, expiration_date, underlying_price)
    put_price = put_price(buy_put_strike, expiration_date, underlying_price)
    
    # Calculate the maximum profit and maximum loss of the Iron Butterfly strategy
    max_profit = sell_call_strike - buy_call_strike
    max_loss = -(buy_put_strike2 - sell_put_strike2 - (sell_call_strike - buy_call_strike) + (sell_call_strike - buy_call_strike))
    
    # Print the maximum profit and maximum loss
    print(f"Maximum profit: {max_profit}")
    print(f"Maximum loss: {max_loss}")

    # Return the maximum profit and maximum loss
    return max_profit, max_loss

def binary_option(strike_price, expiration_date, underlying_price, option_type='call', payout=100):
    """
    Implements a binary option strategy using options.
    
    Parameters:
    strike_price (float): The strike price of the option.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    option_type (str): The type of option, either 'call' or 'put'. Default is 'call'.
    payout (float): The payout amount if the option is in the money. Default is 100.
    
    Returns: 
    float: The profit or loss of the binary option strategy.
    """
    
    # Determine the option price
    option_price = call_price(strike_price, expiration_date, underlying_price) if option_type == 'call' else put_price(strike_price, expiration_date, underlying_price)
    
    # Determine if the option is in the money
    in_the_money = underlying_price > strike_price if option_type == 'call' else underlying_price < strike_price
    
    # Calculate the profit or loss of the binary option strategy
    return payout if in_the_money else -option_price

def synthetic_put(buy_stock_price, sell_call_strike, expiration_date, underlying_price):
    """
    Implements a synthetic put strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock is bought.
    sell_call_strike (float): The strike price of the call option sold.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns: 
    float: The profit or loss of the synthetic put strategy.
    """
    
    # Determine the option price
    option_price = call_price(sell_call_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the synthetic put strategy
    return max(0, sell_call_strike - buy_stock_price) - option_price

def synthetic_call(buy_stock_price, sell_put_strike, expiration_date, underlying_price):
    """
    Implements a synthetic call strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock is bought.
    sell_put_strike (float): The strike price of the put option sold.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns: 
    float: The profit or loss of the synthetic call strategy.
    """
    
    # Determine the option price
    option_price = put_price(sell_put_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the synthetic call strategy
    return max(0, buy_stock_price - sell_put_strike) - option_price

def strangle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a strangle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option.
    put_strike (float): The strike price of the put option.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.
    
    Returns: 
    float: The profit or loss of the strangle strategy.
    """
    
    # Determine the option prices
    call_price = call_price(call_strike, expiration_date, underlying_price)
    put_price = put_price(put_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the strangle strategy
    return max(0, underlying_price - call_strike - put_price) + max(0, put_strike - underlying_price - call_price)

def straddle(call_strike, put_strike, expiration_date, underlying_price):
    """
    Implements a straddle strategy using options.
    
    Parameters:
    call_strike (float): The strike price of the call option.
    put_strike (float): The strike price of the put option.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The profit or loss of the straddle strategy.
    """
    
    # Determine the option prices
    call_price = call_price(call_strike, expiration_date, underlying_price)
    put_price = put_price(put_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the straddle strategy
    return max(0, underlying_price - call_strike - put_price) + max(0, call_strike - underlying_price - put_price)

def butterfly(buy_call_strike, sell_call_strike, buy_call_strike2, expiration_date, underlying_price):
    """
    Implements a butterfly strategy using options.
    
    Parameters:
    buy_call_strike (float): The strike price of the call option to buy.
    sell_call_strike (float): The strike price of the call option to sell.
    buy_call_strike2 (float): The strike price of the second call option to buy.
    expiration_date (str): The expiration date of the options in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The profit or loss of the butterfly strategy.
    """
    
    # Determine the option prices
    buy_call_price = call_price(buy_call_strike, expiration_date, underlying_price)
    sell_call_price = call_price(sell_call_strike, expiration_date, underlying_price)
    buy_call_price2 = call_price(buy_call_strike2, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the butterfly strategy
    return max(0, underlying_price - buy_call_strike - buy_call_price) - 2 * max(0, underlying_price - sell_call_strike - sell_call_price) + max(0, underlying_price - buy_call_strike2 - buy_call_price2)

def married_put(buy_stock_price, buy_put_strike, expiration_date, underlying_price):
    """
    Implements a married put strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    buy_put_strike (float): The strike price of the put option.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The profit or loss of the married put strategy.
    """
    
    # Determine the option price
    put_price = put_price(buy_put_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the married put strategy
    return max(0, underlying_price - buy_put_strike - put_price) + max(0, buy_put_strike - underlying_price - buy_stock_price)

def married_call(buy_stock_price, sell_call_strike, expiration_date, underlying_price):
    """
    Implements a married call strategy using options.
    
    Parameters:
    buy_stock_price (float): The price at which the stock was purchased.
    sell_call_strike (float): The strike price of the call option.
    expiration_date (str): The expiration date of the option in the format 'YYYY-MM-DD'.
    underlying_price (float): The current price of the underlying asset.

    Returns: 
    float: The profit or loss of the married call strategy.
    """
    
    # Determine the option price
    call_price = call_price(sell_call_strike, expiration_date, underlying_price)
    
    # Calculate the profit or loss of the married call strategy
    return max(0, sell_call_strike - underlying_price - buy_stock_price) + max(0, underlying_price - sell_call_strike - call_price)
