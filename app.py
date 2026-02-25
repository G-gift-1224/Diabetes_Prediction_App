import streamlit as st
import numpy as np
import pickle

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide"
)

# Title Section
st.markdown("<h1 style='text-align: center;'>🩺 Diabetes Prediction System</h1>", unsafe_allow_html=True)
st.markdown("### 🤖 Machine Learning Based Health Risk Analyzer")

st.divider()

# Sidebar
st.sidebar.header("⚙️ Navigation")
page = st.sidebar.radio("Go to", ["📝 Patient Details", "📊 About Model"])

if page == "📝 Patient Details":

    st.subheader("📋 Enter Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("👤 Gender", ["Male", "Female"])
        age = st.number_input("🎂 Age", min_value=1, max_value=120)
        hypertension = st.selectbox("💓 Hypertension", [0, 1])
        heart_disease = st.selectbox("❤️ Heart Disease", [0, 1])
    with col2:
        smoking_history = st.selectbox(
            "🚬 Smoking History",
            ["never", "current", "former", "ever", "not current", "No Info"]
        )
        bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=60.0)
        hba1c = st.number_input("🧪 HbA1c Level", min_value=3.0, max_value=15.0)
        glucose = st.number_input("🩸 Blood Glucose Level", min_value=50, max_value=300)


    st.divider()

    if st.button("🔍 Predict Diabetes"):
        
        # Example dummy prediction logic
        if glucose > 125 and bmi > 30:
            st.error("⚠️ High Risk of Diabetes")
        else:
            st.success("✅ Low Risk of Diabetes")

elif page == "📊 About Model":
    st.subheader("📈 Model Information")
    st.write("""
    - Algorithm Used: Logistic Regression
    - Dataset: PIMA Indians Diabetes Dataset
    - Features Used:
        - Glucose
        - BMI
        - Age
        - Insulin
        - Blood Pressure
    """)