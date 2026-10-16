def read_whole_number(prompt):
    while True:
        try:
            value_text = input(prompt)
            return int(value_text)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_balance(income, total_expenses):
    return income - total_expenses


def main():
    print("Welcome to SmartCent!")

    name = input("What is your name? ")
    print("Hello,", name)

    income = read_whole_number("Enter income: ")

    expenses = []

    for expense_number in range(1, 4):
        expense = read_whole_number(f"Enter expense {expense_number}:")
        expenses.append(expense)

    total_expenses = sum(expenses)
    balance = calculate_balance(income, total_expenses)

    print("Income:", income)
    print("Expenses:", expenses)
    print("Total expenses:", total_expenses)
    print("Balance:", balance)


if __name__ == "__main__":
    main()
