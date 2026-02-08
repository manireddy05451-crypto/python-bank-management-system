balance = 0.0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited: ${amount:.2f}")
    print(f"Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: ${amount:.2f}")
        print(f"Successfully withdrawn ${amount:.2f}. New balance: ${balance:.2f}")

def check_balance():
    print(f"Current balance: ${balance:.2f}")

def transactions_history():
    print("--- Transaction History ---")
    for t in transactions:
        print(t)
    if not transactions:
        print("No transactions yet.")

def menu():
    while True:
        print("------ PyBank Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. check Balance")
        print("4. View Transactions History")
        print("5. Exit")

        choice = input("enter your choice: ")

        if choice == '1':
            amount = float(input("enter amount to deposit: "))
            deposit(amount)
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            transactions_history()
        elif choice == '5':
            print("thank you for using PyBank. Goodbye!")
            break
        else:
            print("invalid choice.")

menu()