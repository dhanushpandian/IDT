import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the training data
sales_data = pd.read_csv('sales_data.csv')

# Split features and target variable
X = sales_data[['sales_amount', 'product_demand_level']]
y = sales_data['sales_commission']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to disk
joblib.dump(model, 'sales_model.joblib')
