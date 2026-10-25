from business_rules import (
    calculate_event_total,
    format_event_line,
    needs_second_chef,
    needs_signoff,
)

events = [
    {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
    {"client": "Garden Club", "guest_price": 22.00, "guests": 40, "nonprofit": True},
    {"client": "Hilltop Gym", "guest_price": 30.00, "guests": 120, "nonprofit": False},
    {"client": "Island Pantry", "guest_price": 25.00, "guests": 150, "nonprofit": True},
    {"client": "Juniper Spa", "guest_price": 16.00, "guests": 30, "nonprofit": False},
    {"client": "Kettle Works", "guest_price": 20.00, "guests": 80, "nonprofit": False},
    {"client": "Lumen Labs", "guest_price": 15.00, "guests": 81, "nonprofit": False},
    {"client": "Marlow Gala", "guest_price": 70.00, "guests": 50, "nonprofit": True},
]

print("Harvest Table Catering - Event Report")
for event in events:
    total = calculate_event_total(
        event["guest_price"], event["guests"], event["nonprofit"]
    )
    signoff = needs_signoff(total)
    second_chef = needs_second_chef(event["guests"], total)
    print(format_event_line(event["client"], total, signoff, second_chef))
