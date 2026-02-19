# stock_tracker.py

def main():
    # 1. Nested Dictionary Structure
    portfolio = {
        "AAPL": {"shares": 10, "price": 170},
        "TSLA": {"shares": 4, "price": 250},
        "AMZN": {"shares": 2, "price": 130}
    }

    portfolio_total = 0

    print(f"{'Ticker':<10} | {'Shares':>8} | {'Price':>10} | {'Total Value':>12}")
    print("-" * 50)

    # 2. Loop through the nested dictionary
    # 'ticker' will be "AAPL", "TSLA", etc.
    # 'info' will be the inner dictionary {"shares": 10, "price": 170}
    for ticker, info in portfolio.items():
        # Accessing inner dictionary values by key
        shares = info["shares"]
        price = info["price"]
        
        # Calculation
        holding_value = shares * price
        portfolio_total += holding_value
        
        # Display each row
        print(f"{ticker:<10} | {shares:>8} | ${price:>9.2f} | ${holding_value:>11.2f}")

    # 3. Final Summary
    print("-" * 50)
    print(f"{'GRAND TOTAL PORTFOLIO VALUE:':<35} ${portfolio_total:>11.2f}")

    main()