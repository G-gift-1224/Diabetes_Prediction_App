# Diabetes_Prediction_App
Diabetes_Prediction
Perfect Puji 👏 I updated your README content based on:

# 🩺 Diabetes Prediction App

A Machine Learning web application that predicts whether a person is likely to have diabetes based on health and medical attributes.

This project uses a **Decision Tree Classifier** and is deployed using **Streamlit**.


## 📌 Project Overview

Diabetes is a chronic disease that requires early detection for better treatment and prevention.

This application allows users to input health-related information and predicts whether the person is:

* ✅ Diabetic
* ❌ Non-Diabetic


## 📊 Dataset Features (Columns Used)

The model is trained using the following features:

* `gender`
* `age`
* `hypertension`
* `heart_disease`
* `smoking_history`
* `bmi`
* `HbA1c_level`
* `blood_glucose_level`

Target Variable:

* `diabetes`


## 🧠 Machine Learning Model

* Algorithm Used: **Decision Tree Classifier**
* Dataset: Diabetes Prediction Dataset
* Model File: `model.pkl`
* Language: Python

### Why Decision Tree?

* Easy to understand and interpret
* Handles both numerical and categorical data
* Good performance for classification problems
* No need for feature scaling

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Git & GitHub


## 📂 Project Structure

diabetes_prediction_app/
│
├── app.py                # Streamlit web app
├── model.pkl             # Trained Decision Tree model
├── diabetes_prediction_dataset.csv
├── requirements.txt
└── README.md

## ⚙️ Project Workflow

1. Data Collection
2. Data Preprocessing
3. Encoding Categorical Variables
4. Train-Test Split
5. Model Training (Decision Tree)
6. Model Evaluation
7. Model Saving using Pickle
8. Deployment using Streamlit

##  How to Run the Project Locally

### 1️ Clone the Repository

git clone https://github.com/your-username/diabetes_prediction_app.git

### 2️ Navigate to the Project Folder

cd diabetes_prediction_app

### 3️ Install Required Libraries

pip install -r requirements.txt

### 4️ Run the Streamlit App
streamlit run app.py

The application will open in your browser.

## ✨ Features

✔ Interactive Web Interface
✔ Real-Time Prediction
✔ Decision Tree Model
✔ Beginner-Friendly ML Project
✔ Clean and Simple UI

## 🎯 Future Improvements

* Add model accuracy score display
* Add confusion matrix visualization
* Hyperparameter tuning for better accuracy
* Deploy on Streamlit Cloud
* Improve UI design


## 👩‍💻 Author

Pujitha Govindu
Aspiring Data Scientist | Machine Learning Enthusiast


