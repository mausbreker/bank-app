class Bank:
    
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def transaction_log(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\t Balance: {self.balance}\n")

    def withdrawal(self, amount):        
        try:
            amount = float(amount)
        except:
            amount = 0
        self.balance = self.balance - amount
        self.transaction_log(f"Withdrew {amount}")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except:
            amount = 0
        self.balance = self.balance + amount
        self.transaction_log(f"Deposited {amount}")

account = Bank(21.5)
while True:
    try:
        user_input = input("Do you want to deposit or witdraw? ")
        user_input = user_input.lower()
    except KeyboardInterrupt:
        print("\nLeaving ATM")
        break
    if user_input == "deposit":
        d_amount = input("How much would you like to deposit? ")
        account.deposit(d_amount)
        print("You deposited ", d_amount)
        print("Your balance is ", account.balance)
    elif user_input == "withdraw":
        w_amount = input("How much would you like to withdraw? ")
        account.withdrawal(w_amount)
        print("You withdrew ", w_amount)
        print("Your balance is ", account.balance)
    else:
        print("Action not recognized. Try again! ")
