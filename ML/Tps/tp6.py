# Week 6: Advanced Visualization
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

# Pairplot for multivariate exploration
sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle('Penguin Features Pairplot')
plt.show()

# FacetGrid: distributions by category
g = sns.FacetGrid(df, col='island', hue='sex')
g.map(sns.histplot, 'body_mass_g', kde=True)
g.add_legend()
plt.suptitle('Body Mass by Island and Sex')
plt.show()

# Jointplot: bivariate with margins
sns.jointplot(data=df, x='flipper_length_mm', y='body_mass_g', kind='reg')
plt.suptitle('Flipper Length vs Body Mass')
plt.show()

# Exercise: Create a violin plot for bill length by species