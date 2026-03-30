import streamlit as st
import joblib

# Page config
st.set_page_config(page_title="Rainfall Prediction", layout="centered")

# Title
st.markdown("<h1>🌧️ Rainfall Prediction System</h1>", unsafe_allow_html=True)
st.markdown("### Enter weather details below:")

# ✅ Load saved model
model = joblib.load("model.pkl")

# 🎨 UI Layout
col1, col2 = st.columns(2)

with col1:
    min_temp = st.number_input("🌡️ Min Temperature", value=10.0)
    humidity9 = st.number_input("💧 Humidity 9am", value=50.0)
    pressure9 = st.number_input("🌡️ Pressure 9am", value=1010.0)
    wind9 = st.number_input("🌬️ Wind Speed 9am", value=10.0)

with col2:
    max_temp = st.number_input("🌡️ Max Temperature", value=25.0)
    humidity3 = st.number_input("💧 Humidity 3pm", value=50.0)
    pressure3 = st.number_input("🌡️ Pressure 3pm", value=1010.0)
    wind3 = st.number_input("🌬️ Wind Speed 3pm", value=10.0)

# 🔍 Prediction
if st.button("🔍 Predict Rainfall"):

    input_data = [[min_temp, max_temp, humidity9, humidity3,
                   pressure9, pressure3, wind9, wind3]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🌧️ Rain Expected Tomorrow")
    else:
        st.success("☀️ No Rain Tomorrow")
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
}

/* Title */
h1 {
    text-align: center;
    color: white;
    font-size: 45px;
}

/* Input boxes */
div[data-baseweb="input"] {
    background-color: #1f2a40 !important;
    border-radius: 10px !important;
    padding: 5px;
}

/* Labels */
label {
    color: #ffffff !important;
    font-size: 16px;
}

/* Button */
.stButton>button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #0072ff, #00c6ff);
}

/* Result messages */
.stAlert {
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)