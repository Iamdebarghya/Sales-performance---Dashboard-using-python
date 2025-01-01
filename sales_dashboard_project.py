
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("sales_data.csv")

# Dashboard layout
st.title("Sales Performance Dashboard")
st.sidebar.header("Filter Options")

# Filter by Region
regions = st.sidebar.multiselect("Select Region:", options=data["Region"].unique(), default=data["Region"].unique())

# Filter by Product
products = st.sidebar.multiselect("Select Product:", options=data["Product"].unique(), default=data["Product"].unique())

# Apply Filters
filtered_data = data[(data["Region"].isin(regions)) & (data["Product"].isin(products))]

# Display Data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_data.groupby("Region")["Sales"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Region", y="Sales", data=region_sales, ax=ax)
st.pyplot(fig)

# Sales by Product
st.subheader("Sales by Product")
product_sales = filtered_data.groupby("Product")["Sales"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="Product", y="Sales", data=product_sales, ax=ax)
st.pyplot(fig)
