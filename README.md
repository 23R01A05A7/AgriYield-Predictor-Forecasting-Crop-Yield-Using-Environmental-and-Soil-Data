🌾 Crop Yield Prediction System
📌 Project Overview

This project is a Machine Learning-based Crop Yield Prediction System that predicts agricultural yield using soil and environmental parameters. It helps users make better farming decisions by providing accurate and approximate yield predictions.

🎯 Objectives
Predict crop yield using machine learning
Provide a user-friendly web interface
Visualize results using graphs and dashboard
Store prediction history
Assist in agricultural decision-making
🛠️ Technologies Used
Python
Flask
Scikit-learn
Pandas & NumPy
HTML, CSS, JavaScript
Chart.js
📊 Dataset Description

The dataset contains agricultural data with 1500+ rows and multiple attributes.

🔹 Features Used:
State
Crop
Soil Type
Fertilizer
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Soil pH
Rainfall (mm)
Year
🎯 Target:
Yield (kg/acre)
⚙️ Methodology
1. Data Preprocessing
Handled missing values
Encoded categorical variables
Selected relevant features
2. Model Training
Used Random Forest Regressor
Train-Test Split (80:20)
Evaluated using:
R² Score
RMSE
3. Model Deployment
Saved model using joblib
Integrated model with Flask backend
4. Web Application
Developed frontend using HTML & CSS
Backend using Flask
Connected UI with ML model
🏗️ System Architecture

User Input → Web UI → Flask Backend → ML Model → Prediction → Output & Graphs

✨ Features
🌾 Crop Yield Prediction
📊 Dashboard Visualization
📈 Graphs (NPK, Yield Trends, Efficiency)
🕒 Prediction History
📉 Percentage-based Output
🎨 Clean UI Design
📊 Output Example
Predicted Yield: 45000 kg/acre
Efficiency: 75%
Category: High Yield
🚀 How to Run the Project
1. Clone Repository
git clone <your-repo-link>
cd AgriYield-Predictor-Forecasting-Crop-Yield-Using-Environmental-and-Soil-Data
2. Install Requirements
pip install -r requirements.txt
3. Run Application
python app.py
4. Open Browser
http://127.0.0.1:5000/
✅ Advantages
Easy to use
Fast predictions
Helps farmers
Data-driven insights
⚠️ Limitations
Depends on dataset quality
Predictions are approximate
Limited real-time data
🔮 Future Scope
Real-time weather integration
Mobile application
Advanced ML models
More crops and regions
🏁 Conclusion

This project demonstrates the application of machine learning in agriculture. It provides a smart and efficient way to predict crop yield and supports better decision-making through data and visualization.

👨‍💻 Author

MD Ameer
