import pandas as pd
import numpy as np

# Define parameters for generating data
num_records = 100
min_sales_amount = 1000
max_sales_amount = 5000
min_product_demand_level = 1
max_product_demand_level = 5
commission_rate = 0.02  # 2% commission rate

# Generate random sales data
sales_amounts = np.random.randint(
    min_sales_amount, max_sales_amount + 1, num_records)
product_demand_levels = np.random.randint(
    min_product_demand_level, max_product_demand_level + 1, num_records)

# Calculate sales commissions based on sales amounts and demand levels
sales_commissions = sales_amounts * product_demand_levels * commission_rate

# Create DataFrame
data = pd.DataFrame({
    'sales_amount': sales_amounts,
    'product_demand_level': product_demand_levels,
    'sales_commission': sales_commissions
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('generated_sales_data.csv', index=False)
