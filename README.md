# ML Deployment Project

## Overview
This project is a **Flask-based machine learning deployment** that predicts outcomes based on user inputs. The application takes input features such as Rainfall, Temperature, Fertilizer usage, Irrigation, Days to Harvest, Region, Soil Type, and Crop type to make predictions using a trained machine learning model.

## Features
- Web interface for user input.
- Machine learning model loaded from a **pickle file** (`model.pkl`).
- Input data processing including **one-hot encoding** for categorical values.
- Prediction results displayed on a webpage.
- Includes a **Jupyter Notebook (`Agriculture_Crop_Yield.ipynb`)** for data exploration, preprocessing, and model training.

## Installation
### **1. Clone the Repository**
```bash
git clone <repository_url>
cd ML-Deployement_Project
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/`.


## API Endpoints
- `/` → Renders the homepage (HTML form for input).
- `/predict` → Accepts user input via **POST** request and returns predictions.

## Jupyter Notebook (`Agriculture_Crop_Yield.ipynb`)
This notebook provides:
- Data loading and exploration (`crop_yield.csv`).
- Data preprocessing (handling missing values, duplicates, feature engineering).
- Model training and evaluation.
- Saving the trained model as a `model.pkl` file for deployment.

## Future Enhancements
- Add error handling for invalid inputs.
- Improve the user interface.
- Deploy to cloud platforms like AWS/GCP/Heroku.


