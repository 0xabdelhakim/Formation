# Week 7: Feature Engineering
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Load and explore
housing = fetch_california_housing(as_frame=True)
df = housing.frame
print(df.head())

# Create new feature: rooms per household
df['rooms_per_household'] = df['AveRooms'] / df['HouseAge']

# Log transform for skewed feature
df['log_population'] = np.log1p(df['Population'])

# Binning: latitude into regions
df['lat_bin'] = pd.cut(df['Latitude'], bins=3, labels=['South', 'Central', 'North'])

# Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['MedInc', 'AveRooms']])
poly_df = pd.DataFrame(poly_features, columns=poly.get_feature_names_out())
df = pd.concat([df, poly_df], axis=1)

print("\nNew features:\n", df.columns[-5:])

# Exercise: Create 'bedrooms_per_room' and visualize