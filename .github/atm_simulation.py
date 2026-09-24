import sys

def atm_simulation():
    # Initial balance and secure PIN
    balance = 5000.0
    correct_pin = "1234"
    
    print("=== WELCOME TO THE ATM INTERFACE ===")
    
    # Secure PIN verification step
    pin_input = input("Please enter your 4-digit PIN: ")
    
    if pin_input != correct_pin:
        print("Error: Invalid PIN. Access denied.")
        return

    print("\nAuthentication successful!")
    
    while True:
        # User-friendly console interface menu
        print("\n--- ATM MENU ---")
        print("1. Real-time Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            # Real-time balance inquiry
            print(f"Your current balance is: Rs. {balance:.2f}")
            
        elif choice == '2':
            # Cash deposit functionality
            try:
                amount = float(input("Enter amount to deposit: Rs. "))
                if amount > 0:
                    balance += amount
                    print(f"Successfully deposited Rs. {amount:.2f}")
                    print(f"Updated balance is: Rs. {balance:.2f}")
                else:
                    print("Error: Deposit amount must be positive.")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '3':
            # Cash withdrawal functionality
            try:
                amount = float(input("Enter amount to withdraw: Rs. "))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"Successfully withdrew Rs. {amount:.2f}")
                        print(f"Remaining balance is: Rs. {balance:.2f}")
                    else:
                        print("Error: Insufficient balance.")
                else:
                    print("Error: Withdrawal amount must be positive.")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    atm_simulation()
