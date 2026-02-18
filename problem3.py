def get_expenses():
#Simple loop to collect data into a dictionary of lists.
    data = {"Travel": [], "Meals": [], "Supplies": []}
    
    print("--- Enter Expenses (Type '0' to stop) ---")
    while True:
        cat = input("Category (Travel/Meals/Supplies): ").strip().title()
        if cat == '0': break
        
        if cat in data:
            try:
                val = float(input(f"Amount for {cat}: "))
                data[cat].append(val)
            except ValueError:
                print("Invalid number. Try again.")
        else:
            print("Invalid category.")
    return data

def main():
    # 1. Get the data
    expenses = get_expenses()
    
    # 2. Calculate and Print (The simplest summary logic)
    grand_total = 0
    print(f"\n{'SUMMARY':-^20}")
    
    for category, amounts in expenses.items():
        # Using a nested loop as requested by the skill parameters
        category_total = 0
        for amt in amounts:
            category_total += amt
        
        grand_total += category_total
        print(f"{category}: ${category_total:.2f}")
    
    print("-" * 20)
    print(f"TOTAL: ${grand_total:.2f}")


main()