def assign_tiers(customer_data):
    #Categorizes customers into tiers based on their spending.
    # Initialize our counter dictionary
    tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}

    for name, spent in customer_data.items():
        if spent < 1000:
            tier_counts["Bronze"] += 1
        elif 1000 <= spent < 5000:
            tier_counts["Silver"] += 1
        else:
            tier_counts["Gold"] += 1
            
    return tier_counts

def main():
    # 1. Sample Data
    customers = {
        "Alice": 1200, 
        "Bob": 500, 
        "Charlie": 6000, 
        "Diana": 2500, 
        "Edward": 800
    }

    # 2. Process tiers
    summary = assign_tiers(customers)

    # 3. Print Results
    print("--- Loyalty Tier Summary ---")
    for tier, count in summary.items():
        print(f"{tier}: {count} customers")


main()