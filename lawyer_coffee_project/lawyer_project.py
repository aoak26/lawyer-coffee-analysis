import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("lawyer_coffee.csv")

# 2. Take a quick look at the data
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIPTION ---")
print(df.describe())

# 3. First chart: Coffee vs Days to Deadline
plt.figure(figsize=(8, 5))

for lawyer in df['lawyer_id'].unique():
    subset = df[df['lawyer_id'] == lawyer]
    plt.plot(
        subset['days_to_deadline'],
        subset['coffee_cups'],
        marker='o',
        label=f'Lawyer {lawyer}'
    )

plt.xlabel("Days to Deadline")
plt.ylabel("Coffee Cups per Day")
plt.title("Lawyer Coffee Consumption vs Deadlines")
plt.gca().invert_xaxis()
plt.legend()
plt.show()

# 4. Second chart: Hours Worked vs Coffee Cups
plt.figure(figsize=(8, 5))

plt.scatter(df['hours_worked'], df['coffee_cups'])
plt.xlabel("Hours Worked")
plt.ylabel("Coffee Cups")
plt.title("Coffee Consumption vs Hours Worked")
plt.show()
