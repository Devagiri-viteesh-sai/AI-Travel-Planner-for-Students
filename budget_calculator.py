def calculate_budget(hotel, food, transport, days):

    hotel_cost = hotel * days
    food_cost = food * days
    transport_cost = transport * days

    # Long stay discounts
    if days > 7:
        hotel_cost *= 0.9

    if days > 15:
        transport_cost *= 0.85

    total = hotel_cost + food_cost + transport_cost

    return int(total)