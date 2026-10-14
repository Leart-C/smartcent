from main import calculate_balance


def test_calculate_balance_with_positive_balance():
    result = calculate_balance(5000, 1200)

    assert result == 3800


def test_calculate_balance_with_zero_balance():
    result = calculate_balance(1500, 1500)

    assert result == 0


def test_calculate_balance_with_negative_balance():
    result = calculate_balance(1200, 1700)

    assert result == -500
