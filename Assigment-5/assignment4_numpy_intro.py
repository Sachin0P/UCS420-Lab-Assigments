import numpy as np

arr = np.array([4, 8, 12, 16, 20])
print("Q1 Original array:", arr)

print("a) +2  :", arr + 2)
print("b) *3  :", arr * 3)
print("c) /2  :", arr / 2)

arr = np.array([1, 2, 3, 6, 4, 5])
print("\nQ2a Reversed:", arr[::-1])

def most_frequent(a):
    vals, counts = np.unique(a, return_counts=True)
    top = counts.max()
    winners = vals[counts == top]
    for v in winners:
        idx = np.where(a == v)[0]
        print(f"   value {v} appears {top} times at indices {idx}")

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

print("\nQ2b(i) x:")
most_frequent(x)
print("Q2b(ii) y:")
most_frequent(y)

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\nQ3 Array:\n", arr)

print("a) 1st row, 2nd col:", arr[0, 1])
print("b) 3rd row, 1st col:", arr[2, 0])

sachin = np.linspace(10, 100, 25)
print("\nQ4 Array:\n", sachin)
print("Dimensions :", sachin.ndim)
print("Shape      :", sachin.shape)
print("Total elems:", sachin.size)
print("Data type  :", sachin.dtype)
print("Total bytes:", sachin.nbytes)

row = sachin.reshape(1, 25)
col = row.reshape(25, 1)
print("Transpose via reshape -> shape", col.shape)

print("sachin.T shape:", sachin.T.shape)

print("row.T shape   :", row.T.shape)

ucs420_sachin = np.array([[10, 20, 30, 40],
                          [50, 60, 70, 80],
                          [90, 15, 20, 35]])
print("\nQ5 Array:\n", ucs420_sachin)
print("Mean   :", np.mean(ucs420_sachin))
print("Median :", np.median(ucs420_sachin))
print("Max    :", np.max(ucs420_sachin))
print("Min    :", np.min(ucs420_sachin))
print("Unique :", np.unique(ucs420_sachin))

reshaped_ucs420_sachin = ucs420_sachin.reshape(4, 3)
print("Reshaped (4x3):\n", reshaped_ucs420_sachin)

resized_ucs420_sachin = np.resize(ucs420_sachin, (2, 3))
print("Resized (2x3):\n", resized_ucs420_sachin)
