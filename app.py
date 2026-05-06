import streamlit as st
import joblib
import os

# Page config
st.set_page_config(page_title="Rainfall Prediction", layout="centered")

# Title
st.markdown("<h1>🌧️ Rainfall Prediction System</h1>", unsafe_allow_html=True)
st.markdown("### Enter weather details below:")

# ✅ Load saved model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# 🎨 UI Layout
col1, col2 = st.columns(2)

with col1:
    min_temp = st.number_input("🌡️ Min Temperature", value=10.0, placeholder="Enter value in Celsius", help="Enter value in Celsius")
    st.caption("Enter value in Celsius")
    if min_temp is not None and (min_temp > 60 or min_temp < -50):
        st.warning("⚠️ Unrealistic temperature value.")

    humidity9 = st.number_input("💧 Humidity 9am", value=50.0, placeholder="Range: 0–100%", help="Range: 0–100%")
    st.caption("Range: 0–100%")
    if humidity9 is not None and (humidity9 > 100 or humidity9 < 0):
        st.warning("⚠️ Humidity must be between 0 and 100.")

    pressure9 = st.number_input("🌡️ Pressure 9am", value=1010.0, placeholder="Typical range: 980–1050 hPa", help="Typical range: 980–1050 hPa")
    st.caption("Typical range: 980–1050 hPa")
    if pressure9 is not None and (pressure9 < 900 or pressure9 > 1100):
        st.warning("⚠️ Unusual pressure value.")

    wind9 = st.number_input("🌬️ Wind Speed 9am", value=10.0, placeholder="Enter speed in km/h", help="Enter speed in km/h")
    st.caption("Enter speed in km/h")
    if wind9 is not None and (wind9 < 0 or wind9 > 200):
        st.warning("⚠️ Unrealistic wind speed.")

with col2:
    max_temp = st.number_input("🌡️ Max Temperature", value=25.0, placeholder="Enter value in Celsius", help="Enter value in Celsius")
    st.caption("Enter value in Celsius")
    if max_temp is not None and (max_temp > 60 or max_temp < -50):
        st.warning("⚠️ Unrealistic temperature value.")

    humidity3 = st.number_input("💧 Humidity 3pm", value=50.0, placeholder="Range: 0–100%", help="Range: 0–100%")
    st.caption("Range: 0–100%")
    if humidity3 is not None and (humidity3 > 100 or humidity3 < 0):
        st.warning("⚠️ Humidity must be between 0 and 100.")

    pressure3 = st.number_input("🌡️ Pressure 3pm", value=1010.0, placeholder="Typical range: 980–1050 hPa", help="Typical range: 980–1050 hPa")
    st.caption("Typical range: 980–1050 hPa")
    if pressure3 is not None and (pressure3 < 900 or pressure3 > 1100):
        st.warning("⚠️ Unusual pressure value.")

    wind3 = st.number_input("🌬️ Wind Speed 3pm", value=10.0, placeholder="Enter speed in km/h", help="Enter speed in km/h")
    st.caption("Enter speed in km/h")
    if wind3 is not None and (wind3 < 0 or wind3 > 200):
        st.warning("⚠️ Unrealistic wind speed.")

# 🔍 Prediction
if st.button("🔍 Predict Rainfall"):

    input_data = [[min_temp, max_temp, humidity9, humidity3,
                   pressure9, pressure3, wind9, wind3]]

    # Get class prediction and probability
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0]
    
    # In scikit-learn random forest, class 0 is 'No' (Index 0), class 1 is 'Yes' (Index 1)
    rain_prob = probability[1] * 100

    if prediction[0] == 1:
        st.error("🌧️ Rain Expected Tomorrow")
    else:
        st.success("☀️ No Rain Tomorrow")

    # Show confidence score
    st.markdown("### Model Confidence (Probability of Rain)")
    st.progress(int(rain_prob), text=f"{rain_prob:.1f}% Chance of Rain")

    # Smart Weather Tips
    st.markdown("---")
    st.markdown("#### 💡 Weather Tip:")
    if rain_prob > 70:
        st.warning("High chance of rain! ☔ Don't forget your umbrella.")
    elif rain_prob > 40:
        st.info("Moderate chance of rain. ☁️ You might want to carry a light jacket.")
    else:
        st.success("Clear skies expected! ☀️ Perfect weather for outdoor activities.")

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

/* Input boxes - Glassmorphism */
div[data-baseweb="input"] {
    background-color: rgba(31, 42, 64, 0.4) !important;
    border-radius: 10px !important;
    padding: 5px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    position: relative;
}

/* Hover/Focus Glow Effects */
div[data-baseweb="input"]:focus-within, div[data-baseweb="input"]:hover {
    box-shadow: 0 0 12px rgba(0, 198, 255, 0.4);
    border-color: rgba(0, 198, 255, 0.5);
    background-color: rgba(31, 42, 64, 0.6) !important;
}

/* Unit Badges inside input */
div[data-baseweb="input"]::after {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: #a0aec0;
    font-size: 14px;
    pointer-events: none;
    font-weight: 600;
    z-index: 2;
}

div[data-baseweb="input"]:has(input[aria-label*="Temperature"])::after {
    content: "°C";
    right: 65px;
}

div[data-baseweb="input"]:has(input[aria-label*="Humidity"])::after {
    content: "%";
    right: 65px;
}

div[data-baseweb="input"]:has(input[aria-label*="Pressure"])::after {
    content: "hPa";
    right: 65px;
}

div[data-baseweb="input"]:has(input[aria-label*="Wind"])::after {
    content: "km/h";
    right: 65px;
}

/* Adjust padding so text doesn't overlap units */
input[type="number"] {
    padding-right: 45px !important;
}

/* Labels */
label {
    color: #ffffff !important;
    font-size: 16px;
    font-weight: 500;
}

/* Helper Text styling */
div[data-testid="stCaptionContainer"] {
    margin-top: -15px;
    margin-bottom: 10px;
    color: #a0aec0 !important;
    font-style: italic;
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
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0, 114, 255, 0.3);
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background: linear-gradient(to right, #0072ff, #00c6ff);
    box-shadow: 0 6px 20px rgba(0, 114, 255, 0.5);
    transform: translateY(-2px);
}

/* Result messages */
.stAlert {
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    h1 { font-size: 32px; }
}
</style>
""", unsafe_allow_html=True)