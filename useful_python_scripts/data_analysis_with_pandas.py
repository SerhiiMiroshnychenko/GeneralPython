import pandas as pd

# Read data from a CSV file
data = pd.read_csv('data.csv')

# Perform basic analysis
mean = data['column_name'].mean()
print(f"Mean: {mean}")
