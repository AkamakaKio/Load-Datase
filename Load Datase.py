import pandas as pd

# Load dataset from a CSV file
def load_dataset(filename):
    return pd.read_csv(filename)

# Example usage:
filename = "dataset.csv"
dataset = load_dataset(filename)
print(dataset.head())
