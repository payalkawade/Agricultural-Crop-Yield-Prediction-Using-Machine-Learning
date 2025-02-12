from multiprocessing.util import debug
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("data/model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")  # Ensure this file is in the 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting input values from the form
        rainfall = float(request.form['Rainfall_mm'])
        temperature = float(request.form['Temperature_Celsius'])
        fertilizer = 1 if request.form['Fertilizer_Used'].lower() == 'true' else 0
        irrigation = 1 if request.form['Irrigation_Used'].lower() == 'true' else 0
        days_to_harvest = float(request.form['Days_to_Harvest'])

        # One-hot encoding for categorical features
        region = request.form['Region'].lower()
        soil_type = request.form['Soil_Type'].lower()
        crop = request.form['Crop'].lower()
        weather = request.form['Weather_Condition'].lower()

        # Define categories
        region_categories = ['north', 'south', 'west']
        soil_categories = ['clay', 'loam', 'peaty', 'sandy', 'silt']
        crop_categories = ['cotton', 'maize', 'rice', 'soybean', 'wheat']
        weather_categories = ['rainy', 'sunny']

        # Convert categorical values to one-hot encoding
        region_onehot = [1 if region == cat else 0 for cat in region_categories]
        soil_onehot = [1 if soil_type == cat else 0 for cat in soil_categories]
        crop_onehot = [1 if crop == cat else 0 for cat in crop_categories]
        weather_onehot = [1 if weather == cat else 0 for cat in weather_categories]

        # Combine all input features into an array
        input_features = [rainfall, temperature, fertilizer, irrigation, days_to_harvest]
        input_features.extend(region_onehot + soil_onehot + crop_onehot + weather_onehot)

        # Convert to numpy array and reshape for prediction
        final_input = np.array(input_features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(final_input)[0]

        return render_template("index.html", prediction_text=f'Estimated Crop Yield: {prediction:.2f} tons')

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8082)

