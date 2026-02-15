# NumPy Data Explorer
import numpy as np
import time
print("===== NUMPY DATA EXPLORER =====\n")

# Array Creation
print("1) Array Creation")
# Creating a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Simple Array:", arr)
# Creating array using arange
arr_range = np.arange(1, 6)
print("Array using arange:", arr_range)
# Creating 2D array
matrix = np.array([[1, 2, 3],[4, 5, 6]])
print("2D Array:\n", matrix)

# Indexing and Slicing
print("\n2) Indexing and Slicing")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice (index 1 to 3):", arr[1:4])

# Mathematical Operations
print("\n3) Mathematical Operations")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Axis-wise Operations
print("\n4) Axis-wise Operations")
print("Sum of all elements:", np.sum(matrix))
print("Sum column-wise (axis=0):", np.sum(matrix, axis=0))
print("Sum row-wise (axis=1):", np.sum(matrix, axis=1))

# Statistical Operations
print("\n5) Statistical Operations")
data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))

# Reshaping and Broadcasting
print("\n6) Reshaping and Broadcasting")
numbers = np.arange(1, 7)
print("Original array:", numbers)
reshaped = numbers.reshape(2, 3)
print("Reshaped to 2x3:\n", reshaped)
# Broadcasting example
print("Adding 10 to each element:")
print(reshaped + 10)

# Save and Load NumPy Array
print("\n7) Save and Load Array")
np.save("my_array.npy", reshaped)
loaded_array = np.load("my_array.npy")
print("Loaded Array:\n", loaded_array)

# Performance Comparison
print("\n8) Performance Comparison")
size = 1000000
# Python list
python_list = list(range(size))
start = time.time()
python_list = [x * 2 for x in python_list]
end = time.time()
print("Python List Time:", end - start)

# NumPy array
numpy_array = np.arange(size)
start = time.time()
numpy_array = numpy_array * 2
end = time.time()
print("NumPy Array Time:", end - start)
print("\n===== PROJECT COMPLETED =====")
