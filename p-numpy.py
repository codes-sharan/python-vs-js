import numpy as np

#1. Creating Arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones
full_array = np.full((2, 3), 7)  # 2x3 array filled with 7
range_array = np.arange(0, 10, 2)  # array with numbers from 0 to 10, step 2
lin_space = np.linspace(0, 1, 5)  # 5 values between 0 and 1

print(arr)
print(zeros)
print(ones)
print(full_array)
print(range_array)
print(lin_space)


#2. Array operations
# Element-wise
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# sum_array = a + b          # [5, 7, 9]
# product_array = a * b      # [4, 10, 18]

# Matrix-operations
# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])
# matrix_product = np.dot(matrix1, matrix2)  # Matrix multiplication

# 3. Array manipulations
# Reshaping
# reshaped = np.arange(6).reshape((2, 3))  # Reshape to 2x3

# Indexing and slicing
# array = np.array([10, 20, 30, 40, 50])
# print(array[1:4])  # Output: [20, 30, 40]


# 4. Statistical operations
# data = np.array([1, 2, 3, 4, 5])
# mean = np.mean(data)  # Mean
# std_dev = np.std(data)  # Standard deviation

# 5. Common functions
# total = np.sum(data)
# product = np.prod(data)
# max_value = np.max(data)
# min_value = np.min(data)

# 6. Saving and loading arrays
# np.save('my_array.npy', arr)  # Save
# loaded_arr = np.load('my_array.npy')  # Load


# 7. Example

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# squared = arr ** 2
# mean_value = np.mean(squared)

# print("Original array:", arr)
# print("Squared values:", squared)
# print("Mean of squared values:", mean_value)
