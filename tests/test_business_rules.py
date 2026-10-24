from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
    needs_second_chef,
    needs_signoff,
)


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


def test_service_fee_at_500():
    assert round(calculate_event_total(25.00, 20), 2) == 575.00


def test_no_service_fee_above_500():
    assert round(calculate_event_total(500.01, 1), 2) == 500.01


def test_no_signoff_at_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_above_2500():
    assert needs_signoff(2500.01) is True


def test_no_second_chef_at_80_guests():
    assert needs_second_chef(80, 1000.00) is False


def test_second_chef_above_80_guests():
    assert needs_second_chef(81, 1000.00) is True


def test_no_second_chef_below_3000():
    assert needs_second_chef(50, 2999.99) is False


def test_second_chef_at_3000():
    assert needs_second_chef(50, 3000.00) is True
