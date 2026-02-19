# commission_leaderboard.py

def calculate_commission(amount):
    """Simple 10% commission calculation."""
    return amount * 0.10

def main():
    # 1. Employee Sales Data
    sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
    
    # 2. Process and Rank
    # We use a list to store the results so we can sort them
    leaderboard = []
    
    for name in sales:
        total_sales = sales[name]
        commission = calculate_commission(total_sales)
        # Store as a list [Name, Commission]
        leaderboard.append([name, commission])
    
    # Sort by the commission (index 1), highest to lowest
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    # 3. Print Results
    print(f"{'Rank':<5} | {'Employee':<10} | {'Commission':>10}")
    print("-" * 35)
    
    count = 1
    for entry in leaderboard:
        # entry[0] is name, entry[1] is commission
        print(f"{count:<5} | {entry[0]:<10} | ${entry[1]:>9.2f}")
        count += 1


main()