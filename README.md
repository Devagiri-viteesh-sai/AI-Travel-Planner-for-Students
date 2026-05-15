# ✈️ AI Travel Planner for Students

AI Travel Planner for Students is a Streamlit-based web application that helps students plan affordable and smart trips across India.

The application provides:
- Budget estimation
- Tourist attraction recommendations
- Budget-friendly hotel suggestions
- Personalized travel itineraries
- Multi-city travel planning
- Flexible trip duration selection

---

# 📌 Features

## 🧳 Travel Planning
- Select cities across India
- Choose number of travel days
- Generate travel itineraries

## 💰 Budget Estimation
- Hotel cost calculation
- Food expense estimation
- Transport cost estimation
- Total budget analysis

## 🏨 Budget-Friendly Hotels
- City-wise hotel recommendations
- Price per night
- Hotel ratings

## 📍 Tourist Attractions
- Attraction recommendations
- Entry fees
- Attraction descriptions
- Best visiting times

## 🤖 AI Itinerary Generator
- Budget travel plans
- Comfort travel plans
- Adventure travel plans

## 🗂 Multi-Page Streamlit Application
- Home Page
- Travel Planner
- Hotel Recommendations
- Tourist Attractions

---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- SQLite
- Pillow

---

# 📁 Project Structure

```text
AI_Travel_Planner/
│
├── venv/
│
├── app.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   ├── banner.jpg
│   └── logo.png
│
├── data/
│   ├── indian_cities.csv
│   ├── hotels.csv
│   ├── attractions.csv
│
├── modules/
│   ├── budget_calculator.py
│   ├── hotel_service.py
│   ├── recommendation_engine.py
│   └── itinerary_generator.py
│
├── database/
│   ├── init_db.py
│   └── trips.db
│
└── pages/
    ├── 1_Home.py
    ├── 2_Travel_Planner.py
    ├── 3_Hotels.py
    └── 4_Recommendations.py
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2. Open Project Folder

```bash
cd AI_Travel_Planner
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🗄 Create Database

Run this once:

```bash
python database/init_db.py
```

---

# 📊 Datasets Included

## indian_cities.csv
Contains:
- Indian cities
- Hotel budgets
- Food costs
- Transport costs
- Tourist places

## hotels.csv
Contains:
- Budget hotels
- Ratings
- Price per night

## attractions.csv
Contains:
- Tourist attractions
- Entry fees
- Best visiting times
- Descriptions

---

# 🚀 Future Improvements

The current version is dataset-based.

Future upgrades can include:

- Google Maps API
- OpenWeather API
- AI chatbot integration
- Authentication system
- Live hotel booking
- Route optimization
- PDF itinerary export
- User accounts
- Saved trips
- Recommendation system using Machine Learning

---

# 📷 Screenshots

Add screenshots of:
- Home Page
- Travel Planner
- Hotels Page
- Attractions Page

---

# 👨‍💻 Author

Developed by:
D. Viteesh Sai

---

# 📄 License

This project is for educational and learning purposes.