from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

roll_no = 1024170302

M = float(input("Enter the value of M: "))
x = np.linspace(-10, 10, 200)
y1 = M * x ** 2
y2 = M * np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y1, color="blue", linestyle="-", label="y = M * x^2")
plt.plot(x, y2, color="red", linestyle="--", label="y = M * sin(x)")
plt.title(f"Mathematical Functions for M = {M}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

marks = {
    "Subject": ["Maths", "Physics", "Chemistry", "English", "Computer"],
    "Score": [88, 76, 69, 82, 95],
}
marks_df = pd.DataFrame(marks)
print(marks_df)

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=marks_df, x="Subject", y="Score", hue="Subject", palette="colorblind", legend=False)
for container in ax.containers:
    ax.bar_label(container)
ax.set_title("Scores by Subject")
ax.set_xlabel("Subject")
ax.set_ylabel("Score")
ax.set_ylim(0, 105)
ax.grid(axis="y")
ax.set_axisbelow(True)
plt.show()

np.random.seed(roll_no)
data = np.random.randn(50)
noise = np.random.randn(50)
index = np.arange(50)

fig, axes = plt.subplots(2, 2, figsize=(11, 8))

axes[0, 0].plot(index, np.cumsum(data), color="blue")
axes[0, 0].set_title("Cumulative Sum")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Cumulative Sum")
axes[0, 0].grid(True)

axes[0, 1].scatter(index, data + noise, color="green")
axes[0, 1].set_title("Scatter Plot with Random Noise")
axes[0, 1].set_xlabel("Index")
axes[0, 1].set_ylabel("Value + Noise")
axes[0, 1].grid(True)

axes[1, 0].hist(data, bins=10, color="orange", edgecolor="white")
axes[1, 0].set_title("Histogram of Values")
axes[1, 0].set_xlabel("Value")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True)

axes[1, 1].boxplot(data)
axes[1, 1].set_title("Box Plot of Values")
axes[1, 1].set_xlabel("Dataset")
axes[1, 1].set_ylabel("Value")
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

sales = pd.read_csv(Path(__file__).resolve().parent.parent / "company_sales_data.csv")

plt.figure(figsize=(8, 5))
ax = sns.lineplot(data=sales, x="month_number", y="total_profit", marker="o")
ax.set_title("Total Profit per Month")
ax.set_xlabel("Month")
ax.set_ylabel("Total Profit")
ax.set_xticks(sales["month_number"])
ax.grid(True)
plt.show()

products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
product_sales = sales.melt(id_vars="month_number", value_vars=products, var_name="Product", value_name="Units")

plt.figure(figsize=(9, 5))
ax = sns.lineplot(data=product_sales, x="month_number", y="Units", hue="Product", style="Product", markers=True)
ax.set_title("Product Sales per Month")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")
ax.set_xticks(sales["month_number"])
ax.grid(True)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

attributes = sales.columns.drop("month_number")
fig, axes = plt.subplots(4, 2, figsize=(12, 12))
for ax, attribute in zip(axes.flat, attributes):
    sns.barplot(data=sales, x="month_number", y=attribute, color="steelblue", ax=ax)
    ax.set_title(attribute)
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.grid(axis="y")
    ax.set_axisbelow(True)
plt.tight_layout()
plt.show()
