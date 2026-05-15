import streamlit as st
import pandas as pd
from pathlib import Path

from modules.budget_calculator import calculate_budget
from modules.itinerary_generator import generate_itinerary
from modules.recommendation_engine import recommend_places

BASE_DIR = Path(__file__).resolve().parent.parent

# Load Data
cities = pd.read_csv(BASE_DIR / "data" / "indian_cities.csv")

st.title("🧳 Travel Planner")

# User Inputs
name = st.text_input("Enter Your Name")

city = st.selectbox(
    "Select City",
    sorted(cities["City"].unique())
)

# User can enter any number of days
days = st.number_input(
    "How Many Days Do You Want To Stay?",
    min_value=1,
    max_value=365,
    value=3
)

budget = st.number_input(
    "Enter Your Budget (₹)",
    min_value=1000,
    value=5000
)
travel_style = st.radio(
    "Travel Style",
    ["Budget", "Comfort", "Adventure"]
)

# Get City Data
city_data = cities[cities["City"] == city].iloc[0]

hotel = city_data["Budget_Hotel"]
food = city_data["Food_Per_Day"]
transport = city_data["Transport"]

places = city_data["Places"].split("|")

# Calculate Budget
total_cost = calculate_budget(
    hotel,
    food,
    transport,
    days
)

# Expense Breakdown
st.header("📊 Expense Breakdown")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏨 Hotel", f"₹{hotel * days}")
with col2:
    st.metric("🍽 Food", f"₹{food * days}")

with col3:
    st.metric("🚌 Transport", f"₹{transport * days}")

st.write(f"## Estimated Total Cost: ₹{total_cost}")

# Budget Validation
if budget >= total_cost:

    st.success("✅ Your budget is sufficient")

    st.info(f"Remaining Budget: ₹{budget-total_cost}")

else:

    st.error("❌ Budget insufficient")

    st.warning(f"Need ₹{total_cost-budget} more")

# Places
st.header("📍 Tourist Attractions")

recommended_places = recommend_places(places)

for place in recommended_places:
    st.write(place)

# Itinerary
st.header("🤖 AI Itinerary")

itinerary = generate_itinerary(
    travel_style,
    days
)

for item in itinerary:
    st.info(item)