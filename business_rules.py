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


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return the event total after discounts and any service fee."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    total = food_cost * (1 - discount)
    if total <= SERVICE_FEE_LIMIT:
        total += SERVICE_FEE
    return total


def needs_signoff(total: float) -> bool:
    """Return whether the event needs a manager's sign-off."""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Return whether the event needs a second chef."""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Return the combined total for all events."""
    total = 0.0
    for event in events:
        total += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return total


def largest_event(events: list) -> str:
    """Return the client with the highest event total."""
    largest_client = ""
    largest_total = None
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if largest_total is None or total > largest_total:
            largest_total = total
            largest_client = event["client"]
    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return one formatted event report line."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )
