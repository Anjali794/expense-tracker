import pytest

from app import add_expense, get_expenses, get_total, expenses


@pytest.fixture(autouse=True)
def clear_expenses():
    expenses.clear()


def test_add_expense():
    expense = add_expense("Lunch", 250)

    assert expense["description"] == "Lunch"
    assert expense["amount"] == 250


def test_get_expenses():
    add_expense("Lunch", 250)
    add_expense("Coffee", 100)

    result = get_expenses()

    assert len(result) == 2


def test_get_total():
    add_expense("Lunch", 250)
    add_expense("Coffee", 100)

    assert get_total() == 350


def test_empty_description():
    with pytest.raises(ValueError):
        add_expense("", 100)


def test_invalid_amount():
    with pytest.raises(ValueError):
        add_expense("Lunch", 0)