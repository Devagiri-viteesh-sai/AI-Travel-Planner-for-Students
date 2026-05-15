def generate_itinerary(style, days):

    itinerary = []

    for day in range(1, days + 1):

        if style == "Budget":

            plan = f"""
Day {day}
- Use public transportation
- Explore budget attractions
- Eat local street food
- Stay in affordable hostels
"""

        elif style == "Comfort":

            plan = f"""
Day {day}
- Use cab services
- Visit premium attractions
- Explore cafes and malls
- Stay in comfortable hotels
"""

        else:

            plan = f"""
Day {day}
- Try adventure sports
- Visit hidden places
- Experience nightlife
- Explore trekking locations
"""

        itinerary.append(plan)

    return itinerary