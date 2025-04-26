# Multidimensional Arrays in NumPy

matrix = np.array([[1,2,3],[4,5,6]])
print(matrix[0,1]) # access element at row 0, column 1
print(matrix[:,1]) # get entire second column
print(matrix[1,:]) # get entire second row

#important numpy functions
np.zeros((3,3)) #3*3 matrix of zeros
np.ones((2,4)) #2*4 matrix of ones
np.eye(4) #4*4 identity matrix
np.linspace(1,10,5) #5 evenly spaced values between 1 and 10
np.arrange(1,10,2) #array from 1 to 10 with step 2

