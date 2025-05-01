import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('rf_mmi_classifier.pkl')
scaler = joblib.load('scaler_mmi.pkl')

st.set_page_config(page_title="MMI Prediction App", layout="centered")
st.title("🌍 Earthquake MMI Prediction")
st.markdown("Enter earthquake parameters to predict the shaking intensity (MMI).")

# MMI explanation box
with st.expander("📘 About MMI Levels"):
    st.markdown("""
    - **Low (I - III):** Barely felt, not likely to cause damage  
    - **Medium (IV - VI):** Felt by many, may cause minor damage  
    - **High (VII+):** Strong shaking, potential for significant damage
    """)

# Form input
with st.form(key="mmi_form"):
    st.subheader("Earthquake Parameters")
    magnitude = st.number_input("Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    depth = st.number_input("Depth (km)", min_value=0.0, max_value=700.0, value=10.0, step=1.0)
    distance = st.number_input("Distance to epicenter (km)", min_value=0.0, max_value=1000.0, value=50.0, step=1.0)

    submit = st.form_submit_button("Predict MMI")

# Prediction result
if submit:
    input_data = np.array([[magnitude, depth, distance]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.success(f"✅ Predicted MMI: **{prediction}**")

    # Show MMI classification
    if prediction <= 3:
        mmi_class = "Low (I–III)"
    elif 4 <= prediction <= 6:
        mmi_class = "Medium (IV–VI)"
    else:
        mmi_class = "High (VII+)"

    st.info(f"📊 MMI Category: **{mmi_class}**")
