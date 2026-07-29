import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

print("Original Dataset")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check data types
print("\nData Types:")
print(df.dtypes)

# Display cleaned dataset
print("\nClean Dataset:")
print(df)