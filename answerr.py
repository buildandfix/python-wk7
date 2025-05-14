
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set output directory for saving plots
output_dir = "plots"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    # Task 1: Load and Explore the Dataset

    # Load the Iris dataset using seaborn's built-in dataset
    iris = sns.load_dataset('iris')

    # Display the first few rows
    print("First 5 rows of the Iris dataset:")
    print(iris.head())

    # Explore dataset structure
    print("\nDataset Info:")
    print(iris.info())

    # Check for missing values
    print("\nMissing Values:")
    print(iris.isnull().sum())

    # Clean dataset (Iris is typically clean, but demonstrate handling)
    if iris.isnull().any().any():
        print("\nHandling missing values...")
        # For numerical columns, fill with mean
        numerical_cols = iris.select_dtypes(include=['float64']).columns
        iris[numerical_cols] = iris[numerical_cols].fillna(iris[numerical_cols].mean \
        iris = iris.fillna(iris.mean(numeric_only=True))
        print("Missing values filled with column means.")
    else:
        print("\nNo missing values found in the dataset.")

    # Task 2: Basic Data Analysis

    # Compute basic statistics for numerical columns
    print("\nBasic Statistics:")
    stats = iris.describe()
    print(stats)

    # Group by species and compute mean for numerical columns
    print("\nMean Values by Species:")
    species_means = iris.groupby('species').mean()
    print(species_means)

    # Findings
    print("\nAnalysis Findings:")
    print("- Setosa has the smallest average petal length and width.")
    print("- Virginica has the largest average sepal length and petal measurements.")
    print("- Versicolor shows intermediate values, closer to Virginica than Setosa.")
    print("- Sepal width is relatively consistent across species compared to other measurements.")

    # Task 3: Data Visualization

    # Set seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # 1. Line Chart: Average measurements per species (simulating a trend)
    plt.figure(figsize=(10, 6))
    species_means.plot(kind='line', marker='o')
    plt.title('Average Measurements Across Iris Species', fontsize=14)
    plt.xlabel('Species', fontsize=12)
    plt.ylabel('Measurement (cm)', fontsize=12)
    plt.legend(title='Measurement', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'iris_line_chart.png'))
    plt.close()

    # 2. Bar Chart: Average petal length per species
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal_length', data=iris, ci=None)
    plt.title('Average Petal Length by Species', fontsize=14)
    plt.xlabel('Species', fontsize=12)
    plt.ylabel('Petal Length (cm)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'iris_bar_chart.png'))
    plt.close()

    # 3. Histogram: Distribution of sepal length
    plt.figure(figsize=(8, 6))
    plt.hist(iris['sepal_length'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sepal Length', fontsize=14)
    plt.xlabel('Sepal Length (cm)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'iris_histogram.png'))
    plt.close()

    # 4. Scatter Plot: Sepal length vs. petal length by species
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal_length', y='petal_length', hue='species', size='species', data=iris)
    plt.title('Sepal Length vs. Petal Length by Species', fontsize=14)
    plt.xlabel('Sepal Length (cm)', fontsize=12)
    plt.ylabel('Petal Length (cm)', fontsize=12)
    plt.legend(title='Species', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'iris_scatter_plot.png'))
    plt.close()

    # Additional Observations
    print("\nVisualization Observations:")
    print("- The scatter plot shows clear separation of Setosa, with smaller petal and sepal lengths.")
    print("- Virginica's larger measurements are evident in the bar and line charts.")
    print("- The histogram indicates a roughly normal distribution for sepal length with a slight right skew.")
    print("- The line chart suggests a trend of increasing measurements from Setosa to Virginica.")

except FileNotFoundError:
    print("Error: Dataset could not be loaded. Please check the data source.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
