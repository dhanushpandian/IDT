from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import io
import socket

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('sales_model.joblib')

# Function to process uploaded file and make predictions


def process_file(file):
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(file)

    # Make predictions using the loaded model
    df['predicted_sales_commission'] = model.predict(
        df[['sales_amount', 'product_demand_level']])

    return df

# Endpoint to handle file upload and return predictions


@app.route('/predict', methods=['POST'])
def predict():
    # Check if file is present in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    # Check if the file is a CSV file
    if file.filename.endswith('.csv'):
        # Process the file and make predictions
        df = process_file(io.StringIO(file.stream.read().decode('utf-8')))

        # Convert DataFrame to JSON
        result = df.to_dict(orient='records')
        print(result)

        return jsonify(result)
    else:
        return jsonify({'error': 'Unsupported file format'})

# Render the HTML form for file upload


@app.route('/')
def index():
    return render_template('front.html')  # Render front.html template


# if __name__ == '__main__':
#     # Get the host IP address dynamically
#     host_ip = socket.gethostbyname(socket.gethostname())
#     # Run the Flask app
#     app.run(debug=True, host=host_ip)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
