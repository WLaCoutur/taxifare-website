import streamlit as st
import requests

st.title("TaxiFare Prediction")

# Champs de saisie pour les paramètres
date_time = st.text_input("Date and Time (YYYY-MM-DD HH:MM:SS)", "2023-10-01 12:00:00")
pickup_long = st.number_input("Pickup Longitude", value=-73.95)
pickup_lat = st.number_input("Pickup Latitude", value=40.75)
dropoff_long = st.number_input("Dropoff Longitude", value=-73.98)
dropoff_lat = st.number_input("Dropoff Latitude", value=40.77)
passengers = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

# URL de l'API (remplace par ton API si tu en as une)
url = 'https://taxifare.lewagon.ai/predict'

if st.button("Get Prediction"):
    # Créer un dictionnaire avec les paramètres
    params = {
        "pickup_datetime": date_time,
        "pickup_longitude": pickup_long,
        "pickup_latitude": pickup_lat,
        "dropoff_longitude": dropoff_long,
        "dropoff_latitude": dropoff_lat,
        "passenger_count": passengers
    }

    # Appeler l'API
    response = requests.get(url, params=params)
    prediction = response.json().get("fare", "Error: No prediction returned")

    # Afficher la prédiction
    st.success(f"Predicted Fare: ${prediction:.2f}")
