### **🌟 Bank Account Management System 🌟**

![12291285_Startup-managers-presenting-and-analyzing-sales-growth-chart-1024x683](https://github.com/user-attachments/assets/e0329bcc-619e-4cc0-8ae8-e09d5e32da3d)

#### **🎯 Learning Goals**
1. **Understand Core Programming Concepts**: Functions, loops, conditional statements, and lists.
2. **Work with Python for Real-Life Applications**: Simulate a bank management system with real-world features.
3. **Learn Modular Programming**: Design reusable and well-structured code.
4. **Enhance Debugging Skills**: Test each function using various edge cases.
5. **Version Control and Collaboration**: Use GitHub for submission, version tracking, and feedback.
6. **Critical Thinking**: Implement a credit card type checker and integrate it with other features.



### **📜 Step-by-Step Instructions**

#### **1️⃣ Features**
1. **Create a Bank Account**
   - Prompt user for account name.
   - Add account with `0` balance and initialize a loan amount to `0`.

2. **Deposit Money**
   - Verify the account exists.
   - Update the balance and log the transaction.

3. **Withdraw Money**
   - Ensure sufficient balance exists for the withdrawal.
   - Update the balance and log the transaction.

4. **Check Balance**
   - Display the account's current balance.

5. **List All Accounts**
   - List account holders with their balance and loan details.

6. **Transfer Funds**
   - Allow money transfers between accounts if sufficient balance exists.

7. **Transaction History**
   - View all past transactions for an account.

8. **Apply for a Loan**
   - Allow loan applications up to `MAX_LOAN_AMOUNT` and calculate interest.

9. **Repay a Loan**
   - Deduct loan amounts from balance upon repayment.

10. **Identify Credit Card Type**
    - Check if the card is Visa, Mastercard, or another type based on number prefixes.

11. **Exit the System**
    - Terminate the program gracefully.

---

#### **2️⃣ Credit Card Type Identification 💳**

Added a new functionality to identify credit card types based on the card number.


📌 Implementation Steps:

Created a new function: identify_card_type(),
which prompts the user to input their card number
and identify the type of the card as stated here:

Visa: Card number starts with 4 (e.g., 4123...).
MasterCard: Card number starts with numbers between 51 and 55 (e.g., 5123...).
American Express: Card number starts with 34 or 37 (e.g., 3712...).
Other: If the card number doesn’t match the above patterns.


