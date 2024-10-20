import numpy as np

A = np.arange(1, 16).reshape(3, 5)

print(A)
print("Dimensions", A.ndim)
print("Shape", A.shape)
print("Size", A.size)
print("Data type", A.dtype)

B = np.arange(1, 10).reshape(3, 3)
C = np.ones((3, 3)) * 2

print("\nMatrix B:", B)
print("\nMatrix C:", C)

# Elementwise subtraction
print("\nElement-wise subtraction (B - C):", B - C)

# Elementwise multiplication
print("\nElement-wise multiplication (B * C):", B * C)

# Matrix multiplication
print("\nMatrix multiplication (B @ C):", B @ C)


# Exponentiate each element in B
exp_B = np.exp(B)
print("Exponentiated matrix B:", exp_B)

# Minimum value in the whole matrix
min_value = np.min(B)
print("Minimum value in the whole matrix:", min_value)

# Minimum value in each row
min_row = np.min(B, axis=1)
print("Minimum value in each row:", min_row)

# Minimum value in each column
min_col = np.min(B, axis=0)
print("Minimum value in each column:", min_col)

# Index of the minimum value in the whole matrix
min_index = np.argmin(B)
print("Index of the minimum value in the whole matrix:", min_index)

# Index of the minimum value in each row
min_index_row = np.argmin(B, axis=1)
print("Index of the minimum value in each row:", min_index_row)

# Sum of all elements
sum_B = np.sum(B)
print("Sum of all elements in B:", sum_B)

# Mean for each column
mean_col = np.mean(B, axis=0)
print("Mean for each column:", mean_col)

# Median for each column
median_col = np.median(B, axis=0)
print("Median for each column:", median_col) 


#Iterating through array element-wise
for i in np.nditer(A):
    print(i)
    
    
#Explain code:
a = np.arange(30) #This line creates an array of 30 elements, ranging from 0 to 29.
b = a.reshape((2, 3, -1)) #This line reshapes the 1D array a into a 3D array b with the shape (2, 3, 5)
print(a)
print()
print(b)


#Copies an Views:
v1 = np.arange(4)
v2 = v1[-2:]
print(v1)
print(v2)
#You can check if an array is a view or a copy by using the 
# .base attribute. If the .base attribute is None, 
# then the array is a copy.If .base is not None, it returns
# a reference to the original array, meaning that the array is a view.
print(v1.base)
print(v2.base)

v2[-1] = 123 
#the last element in v1 will be changed. 
# This is because v2 is a view of v1, which means they 
# share the same data buffer. Changing v2 also updates the 
# corresponding elements in v1 because they refer to the same 
# underlying data.
print(v1) 
print(v2)  