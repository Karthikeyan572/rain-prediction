import streamlit as st
import numpy as np
import pandas as pd
import pickle
from datetime import datetime

# --------------- Model and Encoder Loading ---------------
with open('rain_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# For location encoding (as you used LabelEncoder in your notebook)
location_dict = {
    'Austin': 0, 'Charlotte': 1, 'Chicago': 2, 'Columbus': 3, 'Dallas': 4,
    'Denver': 5, 'Fort Worth': 6, 'Houston': 7, 'Indianapolis': 8, 'Jacksonville': 9,
    'Los Angeles': 10, 'New York': 11, 'Philadelphia': 12, 'Phoenix': 13,
    'San Antonio': 14, 'San Diego': 15, 'San Francisco': 16, 'San Jose': 17,
    'Seattle': 18, 'Washington D.C.': 19
}
locations = list(location_dict.keys())

# --------------- Streamlit Interface ---------------
st.title("Rain Prediction App")

# Calendar picker for Date
date_value = st.date_input("Select the Date", datetime.today())
year = date_value.year
month = date_value.month
day = date_value.day

# Option select for Location
location = st.selectbox("Select the Location", options=locations)
loc_num = location_dict[location]

# Manual continuous value inputs
temperature = st.number_input("Temperature (°F)", min_value=30.0, max_value=100.0, value=65.0)
humidity = st.number_input("Humidity (%)", min_value=20.0, max_value=100.0, value=60.0)
wind_speed = st.number_input("Wind Speed", min_value=0.0, max_value=30.0, value=10.0)
precipitation = st.number_input("Precipitation", min_value=0.0, max_value=3.1, value=0.0)
cloud_cover = st.number_input("Cloud Cover (%)", min_value=10.0, max_value=100.0, value=55.0)
pressure = st.number_input("Pressure", min_value=970.0, max_value=1040.0, value=1005.0)

# Convert Precipitation with cube root as you did in preprocessing
precipitation_trans = np.cbrt(precipitation)

# Predict button
if st.button("Predict Rain Tomorrow"):
    feature = np.array([[
        temperature,
        humidity,
        wind_speed,
        precipitation_trans,
        cloud_cover,
        pressure,
        year,
        month,
        day,
        loc_num
    ]])
    result = model.predict(feature)[0]

    if result == 1:
        st.success("Prediction: It will RAIN tomorrow.")
    else:
        st.info("Prediction: It will NOT rain tomorrow.")

# Instructions for running:
# Save this as app.py
# Run: streamlit run app.py
