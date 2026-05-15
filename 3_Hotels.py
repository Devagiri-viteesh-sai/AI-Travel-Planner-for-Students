import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

hotels = pd.read_csv(BASE_DIR / "data" / "hotels.csv")

st.title("🏨 Budget Friendly Hotels")

city = st.selectbox(
    "Select City",
    sorted(hotels["City"].unique())
)

filtered_hotels = hotels[hotels["City"] == city]

st.dataframe(filtered_hotels)