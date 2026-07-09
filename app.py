import streamlit as st
import pickle
import numpy as np

# Load Model
with open("heart_attack_random_forest.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Heart Attack Prediction")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", [0,1])
cp = st.selectbox("Chest Pain Type", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Maximum Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Old Peak")
slope = st.selectbox("Slope", [0,1,2])
ca = st.selectbox("CA", [0,1,2,3,4])
thal = st.selectbox("Thal", [0,1,2,3])

if st.button("Predict"):

    data = np.array([[age, sex, cp, trestbps, chol,
                      fbs, restecg, thalach,
                      exang, oldpeak,
                      slope, ca, thal]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Attack")
    else:
        st.success("✅ Low Risk of Heart Attack")
