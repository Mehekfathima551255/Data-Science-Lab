import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("employees.csv")

# ------------------------
# Bar Chart - Employee Salary
# ------------------------
plt.figure(figsize=(6,4))
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salary")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()

# ------------------------
# Line Chart - Employee Age
# ------------------------
plt.figure(figsize=(6,4))
plt.plot(df["Name"], df["Age"], marker="o")
plt.title("Employee Age")
plt.xlabel("Employee")
plt.ylabel("Age")
plt.show()

# ------------------------
# Pie Chart - Department Distribution
# ------------------------
department_count = df["Department"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)
plt.title("Department Distribution")
plt.show()