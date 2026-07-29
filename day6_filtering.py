import pandas as pd

# Load Dataset
df = pd.read_csv("employees.csv")

print("Original Dataset")
print(df)

# Select a Single Column
print("\nEmployee Names:")
print(df["Name"])

# Select Multiple Columns
print("\nName and Salary:")
print(df[["Name", "Salary"]])

# Filter Employees with Age greater than 26
print("\nEmployees Age > 26:")
print(df[df["Age"] > 26])

# Filter IT Department
print("\nIT Department Employees:")
print(df[df["Department"] == "IT"])

# Sort by Salary (Lowest to Highest)
print("\nSorted by Salary:")
print(df.sort_values("Salary"))

# Sort by Age (Highest to Lowest)
print("\nSorted by Age (Descending):")
print(df.sort_values("Age", ascending=False))