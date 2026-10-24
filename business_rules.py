GROUP_DISCOUNT_GUESTS = 25
NONPROFIT_DISCOUNT_GUESTS = 100
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
SERVICE_FEE = 75.00
SERVICE_FEE_LIMIT = 500.00
SIGNOFF_LIMIT = 2500.00
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Return the food cost before discounts."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate for the event."""
    discount = 0.0
    if guests >= GROUP_DISCOUNT_GUESTS:
        discount = STANDARD_DISCOUNT
    if guests >= NONPROFIT_DISCOUNT_GUESTS and nonprofit:
        discount = NONPROFIT_DISCOUNT
    return discount
