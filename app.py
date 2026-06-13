
import streamlit as st
import joblib
import numpy as np

model = joblib.load("hotel_model.pkl")

st.title("Hotel ADR Prediction")

lead_time = st.number_input("Lead Time", min_value=0)
weekend = st.number_input("Weekend Nights", min_value=0)
week = st.number_input("Week Nights", min_value=0)
adults = st.number_input("Adults", min_value=1)
cancel = st.number_input("Previous Cancellations", min_value=0)

if st.button("Predict"):
    data = np.array([[lead_time, weekend, week, adults, cancel]])
    prediction = model.predict(data)
    st.success(f"Predicted ADR = {prediction[0]:.2f}")
