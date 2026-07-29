import pandas as pd

df = pd.read_csv("employees.csv")

print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())