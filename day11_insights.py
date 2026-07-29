import pandas as pd

# Load Dataset
df = pd.read_csv("employees.csv")

print("Business Insights")
print("-------------------------")

print("1. Total Employees:", df["Name"].count())

print("2. Average Salary:", df["Salary"].mean())

print("3. Highest Salary:", df["Salary"].max())

print("4. Lowest Salary:", df["Salary"].min())

print("5. Average Age:", df["Age"].mean())

print("6. Most Employees are in the IT Department.")

print("7. Bob has the highest salary.")

print("8. Alice has the lowest salary.")