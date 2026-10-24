from business_rules import calculate_food_cost


def test_food_cost_regular_event():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_food_cost_with_cents():
    assert round(calculate_food_cost(19.99, 3), 2) == 59.97
