# Enhanced Bank Account Management System
from operator import index
from zoneinfo import available_timezones

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []         # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account(user, balance, loan):
    """Create a new account."""


    if user not in account_holders:
        account_holders.append(user)
        balances.append(balance)
        loans.append(loan)
        transaction_histories.append([])
        return f"Hello {user}, Your account is created successfully with balance {balance}. You have {loan} loans."

    else:
        return f"Account with this name '{user}' already exists in the system"


def deposit(account, amount):
    """Deposit money into an account."""
    if account not in account_holders:
        return f'Error: Account "{account}" does not exist in the system!'

    if amount <= 0:
        return f"Error: Deposit amount must be greater than Zero!"

    index_deposit = account_holders.index(account)
    balances[index_deposit] += amount
    transaction_histories[index_deposit].append(f'Deposited: {amount}')
    return f'You have deposited {amount} successfully!'

def withdraw(account, amount):
    """Withdraw money from an account."""
    if account not in account_holders:
        return f'Error: Account "{account}" does not exist in the system!'

    if amount <= 0:
        return f"Error: Deposit amount must be greater than Zero!"

    index_withdraw = account_holders.index(account)
    balances[index_withdraw] -= amount
    transaction_histories[index_withdraw].append(f'Withdrawn: {amount}')
    return f'You have withdrawn {amount} successfully!'

def check_balance(account, balance):
    """Check balance of an account."""
    if account not in account_holders:
        return f'Error: Account "{account}" does not exist in the system!'

    index_balance = account_holders.index(account)

    return f'You have {balance[index_balance]} available in your account!'


def list_accounts(account, balance, loan):
    """List all account holders and details."""

    account = account_holders
    balance = balances
    loan = loans

    return list(zip(account, balance, loan))


def transfer_funds(account, target_account, amount):
    """Transfer funds between two accounts."""
    if account not in account_holders:
        return f'Error: Account "{account}" does not exist in the system!'

    if target_account not in account_holders:
        return f'Error: The target account "{account}" does not exist in the system!'

    if amount < 10:
        return f'Error: Minimum amount for transfer - 10.00!'

    index_sender = account_holders.index(account)
    balances[index_sender] -= amount
    transaction_histories[index_sender].append(f'Transferred: {amount}')

    index_receiver = account_holders.index(target_account)
    balances[index_receiver] += amount
    transaction_histories[index_receiver].append(f'Transfer: {amount}')
    return f'Your Transfer for {amount} to "{target_account}" is sent successfully!'


def view_transaction_history(account, operation):
    """View transactions for an account."""
    if account not in account_holders:
        return f'Error: Account "{account}" does not exist in the system!'
    # history = []
    # for operation in transaction_histories:
    #     history.append(operation)
    index_transaction_history = account_holders.index(account)
    return transaction_histories[index_transaction_history]

def apply_for_loan(account, period, amount, money_to_return):
    """Allow user to apply for a loan."""
    if amount > MAX_LOAN_AMOUNT:
        return f'You are eligible only for maximum amount of {MAX_LOAN_AMOUNT}'

    index_loan = account_holders.index(account)
    loans[index_loan] += amount
    transaction_histories[index_loan].append(f"Loan: {money_to_return:.2f}")
    balances[index_loan] += money_to_return

    return f'You have been accepted for a loan with an amount {amount:.2f}\nYou need to return total of {money_to_return:.2f}'

def repay_loan(account, amount_returned, remaining_loan):
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions

        # Create an account
        if choice == 1:
            username = input("Enter Account-name: ")
            # start_balance = 0
            # start_loan = 0
            print(create_account(username, balance=0, loan=0))

        # Deposit to an account
        elif choice == 2:
            username = input("Enter Account-name: ")
            if username in account_holders:
                deposit_amount = float(input("Enter amount to deposit: "))
                print(deposit(account=username, amount=deposit_amount))
                print(check_balance(account=username, balance=balances))

            else:
                print("Account with this name does not exist in the system.")
                print("Do you want to create an account?")
                option = input("Enter Yes or No: ")


                if option != "Yes":
                    print("Thank You for using our services. Goodbye!")
                    break

                else:
                    print(create_account(username, balance=0, loan=0))


        # Withdraw from an account
        elif choice == 3:
            username = input("Enter Account-name: ")
            withdraw_amount = float(input("Enter amount to withdraw: "))
            print(withdraw(account=username, amount=withdraw_amount))
            print(check_balance(account=username, balance=balances))

        # Check current balance of an account
        elif choice == 4:
            username = input("Enter Account-name: ")
            print(check_balance(account=username, balance=balances))

        # List all accounts
        elif choice == 5:

            all_accounts = account_holders
            all_balances = balances
            all_loans = loans
            print(list_accounts(all_accounts, all_balances, all_loans))

        # Transfer funds from Account A to Account B
        elif choice == 6:
            username = input('From which account: ')
            targeted_account = input("Recipient: ")
            transfer_amount = float(input("Transfer amount: "))
            print(transfer_funds(account=username, target_account=targeted_account, amount=transfer_amount))
            print(check_balance(account=username, balance=balances))

        # View transaction history of an account
        elif choice == 7:
            username = input("Enter username: ")
            print(view_transaction_history(account=username, operation=transaction_histories))

        # Apply for loan main logic
        elif choice == 8:
            username = input("Enter Account name: ")
            loan_amount = float(input("Enter desired amount: "))
            loan_period = int(input("Enter a period for returning the loan: "))
            return_money = loan_amount * (INTEREST_RATE * loan_period) + loan_amount
            print(apply_for_loan(account=username, amount=loan_amount, period=loan_period, money_to_return=return_money))

        # Repay loan main logic
        elif choice == 9:
            repay_loan()

        # Identify bank cars main logic
        elif choice == 10:
            identify_card_type()


        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()