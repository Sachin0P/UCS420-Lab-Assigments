import numpy as np

arr = np.array([4, 8, 12, 16, 20])
print("Q1 Array:", arr)
print("a) Add 2:", arr + 2)
print("b) Multiply 3:", arr * 3)
print("c) Divide 2:", arr / 2)


arr = np.array([1, 2, 3, 6, 4, 5])
print("\nQ2a Reversed:", arr[::-1])


def most_frequent(a):
    values, counts = np.unique(a, return_counts=True)
    max_count = counts.max()

    for i in range(len(values)):
        if counts[i] == max_count:
            positions = np.where(a == values[i])[0]
            print("Value", values[i], "appears", max_count, "times at indices", positions)


x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

print("\nQ2b(i) x:")
most_frequent(x)
print("Q2b(ii) y:")
most_frequent(y)


arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\nQ3 Array:")
print(arr)
print("a) 1st row, 2nd column:", arr[0, 1])
print("b) 3rd row, 1st column:", arr[2, 0])


sachin = np.linspace(10, 100, 25)
print("\nQ4 Array:")
print(sachin)
print("Dimensions:", sachin.ndim)
print("Shape:", sachin.shape)
print("Total elements:", sachin.size)
print("Data type:", sachin.dtype)
print("Total bytes:", sachin.nbytes)

transpose = sachin.reshape(25, 1)
print("Transpose using reshape, shape:", transpose.shape)

print("Using .T on 1D array, shape:", sachin.T.shape)
print("Using .T after making it 2D, shape:", sachin.reshape(1, 25).T.shape)


ucs420_sachin = np.array([[10, 20, 30, 40],
                          [50, 60, 70, 80],
                          [90, 15, 20, 35]])
print("\nQ5 Array:")
print(ucs420_sachin)
print("Mean:", np.mean(ucs420_sachin))
print("Median:", np.median(ucs420_sachin))
print("Max:", np.max(ucs420_sachin))
print("Min:", np.min(ucs420_sachin))
print("Unique:", np.unique(ucs420_sachin))

reshaped_ucs420_sachin = ucs420_sachin.reshape(4, 3)
print("Reshaped (4x3):")
print(reshaped_ucs420_sachin)

resized_ucs420_sachin = np.resize(ucs420_sachin, (2, 3))
print("Resized (2x3):")
print(resized_ucs420_sachin)