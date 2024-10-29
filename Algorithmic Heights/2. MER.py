'''
MER exercise

Given: A positive integer n ≤ 10^5 and a sorted array A[1...n] of integers from -10^5 to 10^5, 
       a positive integer m ≤ 10^5 and a sorted array B[1...m] of integers from -10^5 to 10^5.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
'''

# we define a function, 'merge_sort', through which we are able to merge the two given arrays
def merge_sort(a, b):
    C = []                            # C is the empty list to which we will append elements from A and B to form the merged array
    i, j = 0, 0                       # i and j are the starting indexes of the elements of the 2 arrays
    while i < len(a) and j < len(b):  
        if a[i] < b[j]:               # if the element of array A at an established index is bigger than the element of array B at the same index
            C.append(a[i])            # we add the element of arrray A to the empty list C
            i += 1                    # we increase the index i of 1 unit
        else:
            C.append(b[j])            # if not, we append the element of array B to the empty list C
            j += 1                    # we increase the index j of 1 unit

# we now append the remaining elements of A and B to the list C
    C += a[i:]                        
    C += b[j:]

    print (*C)

numbersA = '2 4 10 18'
numbersB = '-5 11 12'

numbers_listA = numbersA.split()
numbers_listB = numbersB.split()

a = [int(num) for num in numbers_listA]
b = [int(num) for num in numbers_listB]

i, j = 4, 3 

merge_sort(a, b)