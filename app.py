import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️"
)

st.title("❤️ Heart Disease Prediction")

st.warning(
    "This app is for educational purposes only and should not be used for real medical diagnosis."
)

st.write("Enter the patient details below to predict heart disease risk.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3],
    help="0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic"
)

trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=250, value=120)

chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG Result",
    [0, 1, 2],
    help="0: Normal, 1: ST-T abnormality, 2: Left ventricular hypertrophy"
)

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=250, value=150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [0, 1, 2],
    help="0: Upsloping, 1: Flat, 2: Downsloping"
)

ca = st.selectbox(
    "Number of Major Vessels Colored by Fluoroscopy",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thalassemia",
    [0, 1, 2, 3]
)

if st.button("Predict"):
    input_data = np.array([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")