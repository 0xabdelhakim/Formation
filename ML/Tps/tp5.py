# Week 5: Visualization Basics
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load and explore
df = sns.load_dataset('penguins')
print(df.head())
print("\nMissing:\n", df.isnull().sum())

# Univariate: histogram
plt.figure(figsize=(8, 5))
sns.histplot(df['bill_length_mm'], kde=True)
plt.title('Distribution of Penguin Bill Length')
plt.show()

# Bivariate: scatter
sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title('Bill Dimensions by Species')
plt.show()

# Correlation heatmap (numerical only)
num_df = df.select_dtypes(include='float')
sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()

# Exercise: Boxplot for body mass by island