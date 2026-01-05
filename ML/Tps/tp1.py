# Week 1: ML Introduction and Setup
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Basic inspection (always start with understanding the data)
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

# Summary statistics
print("\nDescriptive stats:\n", df.describe().round(2))

# Quick plot to visualize relationships
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['target'], cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Sepal Dimensions by Class')
plt.colorbar(label='Target Class')
plt.show()
# Exercise: Add a similar scatter plot for petal features