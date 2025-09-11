def matrix_multiply(A,B):
    #get the dimension of matrices
    rows_A, cols_A = len(A),len(A[0])
    rows_B, cols_B =len(B),len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")
    



    #create the result matrix with zeros

    result =[[0 for _ in range(cols_B)] for _ in range(rows_A)]

    #perform matrix multiplication
    for i in range(rows_A) :
         for j in range (cols_B) :
           for k in range (cols_A) :
                result[i][j] += A[i][k] * B[k][j]
            
    return result
-

#example usage 
A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]
result = matrix_multiply(A,B)
for row in result:
    print(row)