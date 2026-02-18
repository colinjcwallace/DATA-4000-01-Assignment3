def get_item_prices():
    prices_list = []  # Initialize an empty list
    while True:
        try:
            price = float(input("Enter item price: "))
            if price == 0:
                return prices_list  # SUCCESS: Return the whole list
            elif price < 0:
                print("Price cannot be negative.")
            else:
                prices_list.append(price)  # ADD the price to the list
        except ValueError:
            print("Invalid input.")
# input for item prices
# took into account negative values and non-numeric inputs


def calculate_total(prices):
    return sum(prices)
# calculates the total price of the items in the list x

def count_items(prices):
    return len(prices)
# counts the number of items in the list x

def avg_price(prices):
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)


def main():
    print("--- POS System Started (Enter 0 to finish) ---")
    prices = get_item_prices()
    print(f"Your total is: ${calculate_total(prices):.2f}")
    print(f"You bought {count_items(prices)} items.")
    print(f"The average price per item is: ${avg_price(prices):.2f}")

main()
