# Fondements Pratiques de l’Apprentissage Machine  
**TP Course Plan – Master Cybersécurité et IA**  
**Academic Year 2025/2026 – Université de Ain Temouchent**  
**Format: TP only – 3h/week – 14 weeks**  
**Focus: Hands-on learning with real datasets, professional workflows, and scikit-learn best practices**  
**Core Philosophy:** Not a theory course; emphasize data understanding before algorithms, exploration before preprocessing, preprocessing before modeling. Progressive difficulty, beginner-safe, avoid math, focus on ML workflows.  
**References:**  
- Aurélien Géron, *Hands-On Machine Learning*  
- Jake VanderPlas, *Python Data Science Handbook*  
- Sebastian Raschka, *Python Machine Learning*  
- Wes McKinney, *Python for Data Analysis*  

**Evaluation (40% continuous assessment):**  
- Graded TPs: Week 4 (10%), Week 8 (10%), Week 12 (10%), Week 14 mini-project (10%)  
- Weekly checkpoints: Notebook submissions for feedback (pass/fail)  

**Datasets Variety:** Iris, Titanic, Penguins, California Housing, Digits, Breast Cancer, Wine (at least 7 different).  

## Week 1: Introduction to Machine Learning and Python Environment Setup

**Pedagogical Objectives**  
- Familiarize students with the end-to-end ML workflow through a simple example  
- Set up a reproducible development environment for hands-on practice  
- Perform initial data loading and basic inspection to emphasize data understanding first

**Syllabus Link**  
Chapter 1: Introduction to Machine Learning

**Hands-on Activities**  
- Install Jupyter Notebook and required libraries  
- Load and inspect the dataset structure  
- Run basic summary statistics and identify potential issues like missing values

**Dataset Used**  
Iris (built-in scikit-learn dataset for classification)

**Python Libraries Used**  
NumPy, Pandas, Matplotlib, scikit-learn

**Notebook-ready Code**  
(See tp1.py below)

**Common Student Mistakes & Warnings**  
- Forgetting to import libraries at the top, leading to NameError  
- Loading data without checking for missing values or data types, which can cause downstream errors  
- Plotting without labels or titles, making visualizations hard to interpret – always add context

## Week 2: Basic Data Manipulation with Pandas and NumPy

**Pedagogical Objectives**  
- Master essential data loading and manipulation techniques  
- Use array operations for efficient computations  
- Build habits of exploring data subsets before full processing

**Syllabus Link**  
Chapter 2: Data Manipulation

**Hands-on Activities**  
- Load CSV-like data and perform filtering, grouping, and aggregation  
- Handle basic array reshaping and computations  
- Merge small data subsets to simulate real-world joining

**Dataset Used**  
Titanic (built-in Seaborn dataset for mixed data types)

**Python Libraries Used**  
Pandas, NumPy, Seaborn (for loading)

**Notebook-ready Code**  
(See tp2.py below)

**Common Student Mistakes & Warnings**  
- Using loops instead of vectorized Pandas/NumPy operations, which is inefficient for large data  
- Ignoring index alignment during merges, causing duplicated rows – always specify 'on' key  
- Modifying data in-place without .copy(), leading to SettingWithCopyWarning

## Week 3: Data Preprocessing Fundamentals – Handling Missing Data and Types

**Pedagogical Objectives**  
- Identify and address common data quality issues through exploration  
- Apply imputation and type conversion safely  
- Stress the importance of data understanding to choose appropriate preprocessing

**Syllabus Link**  
Chapter 3: Data Preprocessing

**Hands-on Activities**  
- Detect and impute missing values group-wise  
- Convert categorical to numerical types  
- Remove duplicates and invalid entries after inspection

**Dataset Used**  
Titanic (built-in Seaborn dataset)

**Python Libraries Used**  
Pandas, NumPy, scikit-learn (for basic imputation)

**Notebook-ready Code**  
(See tp3.py below)

**Common Student Mistakes & Warnings**  
- Imputing globally without grouping, leading to biased data (e.g., same age for all)  
- Filling missing categoricals with arbitrary values instead of mode – always explore distributions first  
- Forgetting to handle NaNs before type conversion, causing errors

## Week 4: Advanced Data Preprocessing – Encoding and Scaling

**Pedagogical Objectives**  
- Transform categorical and numerical features for ML compatibility  
- Introduce basic pipelines to automate steps  
- Ensure students split data early to prevent leakage

**Syllabus Link**  
Chapter 3: Data Preprocessing

**Hands-on Activities**  
- Apply encoding and scaling after train/test split  
- Build a simple ColumnTransformer for mixed types  
- Compare pre- and post-processed data

**Dataset Used**  
Titanic (built-in Seaborn dataset)

**Python Libraries Used**  
Pandas, scikit-learn (preprocessing, pipeline)

**Notebook-ready Code**  
(See tp4.py below)

**Common Student Mistakes & Warnings**  
- Fitting transformers on full dataset before split, causing data leakage  
- Using LabelEncoder for multi-class without understanding ordinality – prefer OneHot for nominal  
- Ignoring 'handle_unknown' in encoders, leading to errors on new data

**Graded TP**  
- **What is graded:** Notebook submission with preprocessing pipeline, EDA section, and interpretation of changes  
- **Evaluation Criteria (Rubric):**  
  - Code executes without errors (10 pts)  
  - Proper data split before fitting (20 pts)  
  - Logical choice of imputation/scaling/encoding with comments (30 pts)  
  - Quality of EDA (missing value plots, before/after comparison) (20 pts)  
  - Code clarity and comments (20 pts)  
Total: 100 pts (contributes to 10% of continuous assessment)

## Week 5: Data Visualization Basics for Exploration

**Pedagogical Objectives**  
- Use visualizations to uncover patterns and outliers during exploration  
- Select appropriate plot types based on data types  
- Interpret plots to guide preprocessing decisions

**Syllabus Link**  
Chapter 4: Data Visualization

**Hands-on Activities**  
- Create univariate and bivariate plots  
- Identify correlations and distributions  
- Customize plots for clarity

**Dataset Used**  
Penguins (built-in Seaborn dataset for mixed features)

**Python Libraries Used**  
Matplotlib, Seaborn, Pandas

**Notebook-ready Code**  
(See tp5.py below)

**Common Student Mistakes & Warnings**  
- Plotting without handling missing values, distorting distributions  
- Overloading plots with too many hues/variables, making them unreadable – keep simple  
- Forgetting to add titles/labels, reducing interpretability

## Week 6: Advanced Data Visualization Techniques

**Pedagogical Objectives**  
- Leverage multifaceted plots for deeper insights  
- Use statistical visualizations to compare groups  
- Connect visualizations back to data understanding for ML prep

**Syllabus Link**  
Chapter 4: Data Visualization

**Hands-on Activities**  
- Generate pair plots and facet grids  
- Visualize categorical vs numerical interactions  
- Save and annotate plots for reports

**Dataset Used**  
Penguins (built-in Seaborn dataset)

**Python Libraries Used**  
Seaborn, Matplotlib, Pandas

**Notebook-ready Code**  
(See tp6.py below)

**Common Student Mistakes & Warnings**  
- Using pairplot on large datasets without sampling, causing slow rendering  
- Misinterpreting correlations as causation – remind to use for exploration only  
- Not adjusting figure sizes, leading to cramped plots

## Week 7: Feature Engineering – Creating and Transforming Features

**Pedagogical Objectives**  
- Derive new features from existing ones using domain knowledge  
- Apply transformations to improve feature quality  
- Differentiate engineering (creating) from selection (choosing)

**Syllabus Link**  
Chapter 5: Feature Engineering & Selection (focus on engineering)

**Hands-on Activities**  
- Bin continuous features and create interactions  
- Apply log transforms and polynomial features  
- Evaluate new features via quick visualizations

**Dataset Used**  
California Housing (built-in scikit-learn dataset for regression)

**Python Libraries Used**  
Pandas, NumPy, scikit-learn (preprocessing)

**Notebook-ready Code**  
(See tp7.py below)

**Common Student Mistakes & Warnings**  
- Creating features without exploring originals, leading to redundant or noisy ones  
- Applying transforms like log to negative values – check ranges first  
- Confusing engineering with selection; engineering adds/modifies, selection prunes

## Week 8: Feature Selection – Filtering and Wrapping Methods

**Pedagogical Objectives**  
- Reduce feature sets to improve efficiency and reduce overfitting  
- Use statistical methods to select relevant features  
- Contrast with engineering (focus on choosing existing/derived features)

**Syllabus Link**  
Chapter 5: Feature Engineering & Selection (focus on selection)

**Hands-on Activities**  
- Apply variance threshold and correlation-based filtering  
- Use wrapper methods like RFE  
- Compare model scores before/after selection

**Dataset Used**  
California Housing (built-in scikit-learn dataset)

**Python Libraries Used**  
scikit-learn (feature_selection, linear_model), Pandas

**Notebook-ready Code**  
(See tp8.py below)

**Common Student Mistakes & Warnings**  
- Selecting features before splitting, leaking test info  
- Using supervised selection on unsupervised tasks – match method to problem  
- Mixing up selection (pruning) with reduction (projecting like PCA)

**Graded TP**  
- **What is graded:** Notebook with selection methods applied, comparisons, and feature importance interpretation  
- **Evaluation Criteria (Rubric):**  
  - Code runs and splits data correctly (10 pts)  
  - Multiple selection methods implemented (30 pts)  
  - Interpretation of selected features (e.g., why relevant?) (30 pts)  
  - Code clarity, comments, and visualizations (20 pts)  
  - Avoidance of leakage discussed (10 pts)  
Total: 100 pts (contributes to 10% of continuous assessment)

## Week 9: Dimensionality Reduction – Linear Methods (PCA)

**Pedagogical Objectives**  
- Project high-dimensional data to lower spaces for visualization and efficiency  
- Analyze explained variance to choose components  
- Distinguish from feature selection (projection vs subsetting)

**Syllabus Link**  
Chapter 6: Dimensionality Reduction

**Hands-on Activities**  
- Scale data and apply PCA  
- Plot cumulative variance and 2D projections  
- Reconstruct data to understand loss

**Dataset Used**  
Digits (built-in scikit-learn dataset for high-dim images)

**Python Libraries Used**  
scikit-learn (decomposition, preprocessing), Matplotlib

**Notebook-ready Code**  
(See tp9.py below)

**Common Student Mistakes & Warnings**  
- Forgetting to scale features, biasing PCA towards high-variance ones  
- Choosing too few components without checking variance – aim for 90-95%  
- Confusing PCA (new projections) with selection (original features)

## Week 10: Dimensionality Reduction – Non-Linear Methods (t-SNE)

**Pedagogical Objectives**  
- Apply non-linear techniques for better clustering visualization  
- Compare with linear methods like PCA  
- Use for exploration, not as preprocessing without caution

**Syllabus Link**  
Chapter 6: Dimensionality Reduction

**Hands-on Activities**  
- Run t-SNE on scaled data  
- Visualize and interpret clusters  
- Discuss perplexity and iterations

**Dataset Used**  
Digits (built-in scikit-learn dataset)

**Python Libraries Used**  
scikit-learn (manifold), Matplotlib

**Notebook-ready Code**  
(See tp10.py below)

**Common Student Mistakes & Warnings**  
- Using t-SNE for feature preprocessing without understanding it's non-deterministic  
- Setting perplexity too low/high, distorting clusters – start with 30  
- Treating as selection; it's for visualization, not feature creation

## Week 11: Constructing Train/Test/Validation Datasets

**Pedagogical Objectives**  
- Create balanced splits to evaluate models reliably  
- Use stratification and cross-validation to handle imbalances  
- Integrate with preprocessing to avoid leakage

**Syllabus Link**  
Chapter 7: Dataset Construction (Train/Test/Validation)

**Hands-on Activities**  
- Perform stratified splits  
- Set up K-fold CV  
- Build pipeline with split in mind

**Dataset Used**  
Breast Cancer (built-in scikit-learn dataset for classification)

**Python Libraries Used**  
scikit-learn (model_selection), Pandas

**Notebook-ready Code**  
(See tp11.py below)

**Common Student Mistakes & Warnings**  
- Forgetting stratification on imbalanced data, biasing splits  
- Applying CV without pipeline, leaking from folds  
- Using validation as test – reserve test for final eval

## Week 12: Integrating Pipelines for End-to-End Preprocessing

**Pedagogical Objectives**  
- Assemble full workflows using pipelines  
- Combine exploration, preprocessing, and splits  
- Test for leakage and efficiency

**Syllabus Link**  
Chapters 2-7 (integration)

**Hands-on Activities**  
- Build ColumnTransformer pipeline  
- Fit on train, transform test/val  
- Evaluate simple model with/without pipeline

**Dataset Used**  
Breast Cancer (built-in scikit-learn dataset)

**Python Libraries Used**  
scikit-learn (pipeline, compose, preprocessing, linear_model)

**Notebook-ready Code**  
(See tp12.py below)

**Common Student Mistakes & Warnings**  
- Fitting pipeline on test data – only fit on train  
- Omitting ColumnTransformer for mixed types, causing errors  
- Not testing for leakage by comparing train/test performance

**Graded TP**  
- **What is graded:** Full pipeline notebook with EDA, implementation, and leakage check  
- **Evaluation Criteria (Rubric):**  
  - Pipeline correctly assembled and executed (20 pts)  
  - Data split and no leakage (30 pts)  
  - EDA quality and integration (20 pts)  
  - Model evaluation and interpretation (20 pts)  
  - Code clarity/comments (10 pts)  
Total: 100 pts (contributes to 10% of continuous assessment)

## Week 13: Mini-Project Preparation – Dataset Choice and Exploration

**Pedagogical Objectives**  
- Independently select and explore a new dataset  
- Apply full exploration and preprocessing workflow  
- Prepare for pipeline building in Week 14

**Syllabus Link**  
All Chapters 1-7

**Hands-on Activities**  
- Choose dataset, perform EDA  
- Clean and engineer features  
- Visualize and document findings

**Dataset Used**  
Wine Quality (built-in scikit-learn, but simulate with load_wine for classification)

**Python Libraries Used**  
All previous (Pandas, Seaborn, scikit-learn)

**Notebook-ready Code**  
(See tp13.py below)

**Common Student Mistakes & Warnings**  
- Skipping EDA, jumping to preprocessing – always explore first  
- Over-engineering without validation  
- Not documenting choices, making review hard

## Week 14: Mini-Project – Full End-to-End Pipeline

**Pedagogical Objectives**  
- Synthesize course skills into a complete ML preparation workflow  
- Build and document a professional pipeline  
- Reflect on decisions to think like practitioners

**Syllabus Link**  
All Chapters 1-7

**Hands-on Activities**  
- Split, preprocess, engineer/select/reduce in pipeline  
- Evaluate with CV  
- Write report on choices and potential improvements

**Dataset Used**  
Wine Quality (built-in scikit-learn)

**Python Libraries Used**  
All previous

**Notebook-ready Code**  
(See tp14.py below)

**Common Student Mistakes & Warnings**  
- Integrating everything without modular testing, hard to debug  
- Ignoring class imbalance in multiclass  
- No reflection section – always discuss what worked/why


```python
# tp8.py
# Week 8: Feature Selection
from sklearn.datasets import fetch_california_housing
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load, split
housing = fetch_california_housing(as_frame=True)
X = housing.data
y = housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Variance threshold
vt = VarianceThreshold(threshold=0.1)
X_train_vt = vt.fit_transform(X_train)
print("Features after variance:", X_train_vt.shape[1])

# SelectKBest (filter)
selector = SelectKBest(f_regression, k=5)
X_train_kbest = selector.fit_transform(X_train, y_train)
print("Selected features:", X.columns[selector.get_support()])

# RFE (wrapper)
model = LinearRegression()
rfe = RFE(model, n_features_to_select=4)
rfe.fit(X_train, y_train)
print("RFE features:", X.columns[rfe.support_])

# Exercise: Apply to test set and compare shapes
```

```python
# tp9.py
# Week 9: PCA for Dimensionality Reduction
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# Load and split (though PCA unsupervised, split for consistency)
digits = load_digits()
X = digits.data
y = digits.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Always scale for PCA

# Apply PCA
pca = PCA(n_components=0.95)  # Retain 95% variance
X_pca = pca.fit_transform(X_scaled)
print("Components:", pca.n_components_)

# Explained variance plot
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Components')
plt.ylabel('Cumulative Variance')
plt.title('PCA Variance Explained')
plt.show()

# 2D projection
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10')
plt.colorbar()
plt.title('Digits PCA 2D')
plt.show()

# Exercise: Reconstruct with inverse_transform and compare
```

```python
# tp10.py
# Week 10: t-SNE for Non-Linear Reduction
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

digits = load_digits()
X = digits.data
y = digits.target
X_scaled = StandardScaler().fit_transform(X)

# Apply t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# Visualize
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10')
plt.colorbar()
plt.title('Digits t-SNE 2D Projection')
plt.show()

# Compare with PCA (from Week 9 code)
# Assume X_pca from previous
# plt.subplot(1,2,1); plt.scatter(X_pca[:,0], X_pca[:,1], c=y); plt.title('PCA')
# plt.subplot(1,2,2); plt.scatter(X_tsne[:,0], X_tsne[:,1], c=y); plt.title('t-SNE')

# Exercise: Vary perplexity (5, 50) and observe changes
```

```python
# tp11.py
# Week 11: Dataset Construction
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load
cancer = load_breast_cancer(as_frame=True)
X = cancer.data
y = cancer.target

# Stratified split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, stratify=y_train, random_state=42)
print("Shapes: Train", X_train.shape, "Val", X_val.shape, "Test", X_test.shape)

# K-fold CV
skf = StratifiedKFold(n_splits=5)
pipe = Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])
scores = cross_val_score(pipe, X_train, y_train, cv=skf)
print("CV scores:", scores.round(3))

# Exercise: Check class balance in splits
```

```python
# tp12.py
# Week 12: End-to-End Pipelines
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer(as_frame=True)
X = cancer.data
y = cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Preprocessor
num_transformer = Pipeline([('scaler', StandardScaler())])  # All numerical here

full_pipe = Pipeline([
    ('preprocessor', ColumnTransformer([('num', num_transformer, X.columns)])),
    ('classifier', LogisticRegression())
])

full_pipe.fit(X_train, y_train)
y_pred = full_pipe.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred).round(3))

# Exercise: Add MinMaxScaler alternative and compare
```

```python
# tp13.py
# Week 13: Mini-Project Prep
from sklearn.datasets import load_wine
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and explore
wine = load_wine(as_frame=True)
df = wine.frame
print(df.head())
print("\nMissing:\n", df.isnull().sum())
sns.pairplot(df, hue='target')
plt.show()

# Basic preprocessing (student expand)
df['alcohol_ph_ratio'] = df['alcohol'] / df['proline']  # Example engineering

# Exercise: Full EDA, impute if needed, visualize correlations
```

```python
# tp14.py
# Week 14: Mini-Project Pipeline
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

wine = load_wine(as_frame=True)
X = wine.data
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Pipeline with reduction
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('model', LogisticRegression(multi_class='auto'))
])

scores = cross_val_score(pipe, X_train, y_train, cv=5)
print("CV accuracy:", scores.mean().round(3))

# Exercise: Add feature selection step and compare
```