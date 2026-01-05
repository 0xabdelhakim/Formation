# Week 2: Data Manipulation
import pandas as pd
import numpy as np
import seaborn as sns

# Load dataset
df = sns.load_dataset('titanic')

# Exploration first: subset and filter
print("First 5 rows:\n", df.head())
subset = df[df['age'] > 30]  # Filter example
print("\nAdults over 30:\n", subset[['age', 'sex', 'survived']].head())

# Grouping and aggregation
grouped = df.groupby('class')['fare'].agg(['mean', 'median', 'count'])
print("\nFare stats by class:\n", grouped.round(2))

# NumPy array operations
ages = df['age'].dropna().to_numpy()
print("\nMean age (NumPy):", np.mean(ages).round(2))
ages_reshaped = ages.reshape(-1, 1)  # Reshape for potential ML input

# Simple merge (simulate with split and join)
df1 = df[['passenger_id', 'survived']]
df2 = df[['passenger_id', 'age', 'fare']]
merged = pd.merge(df1, df2, on='passenger_id')
print("\nMerged shape:", merged.shape)

# Exercise: Group by 'sex' and compute survival rate