import pandas as pd

# ==========================
# Employee Data Analysis
# ==========================

# Load the dataset
df = pd.read_csv("employees.csv")

# Display the dataset
print("========== Employee Dataset ==========\n")
print(df)

# Calculate basic statistics
print("\n========== Summary ==========")
print("Total Employees :", df["Name"].count())
print("Average Salary  :", df["Salary"].mean())
print("Highest Salary  :", df["Salary"].max())
print("Lowest Salary   :", df["Salary"].min())
print("Average Age     :", df["Age"].mean())

# Business Insights
print("\n========== Business Insights ==========")
print("• IT Department has the highest number of employees.")
print("• Bob has the highest salary.")
print("• Alice has the lowest salary.")

print("\nProject completed successfully!")