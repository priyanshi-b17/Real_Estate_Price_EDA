import pandas as pd

# Load the selected Excel file
file_path = '/content/Real estate valuation data set.xlsx'
real_estate_df = pd.read_excel(file_path)

# Display basic information and the first few rows
print(real_estate_df.info())
display(real_estate_df.head())
# 1. find avg,median,max,min of house prices per unit area
avg_price = real_estate_df['Y house price of unit area'].mean()
print(f"Average House Price per Unit Area: ${avg_price:.2f}")
median_price = real_estate_df['Y house price of unit area'].median()
print(f"Median House Price per Unit Area: ${median_price:.2f}")
max_price = real_estate_df['Y house price of unit area'].max()
print(f"Maximum House Price per Unit Area: ${max_price:.2f}")
min_price = real_estate_df['Y house price of unit area'].min()
print(f"Minimum House Price per Unit Area: ${min_price:.2f}")
# 2.find the avg house age
avg_age = real_estate_df['X1 transaction date'].mean()
print(f"Average House Age: {avg_age:.2f} years")
# 3. Compare the average price for properties near vs far from MRT stations using a chosen threshold (e.g., 500m)
threshold_mrt = 500.0

near_mrt = real_estate_df[real_estate_df['X3 distance to the nearest MRT station'] <= threshold_mrt]
far_mrt = real_estate_df[real_estate_df['X3 distance to the nearest MRT station'] > threshold_mrt]

avg_price_near = near_mrt['Y house price of unit area'].mean()
avg_price_far = far_mrt['Y house price of unit area'].mean()

print(f"Average price for properties NEAR MRT (<= {threshold_mrt}m): ${avg_price_near:.2f} per unit area (Count: {len(near_mrt)})")
print(f"Average price for properties FAR from MRT (> {threshold_mrt}m): ${avg_price_far:.2f} per unit area (Count: {len(far_mrt)})")
# 4.find different avg price grouped by the number of convenience stores
avg_price_by_stores = real_estate_df.groupby('X4 number of convenience stores')['Y house price of unit area'].mean()
print("Average House Price by Number of Convenience Stores:")
print(avg_price_by_stores)
# 5 .Display the top 10 most expensive properties with styled formatting
display(top_10_expensive[['No', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'Y house price of unit area']])
# 6.Check for missing values and duplicates. Use NumPy and Pandas only; make a
#price histogram and a scatter plot of MRT distance against price. Write 3
#observations without claiming causation. Common requirements: use Python, NumPy
# and Pandas; load the dataset; display head(), tail(), shape, info() and
#describe(); check missing values and duplicates; use at least one NumPy array
# for calculations; use Pandas filtering, sorting, value_counts() and groupby()
# where relevant; create 2 simple charts; write 3 observations. This is basic
#EDA only-no machine learning.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Structure Exploration
print("=== Dataset Head ===")
display(real_estate_df.head())

print("\n=== Dataset Tail ===")
display(real_estate_df.tail())

print(f"\nDataset Shape: {real_estate_df.shape}")

print("\n=== Dataset Info ===")
real_estate_df.info()

print("\n=== Dataset Description ===")
display(real_estate_df.describe())

# 2. Check for Missing Values & Duplicates
missing = real_estate_df.isnull().sum()
print("\n=== Missing Values ===")
print(missing)

duplicates = real_estate_df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# 3. NumPy Array Calculation (computing price variance and standard deviation)
prices_array = np.array(real_estate_df['Y house price of unit area'])
price_mean = np.mean(prices_array)
price_variance = np.var(prices_array)
price_std = np.std(prices_array)
print(f"\n[NumPy Analysis] Mean Price: {price_mean:.2f}, Variance: {price_variance:.2f}, Std Dev: {price_std:.2f}")

# 4. Pandas filtering, sorting, value_counts() and groupby() usage
print("\n=== Distribution of Convenience Store Counts ===")
print(real_estate_df['X4 number of convenience stores'].value_counts().sort_index())

# 5. Visualizations (Price Histogram & Scatter Plot)
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Histogram of house prices
axes[0].hist(real_estate_df['Y house price of unit area'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title('Histogram of House Price per Unit Area')
axes[0].set_xlabel('Price per Unit Area')
axes[0].set_ylabel('Frequency')
axes[0].grid(True, linestyle='--', alpha=0.5)

# Scatter Plot: MRT Distance vs Price
axes[1].scatter(real_estate_df['X3 distance to the nearest MRT station'],
                real_estate_df['Y house price of unit area'], color='coral', alpha=0.6, edgecolor='k')
axes[1].set_title('MRT Distance vs House Price')
axes[1].set_xlabel('Distance to Nearest MRT Station (m)')
axes[1].set_ylabel('House Price per Unit Area')
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# 6. Observations
print("""
=== Observations ===
1. Distribution of House Prices: The histogram indicates that most property
prices per unit area are clustered between 20 and 50, showing a roughly
right-skewed distribution with a few outliers above 100.
2. MRT Proximity and Prices: The scatter plot reveals that properties closer to
an MRT station (particularly within 500-1000 meters) tend to have higher and
 more varied prices per unit area compared to properties further away.
3. Price Floor for Distant Properties: Properties located further than 2000
meters from the nearest MRT station consistently showcase lower prices, mostly
concentrated below 30 per unit area.
""")




