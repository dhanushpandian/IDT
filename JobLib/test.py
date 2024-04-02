import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Load the training data
sales_data = pd.read_csv('sales_data.csv')

# Split features and target variable
X = sales_data[['sales_amount', 'product_demand_level']]
y = sales_data['sales_commission']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create a pipeline with preprocessing and model
model = make_pipeline(StandardScaler(), LinearRegression())

# Evaluate the model using cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print("Cross-validation scores:", cv_scores)
print("Average cross-validation score:", cv_scores.mean())

# Train the model on the entire training set
model.fit(X_train, y_train)

# Save the trained model to disk
joblib.dump(model, 'sales_model.joblib')

# Generate predictions on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Plot predictions vs. actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('Actual Sales Commission')
plt.ylabel('Predicted Sales Commission')
plt.title('Actual vs. Predicted Sales Commission')
plt.grid(True)
plt.show()

# Plot residuals
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals)
plt.xlabel('Predicted Sales Commission')
plt.ylabel('Residuals')
plt.title('Residuals vs. Predicted Sales Commission')
plt.axhline(y=0, color='r', linestyle='--')
plt.grid(True)
plt.show()

# Print evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)
