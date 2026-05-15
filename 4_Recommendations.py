import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# LOAD DATA
attractions = pd.read_csv(BASE_DIR / "data" / "attractions.csv")

st.title("📍 Tourist Attractions")

# CITY SELECTION
city = st.selectbox(
    "Select City",
    sorted(attractions["City"].unique())
)

# FILTER CITY DATA
city_places = attractions[
    attractions["City"] == city
]

# DISPLAY CARDS
for index, row in city_places.iterrows():

    with st.container():

        st.subheader(row["Attraction"])

        st.write(f"🏷 Type: {row['Type']}")

        st.write(f"💰 Entry Fee: ₹{row['Entry_Fee']}")

        st.write(f"🕒 Best Time: {row['Best_Time']}")

        st.write(f"📖 Description: {row['Description']}")

        st.markdown("---")
        