'''
INS exercise

Given: A positive integer n ≤ 10^3 and an array A[1...n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1...n].
'''

numbers = '6 10 4 5 1 2'

# with the 2 following commands we are transforming the numbers string into a list of integers
numbers_list = numbers.split()
a = [int(num) for num in numbers_list]

# we initialize the swap count as 0
swapcount = 0 

# with the for loop we are able to continuously check the elements in the list a
for element in range (1 , len (a)):
    key = a[element]                # key represents the elements we need to move in the correct position
    j = element - 1                 # j represents the elements on the left of key with which we want to compare key

# with the while loop we check if key is smaller than element at index j
    while j >= 0 and key < a[j]:    
        a[j +1] = a[j]              # if key is smaller than element at index j, we move key to the left of a[j]
        j -= 1                      # we are now moving to the right of 1 index to continue the comparison with other elements of a
        swapcount += 1              # if the while loop does these actions the swapcount is increased of 1 unit
    a[j +1] = key

print (swapcount)