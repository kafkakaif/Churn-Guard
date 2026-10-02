# 📡 Churn Guard – Customer Churn Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange?logo=scikitlearn&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit&logoColor=white)
![Data](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)
![Model](https://img.shields.io/badge/Model-Pre--Trained-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</p>

<p align="center">

### *“Predict churn. Understand customers. Improve retention.”*

</p>

---

## 📌 Overview

**Churn Guard** is a machine-learning based customer churn prediction system designed to identify telecom customers who are likely to leave a service.

The system analyzes customer account and billing information and uses a pre-trained machine-learning model to generate a churn prediction and probability score.

The application provides an interactive **Streamlit dashboard** where users can enter customer information and instantly view the prediction.

---

## 🎯 Problem Statement

Customer churn is a major challenge for telecom companies. Losing customers can affect revenue and increase the cost of acquiring new customers.

Traditional methods of identifying customers at risk of leaving often rely on manual analysis.

**Churn Guard** addresses this problem by using machine learning to analyze customer behavior and provide an automated churn prediction.

---

## 💡 Proposed Solution

Churn Guard provides a simple machine-learning based solution that:

1. Collects customer information.
2. Processes the input data.
3. Converts categorical values into model-compatible features.
4. Sends the processed data to a trained ML model.
5. Predicts whether the customer is likely to churn.
6. Calculates the churn probability.
7. Displays the result through an interactive dashboard.

---

## 🧠 How the System Works

```text
                 Customer Details
                       │
                       ▼
              ┌──────────────────┐
              │ Streamlit UI     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Data Processing  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Feature Encoding │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ ML Model         │
              │ churn_model.pkl  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Prediction       │
              └────────┬─────────┘
                       │
              ┌────────┴─────────┐
              ▼                  ▼
        Likely to Stay      High Risk
              │                  │
              └────────┬─────────┘
                       ▼
              Churn Probabilit