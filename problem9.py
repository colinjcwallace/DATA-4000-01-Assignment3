def calculate_growth(current_revenue, rate):
#   Calculates the revenue for the following year.
    return current_revenue * (1 + rate)

def main():
    # 1. User Inputs
    try:
        initial_revenue = float(input("Enter initial revenue: "))
        growth_rate = float(input("Enter annual growth rate (e.g., 0.05 for 5%): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # 2. Header for the table
    print(f"\n{'Year':<10} | {'Projected Revenue':>20}")
    print("-" * 35)
    

    current_revenue = initial_revenue

    # 3. Projection Loop (10 Years)
    # range(1, 11) gives us years 1 through 10
    for year in range(1, 11):
        current_revenue = calculate_growth(current_revenue, growth_rate)
        
        # Print the results in a formatted table
        print(f"Year {year:<5} | ${current_revenue:>18,.2f}")

main()