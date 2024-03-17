import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the sales data from a CSV file
sales_data = pd.read_csv("sales_data.csv")

# Assume the sales_data.csv contains columns like 'sales_amount', 'product_demand_level', 'sales_commission', etc.

# Assume 'product_demand_level' is encoded (e.g., 1 for low, 2 for medium, 3 for high)

# Define features (X) and target variable (y)
X = sales_data[['sales_amount', 'product_demand_level']]
y = sales_data['sales_commission']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Example usage:
# Once the model is trained, you can use it to predict sales commissions for new sales data
new_sales_data = pd.DataFrame({'sales_amount': [1500, 2000], 'product_demand_level': [2, 3]})
predicted_commissions = model.predict(new_sales_data)
print("Predicted Commissions:", predicted_commissions)
