print("Welcome to SmartCent!")

name = input("What is your name? ")
print("Hello,", name)

try:
    income_text = input("Enter income: ")
    income = int(income_text)

    expenses_text = input("Enter expenses: ")
    expenses = int(expenses_text)
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
else:
    balance = income - expenses

    print("Income:", income)
    print("Expenses:", expenses)
    print("Balance:", balance)
