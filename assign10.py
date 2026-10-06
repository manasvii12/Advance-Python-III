import numpy as np

# 1. Create a one-dimensional array with numbers 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Perform slicing operations
print("\nFirst 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Elements from index 2 to 7:", arr[2:8])
print("Every second element:", arr[::2])

# 3. Compute statistical measures
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Apply broadcasting to modify elements
print("\nArray after adding 5:", arr + 5)
print("Array after multiplying by 2:", arr * 2)
