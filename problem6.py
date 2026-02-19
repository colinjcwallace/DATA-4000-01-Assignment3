# loan_simulator.py

def pay_month(current_balance, interest_rate, payment):
#Adds interest and subtracts payment for one month.
    interest = current_balance * (interest_rate / 12)
    return current_balance + interest - payment

def main():
    # 1. Inputs
    balance = float(input("Loan amount: "))
    rate = float(input("Interest rate (e.g. 0.05): "))
    payment = float(input("Monthly payment: "))
    
    months = 0

    # 2. The Simple While Loop
    # Keep looping as long as we owe money
    while balance > 0:
        balance = pay_month(balance, rate, payment)
        months += 1
        
        # Safety break: stop if balance is growing instead of shrinking
        if months > 1000: 
            print("Payment too low; loan will never be paid off.")
            return

    # 3. Final Output
    print(f"Total months to pay off: {months}")

main()