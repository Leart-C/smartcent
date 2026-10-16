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

    first_expense = read_whole_number("Enter expense 1: ")
    expenses.append(first_expense)

    second_expense = read_whole_number("Enter expense 2: ")
    expenses.append(second_expense)

    third_expense = read_whole_number("Enter expense 3: ")
    expenses.append(third_expense)

    total_expenses = sum(expenses)
    balance = calculate_balance(income, total_expenses)

    print("Income:", income)
    print("Expenses:", expenses)
    print("Total expenses:", total_expenses)
    print("Balance:", balance)


if __name__ == "__main__":
    main()
