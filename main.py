def read_whole_number(prompt):
    while True:
        try:
            value_text = input(prompt)
            return int(value_text)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_balance(income, expenses):
    return income - expenses


def main():
    print("Welcome to SmartCent!")

    name = input("What is your name? ")
    print("Hello,", name)

    income = read_whole_number("Enter income: ")
    expenses = read_whole_number("Enter expenses: ")

    balance = calculate_balance(income, expenses)

    print("Income:", income)
    print("Expenses:", expenses)
    print("Balance:", balance)


if __name__ == "__main__":
    main()
