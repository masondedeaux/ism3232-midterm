from business_rules import calculate_food_cost, get_event_discount


def test_food_cost_regular_event():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_food_cost_with_cents():
    assert round(calculate_food_cost(19.99, 3), 2) == 59.97


def test_discount_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_nonprofit_discount_below_100_guests():
    assert get_event_discount(99, nonprofit=True) == 0.05


def test_nonprofit_flag_changes_discount():
    assert get_event_discount(100, nonprofit=False) == 0.05
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_nonprofit_below_25_has_no_discount():
    assert get_event_discount(24, nonprofit=True) == 0.0