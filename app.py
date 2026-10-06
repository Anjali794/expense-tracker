expenses = []


def add_expense(description, amount):
    if not description.strip():
        raise ValueError("Description cannot be empty")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    return expense


def get_expenses():
    return expenses


def get_total():
    return sum(expense["amount"] for expense in expenses)