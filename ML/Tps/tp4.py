# Week 4: Advanced Preprocessing
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Load and split first (avoid leakage)
df = sns.load_dataset('titanic')
X = df.drop('survived', axis=1)
y = df['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define transformers
num_features = ['age', 'fare']
cat_features = ['sex', 'embarked']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_features)
    ])

# Fit on train only
X_train_prep = preprocessor.fit_transform(X_train)
print("Processed train shape:", X_train_prep.shape)

# Transform test
X_test_prep = preprocessor.transform(X_test)

# Exercise: Add 'pclass' to categorical and rerun