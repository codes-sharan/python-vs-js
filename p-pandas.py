
import pandas as pd

# 1. Creating a dataframe
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

# 2. Reading data
# From a CSV file
# df = pd.read_csv('iris.csv')

# # From an Excel file
# df = pd.read_excel('file.xlsx')

# # From a JSON file
# df = pd.read_json('file.json')

import seaborn as sns
iris = sns.load_dataset('iris')
iris.to_csv('iris.csv', index=False)  # Save to CSV



# Basic dataframe operations
print(df.head())      # First 5 rows
print(df.tail())      # Last 5 rows
print(df.shape)       # Dimensions of the DataFrame

# Selecting Columns:
ages = df['Age']              # Single column
subset = df[['Name', 'City']] # Multiple columns

# Filtering Rows:
adults = df[df['Age'] > 30]  # Rows where Age is greater than 30

# Adding a New Column:
df['Salary'] = [70000, 80000, 90000]  # New column

# Dropping Columns:
df.drop('Salary', axis=1, inplace=True)  # Drop column in place


# Data analysis
print(df.describe())  # Summary statistics
grouped = df.groupby('City').mean()  # Group by 'City' and calculate mean
sorted_df = df.sort_values(by='Age', ascending=False)  # Sort by Age

# Saving data
df.to_csv('output.csv', index=False)     # Save to CSV
df.to_excel('output.xlsx', index=False)  # Save to Excel
