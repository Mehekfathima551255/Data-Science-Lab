import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("employees.csv")

# Create Dashboard
plt.figure(figsize=(12, 8))

# -------------------------
# Chart 1 - Bar Chart
# -------------------------
plt.subplot(2, 2, 1)
plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salary")

# -------------------------
# Chart 2 - Line Chart
# -------------------------
plt.subplot(2, 2, 2)
plt.plot(df["Name"], df["Age"], marker="o")
plt.title("Employee Age")

# -------------------------
# Chart 3 - Pie Chart
# -------------------------
plt.subplot(2, 2, 3)

department = df["Department"].value_counts()

plt.pie(
    department,
    labels=department.index,
    autopct="%1.1f%%"
)
plt.title("Departments")

# -------------------------
# Chart 4 - Salary Statistics
# -------------------------
plt.subplot(2, 2, 4)

stats = [
    df["Salary"].min(),
    df["Salary"].mean(),
    df["Salary"].max()
]

labels = ["Min", "Average", "Max"]

plt.bar(labels, stats)
plt.title("Salary Statistics")

plt.tight_layout()

plt.show()