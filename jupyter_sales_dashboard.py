
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable interactive plots in Jupyter Notebook
%matplotlib inline

# Sample dataset
data = pd.DataFrame({
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06"],
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product B", "Product A"],
    "Sales": [1000, 1200, 800, 900, 1100, 1300]
})

# Simulate user-selected filters
region_filter = ["North", "South"]  # Replace with desired regions
product_filter = ["Product A", "Product B"]  # Replace with desired products

# Apply filters
filtered_data = data[
    (data["Region"].isin(region_filter)) & 
    (data["Product"].isin(product_filter))
]

# Display filtered data
print("Filtered Data:")
print(filtered_data)

# Visualize Sales by Region
region_sales = filtered_data.groupby("Region")["Sales"].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Sales", data=region_sales)
plt.title("Sales by Region")
plt.show()

# Visualize Sales by Product
product_sales = filtered_data.groupby("Product")["Sales"].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Sales", data=product_sales)
plt.title("Sales by Product")
plt.show()
