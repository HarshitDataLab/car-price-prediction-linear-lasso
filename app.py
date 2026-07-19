import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("car_price_prediction.sav", "rb"))

# Page configuration
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details to predict the selling price.")

# User Inputs
year = st.number_input("Manufacturing Year", min_value=2000, max_value=2026, value=2018)

present_price = st.number_input(
    "Present Price (in Lakhs)",
    min_value=0.0,
    value=5.0,
    format="%.2f"
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Previous Owners",
    [0, 1, 2, 3]
)

# Encode categorical variables
fuel_map = {
    "CNG": 0,
    "Petrol": 1,
    "Diesel": 2
}

seller_map = {
    "Individual": 0,
    "Dealer": 1
}

transmission_map = {
    "Automatic": 0,
    "Manual": 1
}

# Prediction
if st.button("Predict Selling Price"):

    input_data = pd.DataFrame([[
        year,
        present_price,
        kms_driven,
        fuel_map[fuel_type],
        seller_map[seller_type],
        transmission_map[transmission],
        owner
    ]], columns=[
        "Year",
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type",
        "Seller_Type",
        "Transmission",
        "Owner"
    ])

    prediction = model.predict(input_data)

    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")