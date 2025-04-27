#numpy arrays.py (recommended for numerical operations)

#creating numpy array


import numpy as np
arr = np.array([1,2,3,4,5]) #1D array

matrix = np.array([[1,2,3],[4,5,6]]) #2D array

#Operations on NumPy Arrays
arr = np.append(arr,[6,7]) # append elements
arr = np.insert(arr,2,10) # insert at index 2
arr = np.delete(arr,1) # delete element at index 1
print(arr.size) # get size
print(arr.shape) # get shape of array
print(arr.dtype) # get data type

#Mathematical operations
arr = np.array([1,2,3,4,5])
print(arr + 2) #Add 2 to each element
print(arr * 3) #Multiply each element by 3
print(np.sum(arr)) #Sum of element
print(np.mean(arr)) #Mean of element
print(np.sqrt(arr)) #Square root of each element



