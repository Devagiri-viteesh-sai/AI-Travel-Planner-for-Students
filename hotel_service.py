import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_hotels(city):

    hotels = pd.read_csv(BASE_DIR / "data" / "hotels.csv")

    filtered = hotels[hotels["City"] == city]

    return filtered