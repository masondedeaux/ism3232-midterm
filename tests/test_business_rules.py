from business_rules import calculate_food_cost, get_event_discount


def test_food_cost_regular_event():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_food_cost_with_cents():
    assert round(calculate_food_cost(19.99, 3), 2) == 59.97


def test_discount_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_discount_at_25_guests():
    assert get_event_discount(25) == 0.05
