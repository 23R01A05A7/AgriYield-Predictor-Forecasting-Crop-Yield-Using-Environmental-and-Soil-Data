from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Mappings
state_map = {"Karnataka": 0, "Andhra Pradesh": 1, "Tamil Nadu": 2, "Maharashtra": 3}
crop_map = {"Rice": 0, "Wheat": 1, "Sugarcane": 2, "Cotton": 3}
soil_map = {"Loamy": 0, "Sandy": 1, "Clay": 2}
fertilizer_map = {"Urea": 0, "DAP": 1, "Compost": 2}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Get data from form
        state = request.form.get('state')
        crop = request.form.get('crop')
        soil = request.form.get('soil')
        fertilizer = request.form.get('fertilizer')
        
        # Numeric inputs
        n = request.form.get('n')
        p = request.form.get('p')
        k = request.form.get('k')
        ph = request.form.get('ph')
        rainfall = request.form.get('rainfall')
        year = request.form.get('year')

        # Check for missing inputs
        if not all([state, crop, soil, fertilizer, n, p, k, ph, rainfall, year]):
            return render_template('index.html', error="All fields are required.")

        # Encode categorical variables
        state_val = state_map.get(state)
        crop_val = crop_map.get(crop)
        soil_val = soil_map.get(soil)
        fert_val = fertilizer_map.get(fertilizer)

        # Ensure all numeric inputs are float
        features = [
            float(state_val),
            float(crop_val),
            float(soil_val),
            float(fert_val),
            float(n),
            float(p),
            float(k),
            float(ph),
            float(rainfall),
            float(year)
        ]

        # Ensure 2D array input
        input_data = np.array([features])
        
        # Check feature count
        if input_data.shape[1] != 10:
             return render_template('index.html', error=f"Feature mismatch. Expected 10, got {input_data.shape[1]}.")

        # Prediction
        prediction = model.predict(input_data)[0]
        
        # Calculate percentage (max yield assumed to be 60000 kg/acre)
        percentage = (prediction / 60000) * 100
        percentage = max(0, min(100, percentage)) # Clip between 0 and 100

        # Category logic
        if percentage > 75:
            category = "High"
            cat_color = "#28a745"
        elif 40 <= percentage <= 75:
            category = "Medium"
            cat_color = "#ffc107"
        else:
            category = "Low"
            cat_color = "#dc3545"

        return render_template('index.html', 
                             prediction=f"{prediction:.2f}", 
                             percentage=f"{percentage:.2f}", 
                             category=category,
                             cat_color=cat_color)

    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter numbers for numeric fields.")
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
