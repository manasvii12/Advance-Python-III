import pandas as pd
import numpy as np

# 1. Create a Series with 10 random numbers
numbers = pd.Series(np.random.randint(1, 100, 10))
print("Series of Random Numbers:")
print(numbers)

# 2. Indexing examples
print("\nAccess first element (iloc):", numbers.iloc[0])
print("Access element with label 3 (loc):", numbers.loc[3])

# 3. Filtering examples
print("\nNumbers greater than 50:")
print(numbers[numbers > 50])

print("\nEven numbers only:")
print(numbers[numbers % 2 == 0])

# 4. Statistical operations
print("\nMean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())
