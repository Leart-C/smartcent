print("Welcome to SmartCent!")

name = input("What is your name? ")
print("Hello,", name)

while True:
    try:
        income_text = input("Enter income: ")
        income = int(income_text)
        break
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")

while True:
    try:
        expenses_text = input("Enter expenses: ")
        expenses = int(expenses_text)
        break
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")

balance = income - expenses

print("Income:", income)
print("Expenses:", expenses)
print("Balance:", balance)
