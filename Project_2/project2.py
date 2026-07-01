#ATM simulator

balance = 1000
correct_pin = 1234
attempts = 0

# PIN Verification
while attempts < 3:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("\nWelcome to Python ATM")

        while True:
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Current Balance: ₹", balance)

            elif choice == 2:
                amount = float(input("Enter amount to deposit: ₹"))

                if amount > 0:
                    balance += amount
                    print("₹", amount, "deposited successfully.")
                else:
                    print("Invalid amount! Deposit amount must be positive.")

            elif choice == 3:
                amount = float(input("Enter amount to withdraw: ₹"))

                if amount <= 0:
                    print("Invalid amount! Withdrawal amount must be positive.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print("Please collect your cash.")
                    print("Remaining Balance: ₹", balance)

            elif choice == 4:
                print("Thank you for using Python ATM!")
                break

            else:
                print("Invalid choice! Please try again.")

        break

    else:
        attempts += 1
        if attempts < 3:
            print("Incorrect PIN! Attempts left:", 3 - attempts)
        else:
            print("Account Locked! Too many incorrect PIN attempts.")
