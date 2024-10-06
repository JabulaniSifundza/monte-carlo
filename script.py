import math
import numpy as np
import matplotlib.pyplot as plt

N = 252
time_step = 1.0

def run_monte_carlo_simulations(drift, sigma, initial_price):
    # Generating random increments for Brownian Motion
    # Using geometric Brownian motion to create simulations
    log_returns = np.random.normal(drift - 0.5 * sigma ** 2, sigma, size=(1000, 252))
    # Simulating price paths
    price_paths = initial_price * np.exp(log_returns.cumsum(axis=1))
    # Plotting simulated Prices 
    plt.plot(price_paths.T)
    plt.show()
    ending_prices = price_paths[:,-1]
    # Plotting simulated Prices
    plt.hist(ending_prices, bins=50, edgecolor='blue')
    plt.title("Ending Prices")
    plt.show()
    # Annual log return calculation
    annual_log_returns = np.log(ending_prices / initial_price)
    # Plotting annual log returns
    plt.hist(annual_log_returns, bins=50, edgecolor='blue')
    plt.title("Annual Log Returns")
    plt.show()
    # Calculating expected annual returns
    expected_annual_return = np.mean(annual_log_returns)
    print(expected_annual_return)
    # Calculated annual volatility/risk
    daily_volatility = np.std(log_returns)
    annualized_standard_deviation = daily_volatility * np.sqrt(252)
    print(annualized_standard_deviation)
    return None
