from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('sales_model.joblib')

# Endpoint to receive input and return predictions


@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the frontend
    data = request.json
    sales_amount = float(data['sales_amount'])  # Convert to float
    product_demand_level = float(
        data['product_demand_level'])  # Convert to float

    # Make prediction using the loaded model
    prediction = model.predict([[sales_amount, product_demand_level]])

    # Return the prediction to the frontend
    print("\n \n Prediction:", prediction[0], end="\n\n")
    return jsonify({'sales_commission': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
