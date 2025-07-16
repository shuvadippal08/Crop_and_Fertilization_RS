# 🌾 Crop and Fertilizer Recommendation System

This project is a **web-based intelligent system** that recommends the most suitable **crop** and **fertilizer** based on soil and environmental conditions. Built using **Flask**, it leverages **machine learning models** trained from real agricultural datasets to provide accurate recommendations for farmers and agricultural professionals.

## 🔗 Live Deployment
> 🚀 Hosted on: *[Add your deployment URL here]*

---

## 🧠 Features

- ✅ Crop recommendation based on:
  - Nitrogen (N), Phosphorus (P), Potassium (K)
  - Temperature, Humidity, pH level, Rainfall

- ✅ Fertilizer recommendation based on:
  - NPK levels, Temperature, Humidity, Moisture
  - Soil type, Crop type

- 🧮 Pretrained ML models with scaling (StandardScaler, MinMaxScaler)
- 🌐 User-friendly interface via `Flask` and HTML templates

---

## 🗂️ Project Structure
├── Crop_RS.ipynb # Jupyter notebook for crop model training
├── fertilizer.ipynb # Jupyter notebook for fertilizer model training
├── app.py # Flask backend script
├── templates/
│ └── index.html # Web interface for user input
├── model.pkl # Trained crop model
├── standardscalar.pkl # StandardScaler for crop model
├── minmaxscalar.pkl # MinMaxScaler for crop model
├── fertilizer_model.pkl # Trained fertilizer model
├── fertilizer_standardscalar.pkl# StandardScaler for fertilizer model
├── fertilizer_minmaxscalar.pkl # MinMaxScaler for fertilizer model
└── README.md # Project documentation
