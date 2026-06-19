import pandas as pd

# Load CSV dataset
df = pd.read_csv("sales_data.csv")

print("\n===== DATASET =====")
print(df)

# Inspect dataset
print("\n===== DATA INFORMATION =====")
print(df.info())

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Filter data
electronics = df[df["Category"] == "Electronics"]

print("\n===== ELECTRONICS PRODUCTS =====")
print(electronics)

# Grouping and aggregation
category_sales = df.groupby("Category")["Sales"].sum()

print("\n===== TOTAL SALES BY CATEGORY =====")
print(category_sales)

# Highest sales product
highest = df.loc[df["Sales"].idxmax()]

print("\n===== HIGHEST SALES PRODUCT =====")
print(highest)

# Insights
print("\n===== INSIGHTS =====")
print("1. Electronics category generated the highest sales.")
print("2. Laptop is the best-selling product.")
print("3. Education category generated the lowest sales.")