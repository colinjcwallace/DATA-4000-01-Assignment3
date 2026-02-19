## Problem 1

- Created function get_item_prices to input price until 0 entered. accounted for invalid inputs with exceptions.
- Created function calculate_total to sum the prices entered.
- Created function count_items to return a count of inputed items.
- Created function avg_price to calculate price (sum(prices / len(prices))
- Created main function with the prints and rest of functions

________________________________________________________

## Problem 2

- Created function get_survey_data for input of survey data. Outlined valid options and dealt with invalid inputs. Loop ends with input of 0
- Created function calculate_market_share to use a dictionary to count items and print the percentage share.
- Created main function to join the two other functions into one usable function.

________________________________________________________

## Problem 3

- Created function get_expenses as a simple loop to collect data into a dictionary of lists, Travel, Meals, and Supplies. Dealt with invalid inputs with an exception.
- Create main function to calculate and print the simplest summary logic with a nested loop to sum amounts for each category.

_______________________________________________________

## Problem 4

- Created function calculate_commission to calculate a flat 10% commission on sales totals.
- Created main function to iterate through the employee dictionary and store results in a list of tuples for sorting.
- Implemented a sorting algorithm using a lambda key to rank employees from highest to lowest commission.
- Generated a formatted leaderboard output with rank, name, and currency formatting.

______________________________________________________

## Problem 5

- Utilized a nested dictionary structure to represent a stock portfolio (Ticker -> Shares/Price).
- Created a loop using the .items() method to "drill down" into the inner dictionaries to access specific stock data.
- Calculated the total value for each individual holding and maintained a running grand total for the entire portfolio.
- Printed a structured financial report with aligned columns and decimal precision for prices.

_____________________________________________________

## Problem 6

- Created function pay_month to handle the iterative math of adding monthly interest and subtracting a fixed payment.
- Implemented a while loop that runs dynamically until the loan balance reaches zero.
- Included a safety break within the loop to prevent infinite runs if the monthly payment is lower than the interest accrued.
- Tracked the number of iterations to report the total time required for loan repayment in months.

_____________________________________________________

## Problem 7

- Modeled a complex supply chain using a list of dictionaries, where each warehouse contained its own nested inventory dictionary.
- Created function get_total_stock using nested loops: the outer loop iterates through warehouses, while the inner loop aggregates product counts.
- Used a dictionary to tally global totals, handling the addition of new products dynamically.
- Printed a global inventory summary for all products found across the entire supply chain.

_____________________________________________________

## Problem 8

- Created function assign_tiers to process customer spending data and categorize it into Bronze, Silver, and Gold levels.
- Used a series of if/elif/else conditionals to evaluate numerical ranges for each loyalty tier.
- Utilized a dictionary to store the frequency counts of customers falling into each specific category.
- Created a summary report to display the distribution of the customer base across the three tiers.

____________________________________________________

## Problem 9

- Created function calculate_growth to apply an annual growth rate formula to business revenue.
- Implemented a for loop using range(1, 11) to simulate exactly 10 years of business operations.
- Applied compound growth logic where each year's starting revenue is based on the previous year's result.
- Generated a year-by-year projection table using f-string formatting to include thousands-separators for large currency values.

_____________________________________________________

## Problem 10

- Created function create_bar to demonstrate string multiplication by repeating characters based on an integer value.
- Mapped a dictionary of yearly projections to a visual ASCII-style bar chart.
- Used a for loop to iterate through the dataset and print a "Year" label alongside a scaled bar of # symbols.
- Implemented string padding to ensure the visual chart remained aligned and easy to read for a business pitch simulation.
