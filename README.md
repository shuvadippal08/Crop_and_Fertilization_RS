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

## 🗂️ Project Structure </br>
├── Crop_RS.ipynb # Jupyter notebook for crop model training </br>
├── fertilizer.ipynb # Jupyter notebook for fertilizer model training </br>
├── app.py # Flask backend script </br>
├── templates/ </br>
│ └── index.html # Web interface for user input </br>
├── model.pkl # Trained crop model </br>
├── standardscalar.pkl # StandardScaler for crop model </br>
├── minmaxscalar.pkl # MinMaxScaler for crop model </br>
├── fertilizer_model.pkl # Trained fertilizer model </br>
├── fertilizer_standardscalar.pkl# StandardScaler for fertilizer model </br>
├── fertilizer_minmaxscalar.pkl # MinMaxScaler for fertilizer model </br>
└── README.md # Project documentation </br>



## 🏗️ How to Run Locally

1. **Clone the repository**
bash
git clone [https://github.com/your-username/crop-fertilizer-recommendation.git](https://github.com/shuvadippal08/Crop_and_Fertilization_RS)
cd crop-fertilizer-recommendation


2. **Install Dependencies**
3.  **Run The Flask App**
4.  **Open in Browser**

##📊 ML Model Details
<b>Crop Recommendation Model</b><br>
Input Features: N, P, K, Temperature, Humidity, pH, Rainfall<br>

Algorithm Used: [Specify model, e.g., Random Forest]<br>

Preprocessing: MinMaxScaler → StandardScaler</br>
Accuracy -> 99.3% <br/>
<b>Fertilizer Recommendation Model</b>
Input Features: N, P, K, Temperature, Humidity, Moisture, Soil Type, Crop Type</br>

Algorithm Used: [Specify model, e.g., Random Forest Classifier ]</br>

Preprocessing: MinMaxScaler → StandardScaler</br>
Accuracy -> 95%
