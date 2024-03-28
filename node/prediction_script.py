# prediction_script.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import sys

# Load the data
file_path = sys.argv[1]
sales_data = pd.read_csv(file_path)

# Assume the data has columns like 'sales_amount', 'product_demand_level', etc.

# Train a simple linear regression model
model = LinearRegression()
model.fit(sales_data[['sales_amount', 'product_demand_level']],
          sales_data['sales_commission'])

# Make predictions
new_sales_data = pd.DataFrame(
    {'sales_amount': [1500, 2000], 'product_demand_level': [2, 3]})
predicted_commissions = model.predict(new_sales_data)

# Print predictions to stdout
for pred in predicted_commissions:
    print(pred)
