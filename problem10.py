def create_bar(value):
    #Returns a string of '#' symbols based on the value provided.
    # String multiplication: '#' * 3 results in '###'
    return "#" * value

def main():
    # 1. Projected Data (Scale: 1 '#' = $10k in revenue)
    projections = {
        "Year 1": 3,
        "Year 2": 5,
        "Year 3": 8,
        "Year 4": 12,
        "Year 5": 20
    }

    print("--- PROJECTED REVENUE GROWTH ---")
    print("(Scale: Each # represents $10,000)")
    print("-" * 35)

    # 2. Loop to generate the 'Chart'
    for year, revenue_units in projections.items():
        bar = create_bar(revenue_units)
        
        # Formatting the output to align the text and the bars
        print(f"{year:<7}: {bar}")

    print("-" * 35)
    print("End of Projection")

main()