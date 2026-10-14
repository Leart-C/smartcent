from main import calculate_balance


def test_calculate_balance_with_positive_balance():
    result = calculate_balance(5000, 1200)

    assert result == 3800
