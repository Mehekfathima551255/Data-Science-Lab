import pandas as pd

# Load Dataset
df = pd.read_csv("employees.csv")

print("Dataset")
print(df)

# Total Salary
print("\nTotal Salary:")
print(df["Salary"].sum())

# Average Salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# Highest Salary
print("\nHighest Salary:")
print(df["Salary"].max())

# Lowest Salary
print("\nLowest Salary:")
print(df["Salary"].min())

# Number of Employees
print("\nNumber of Employees:")
print(df["Name"].count())

# Average Age
print("\nAverage Age:")
print(df["Age"].mean())

# Highest Age
print("\nHighest Age:")
print(df["Age"].max())

# Lowest Age
print("\nLowest Age:")
print(df["Age"].min())