import pandas as pd
import numpy as np

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['X', 'Y', 'X', 'Y', 'Z']}
df = pd.DataFrame(data)

# Data Selection and Filtering
# Using loc[] for label-based indexing
print("Using loc[]:")
print(df.loc[df['C'] == 'X'])

# Using iloc[] for integer-based indexing
print("\nUsing iloc[]:")
print(df.iloc[[1, 3]])

# Using query() for filtering
print("\nUsing query():")
print(df.query('B > 30'))

# Using isin() to check for values
print("\nUsing isin():")
print(df[df['C'].isin(['X', 'Y'])])

# Data Aggregation and Transformation
# Using groupby()
print("\nGrouped DataFrame:")
print(df.groupby('C')['A'].mean())

# Using pivot_table()
print("\nPivot table:")
print(pd.pivot_table(df, values='A', index='C', aggfunc=np.mean))

# Using apply() and applymap()
print("\nUsing apply() and applymap():")
print(df.apply(lambda x: x**2))

# Data Cleaning and Preprocessing
# Using drop_duplicates()
print("\nDataFrame after dropping duplicates:")
print(df.drop_duplicates())

# Using replace()
print("\nDataFrame after replacing 'X' with 'Z':")
print(df.replace({'X': 'Z'}))

# Using astype()
print("\nDataFrame after casting column 'B' to float:")
print(df.astype({'B': float}))

# Array Manipulation
# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Using reshape()
print("\nReshaped array:")
print(np.reshape(arr, (3, 2)))

# Using transpose()
print("\nTransposed array:")
print(np.transpose(arr))

# Using hstack() and vstack()
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nHorizontal stack:")
print(np.hstack((arr1, arr2)))
print("\nVertical stack:")
print(np.vstack((arr1, arr2)))

# Using mean(), median(), std()
print("\nMean of array elements:", np.mean(arr))
print("Median of array elements:", np.median(arr))
print("Standard deviation of array elements:", np.std(arr))

# Using dot()
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("\nDot product of arrays:")
print(np.dot(arr1, arr2))

# Using argmax() and argmin()
print("\nIndex of maximum element:", np.argmax(arr))
print("Index of minimum element:", np.argmin(arr))

# Random Number Generation
# Using randint()
print("\nRandom integers between 1 and 10:")
print(np.random.randint(1, 10, size=(2, 3)))

# Using uniform()
print("\nRandom samples from a uniform distribution:")
print(np.random.uniform(size=(2, 3)))
