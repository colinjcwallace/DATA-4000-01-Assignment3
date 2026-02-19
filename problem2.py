def get_survey_data():

    responses = []
    # Define valid options for validation
    valid_options = ["coffee", "tea", "soda"]
    
    print("--- Market Survey (Enter 0 to finish) ---")
    print(f"Options: {', '.join(valid_options)}")
    
    while True:
        # Get input, remove whitespace, and convert to lowercase
        user_choice = input("Enter preference: ").strip().lower()
        
        if user_choice == '0':
            break
            
        # Validation: Check if the input is in our allowed list
        if user_choice in valid_options:
            responses.append(user_choice)
        else:
            print(f"Invalid entry: '{user_choice}'. Please choose Coffee, Tea, or Soda.")
            
    return responses

def calculate_market_share(data_list):
#Uses a dictionary to count items and prints the percentage share.
    counts = {}
    total = len(data_list)
    
    if total == 0:
        print("\nNo valid survey data was collected.")
        return

    # Counting logic using a dictionary
    for item in data_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            
    print("\n--- Market Share Results ---")
    for product, count in counts.items():
        # Arithmetic: (Count / Total) * 100
        percentage = (count / total) * 100
        print(f"{product.title()}: {percentage:.0f}%")

def main():
    # 1. Get the list of data from the user
    survey_results = get_survey_data()
    
    # 2. Process that list to show the dictionary-based summary
    calculate_market_share(survey_results)



main()