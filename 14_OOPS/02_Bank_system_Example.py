# need to create a class to hold bank system

class BankAccount:
    # Constructor
    def __init__(self , name , balance = 0):
        self.name = name
        self.balance = balance
    # Instance method to deposit money
    def deposit(self , amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    # Instance method to withdraw money
    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    # Instance method to check balance
    def check_balance(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")


# creating an object
print("Welcome to Anslone Banks")
print("*"*20)

ask = input("Do you want to create an account? (yes/no): ").lower()
if ask == "yes":
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    account1 = BankAccount(name, initial_deposit)
else:
    print("Thank you for visiting Anslone Banks")
    exit()

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)
    elif choice == "3":
        account1.check_balance()
    elif choice == "4":
        print("Thank you for using Anslone Banks")
        break
    else:
        print("Invalid choice. Please try again.")
        