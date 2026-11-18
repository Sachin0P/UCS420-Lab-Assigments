import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

roll_no = 1024170302

np.random.seed(roll_no)
low = np.random.randint(1000, 2001)
high = np.random.randint(4000, 5001)
sales = np.random.randint(low, high + 1, size=(12, 4))

categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df = pd.DataFrame(sales, columns=categories, index=months)

print("First 5 rows:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())

print("\nTotal sales per category:")
print(df[categories].sum())
print("\nTotal sales per month:")
print(df[categories].sum(axis=1))

print("\nAverage growth between consecutive months (%):")
print(df[categories].pct_change().mean() * 100)

df["Total Sales"] = df[categories].sum(axis=1)
df["Growth Rate"] = df["Total Sales"].pct_change() * 100
print("\nWith Total Sales and Growth Rate:")
print(df)

if roll_no % 2 == 0:
    df["Electronics"] = df["Electronics"] * 0.90
    print("\nRoll number is even: 10% discount applied to Electronics")
else:
    df["Clothing"] = df["Clothing"] * 0.85
    print("\nRoll number is odd: 15% discount applied to Clothing")

df["Total Sales"] = df[categories].sum(axis=1)
df["Growth Rate"] = df["Total Sales"].pct_change() * 100
print(df)

plt.figure(figsize=(10, 5))
ax = sns.lineplot(data=df[categories], markers=True)
ax.set_title("Monthly Sales Trends by Category")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")
ax.grid(True)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
ax = sns.boxplot(data=df[categories])
ax.set_title("Sales Distribution by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Units Sold")
ax.grid(axis="y")
ax.set_axisbelow(True)
plt.show()

array = np.array([[1, -2, 3], [-4, 5, -6]])

print("\nAbsolute values:")
print(np.abs(array))

percentiles = [25, 50, 75]
print("\nPercentiles of flattened array:", np.percentile(array, percentiles))
print("Percentiles of each column:")
print(np.percentile(array, percentiles, axis=0))
print("Percentiles of each row:")
print(np.percentile(array, percentiles, axis=1))

print("\nFlattened mean:", np.mean(array))
print("Flattened median:", np.median(array))
print("Flattened standard deviation:", np.std(array))
print("Column mean:", np.mean(array, axis=0))
print("Column median:", np.median(array, axis=0))
print("Column standard deviation:", np.std(array, axis=0))
print("Row mean:", np.mean(array, axis=1))
print("Row median:", np.median(array, axis=1))
print("Row standard deviation:", np.std(array, axis=1))

a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

print("\nFloor:", np.floor(a))
print("Ceiling:", np.ceil(a))
print("Truncated:", np.trunc(a))
print("Rounded:", np.round(a))

numbers = [10, 20, 30, 40, 50]
print("\nList before swap:", numbers)
i, j = 1, 3
temp = numbers[i]
numbers[i] = numbers[j]
numbers[j] = temp
print("List after swap:", numbers)

values = {1, 2, 3, 4, 5}
print("\nSet:", values)
values_list = list(values)
print("List before swap:", values_list)
i, j = 0, 4
temp = values_list[i]
values_list[i] = values_list[j]
values_list[j] = temp
print("List after swap:", values_list)
