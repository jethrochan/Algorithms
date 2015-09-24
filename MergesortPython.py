#Jethro Chan
#python 3.4.2
#Mergesort
import math
import copy


def Mergesort(A):
    n = len(A)
    if(n < 2):
        return
    mid = math.floor(n/2) 
   
    #create data from A into L and R array respectively
    left = copy.copy(A[0:mid])
    right = copy.copy(A[mid:n])

    Mergesort(left)
    Mergesort(right)
    Merge(left, right, A)
    return

def Merge(L, R, A):
    nL = len(L)
    nR = len(R)

    i = 0 #iterator for left
    j = 0 #iterator for right
    k = 0 #iterator for A

    #1st while loop
    while(i < nL and j <nR):
        if(L[i] <= R[j]): #if the min of the L and R is less in L, pick left
            A[k] = L[i] 
            k = k+1
            i = i+1
        else:
            A[k] = R[j] 
            k = k+1
            j = j+1
               

    #2nd while loop
    while(i < nL): #if items are still remaining in left and not placed in A yet
        A[k] = L[i]
        k = k+1
        i = i+1

    while(j < nR): #if items are still remaining in left and not placed in A yet
        A[k] = R[j]
        k = k+1
        j = j+1

    return
    
#take in input for original array A
A = []

inputnumber = 0
while(inputnumber != 's'):
    inputnumber = input("Please Enter Integers to be Sorted, 's' to stop: ")
    if(inputnumber != 's'):
        A.append(inputnumber)

A = [int(i) for i in A] #convert elements in array to ints
    
Mergesort(A)
print("Result: ")
print(A) #print out sorted array
