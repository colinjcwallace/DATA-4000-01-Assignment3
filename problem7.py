def get_total_stock(warehouse_list):
    #Aggregates inventory from all warehouses into one dictionary.
    totals = {}

    # Outer Loop: Go through each warehouse dictionary
    for warehouse in warehouse_list:
        inventory = warehouse["inventory"]
        
        # Inner Loop: Go through each item in the inventory dictionary
        for product, count in inventory.items():
            if product in totals:
                totals[product] += count
            else:
                totals[product] = count
                
    return totals

def main():
    # 1. Data Structure: List of Dictionaries
    warehouses = [
        {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
        {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
        {"name": "Warehouse C", "inventory": {"apples": 50, "oranges": 80}}
    ]

    # 2. Process Data
    total_inventory = get_total_stock(warehouses)

    # 3. Output Results
    print("--- GLOBAL INVENTORY TOTALS ---")
    for product, total in total_inventory.items():
        print(f"{product.title()}: {total}")

main()