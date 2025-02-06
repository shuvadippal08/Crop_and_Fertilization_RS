from flask import Flask, request, render_template
import numpy as np
import pickle

# Load models and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standardscalar.pkl', 'rb'))
mx = pickle.load(open('minmaxscalar.pkl', 'rb'))

fertilizer_model = pickle.load(open('fertilizer_model.pkl', 'rb'))
fertilizer_sc = pickle.load(open('fertilizer_standardscalar.pkl', 'rb'))
fertilizer_mx = pickle.load(open('fertilizer_minmaxscalar.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    recommendation_type = request.form.get('recommendation_type')

    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])

    if recommendation_type == 'crop':
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)
        prediction = model.predict(sc_mx_features)

        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
                     7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango",
                     13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean",
                     18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

        result = f"Recommended Crop: {crop_dict.get(prediction[0], 'Unknown Crop')}."

    elif recommendation_type == 'fertilizer':
        moisture = float(request.form['Moisture'])
        soil_type = int(request.form['SoilType'])
        crop_type = int(request.form['CropType'])
        feature_list = [N, P, K, temp, humidity, moisture, soil_type, crop_type]
        single_pred = np.array(feature_list).reshape(1, -1)

        mx_features = fertilizer_mx.transform(single_pred)
        sc_mx_features = fertilizer_sc.transform(mx_features)
        prediction = fertilizer_model.predict(sc_mx_features)

        fertilizer_dict = {1: "Urea", 2: "DAP", 3: "14-35-14", 4: "28-28", 5: "17-17-17", 6: "20-20",7:"10-26-26"}

        result = f"Recommended Fertilizer: {fertilizer_dict.get(prediction[0], 'Unknown Fertilizer')}."

    else:
        result = "Invalid selection. Please choose a recommendation type."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
