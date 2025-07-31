#Problem Statement –
#A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

#Example 1 :

##There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

#Input :

#8  – Value of N

#[4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

#Output:

#4 5 1 9 5 0 0 0

#Example 2:

#Input:

#6 — Value of N.

#[6,0,1,8,0,2] – Element of arr[0] to arr[N-1], While input each element is separated by newline

#Output:

#6 1 8 2 0 0


#You are given an array of integers representing chocolate packets. Some of these packets are empty, represented by the value 0.

#Your goal is to:

#Move all the 0s (empty packets) to the end of the array.

#Preserve the order of the non-zero (non-empty) packets.

#This operation must be in-place (i.e., without creating a new array, if possible).


N=8
arr=[4,5,0,1,9,0,5,0]
def push_zeros_to_end(arr,N):
    pos=0 #position to place the next non-zeros element

#first move non-zero element to the front
    for i in range(N):
            if arr[i]!=0:
                arr[pos]=arr[i]   
                pos +=1

#fill the rest of array with 0s
    while pos < N:
                     arr[pos]=0
                     pos+= 1
    
    return arr

N=int(input())
arr=[int(input()) for _ in range(N)]

result=push_zeros_to_end(arr,N)
print(*result)
