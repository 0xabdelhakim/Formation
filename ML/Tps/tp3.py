# Week 3: Data Preprocessing Fundamentals
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer

# Load and explore
df = sns.load_dataset('titanic').copy()
print("Missing values:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)

# Impute missing ages (group by 'sex' and 'class' for better accuracy)
age_imputer = SimpleImputer(strategy='median')
# But first, explore groups
print("\nMedian age by sex/class:\n", df.groupby(['sex', 'pclass'])['age'].median())
df['age'] = df.groupby(['sex', 'pclass'])['age'].transform('median')  # Group-wise fill

# Handle categorical: convert 'embarked' to category type
df['embarked'] = df['embarked'].astype('category')
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)
print("\nAfter cleaning shape:", df.shape)

# Exercise: Impute 'fare' if any missing, and check types again