# 🌱 Fertilizer Recommendation System Using Machine Learning

A machine learning-based web application that recommends a suitable fertilizer based on soil conditions, crop information, weather conditions, and crop growth stage.

## 📌 Project Overview

The Fertilizer Recommendation System uses machine learning to predict the most suitable fertilizer category for a given set of agricultural conditions.

The system takes soil, crop, and environmental parameters as input and provides a fertilizer recommendation.

## 🎯 Objectives

- Recommend a suitable fertilizer based on input conditions.
- Use machine learning for fertilizer classification.
- Provide a simple and user-friendly web interface.
- Deploy the application as a web-based system.

## 📊 Dataset

The dataset contains **10,000 records** and **14 input features**.

### Input Features

- Soil Type
- Soil pH
- Soil Moisture
- Organic Carbon
- Electrical Conductivity
- Nitrogen Level
- Phosphorus Level
- Potassium Level
- Temperature
- Humidity
- Rainfall
- Crop Type
- Crop Growth Stage
- Season

### Target

`Recommended_Fertilizer`

The system predicts fertilizer categories such as:

- Urea
- DAP
- MOP
- NPK
- SSP
- Compost
- Zinc Sulphate

## 🤖 Machine Learning

Three machine learning algorithms were evaluated:

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The **Decision Tree Classifier** was selected as the final model because it achieved the best accuracy.

**Decision Tree Accuracy: 87.40%**

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS
- GitHub
- Render

## ⚙️ System Workflow

```text
User Input
    ↓
Flask Web Application
    ↓
Data Preprocessing
    ↓
Trained Decision Tree Model
    ↓
Fertilizer Prediction
    ↓
Recommended Fertilizer
## 🌐 Web Application

The application provides an interactive form where users can enter soil, crop, and environmental information.

The trained machine learning model processes the input and displays the recommended fertilizer.

## 🚀 Deployment

The Flask application is deployed using Render.
## 📁 Project Structure

```text
fertilizer-recommendation-system/
│
├── app.py
├── fertilizer_decision_tree.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 👩‍💻 Project

Developed as part of a B.Tech Artificial Intelligence and Data Science academic project.

---

⭐ Fertilizer Recommendation System Using Machine Learning
