'''
PAR exercise
Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5.

Return: A permuted array B[1...n] such that it is a permutation of A and there is an index 1≤q≤n
        such that B[i]≤A[1] for all 1≤i≤q-1, B[q]=A[1] and B[i]>A[1] for all q+1≤i≤n.
'''

# we define a function through which we can permutate the array A following the given instructions
def two_way_partition(array):
    q = array[0]                           # q is our pivot, it is the element at index 0 in the array A
    smallerQ = []                          # smallerQ is an empty list to which we will append all the elements smaller than the chosen pivot
    greaterQ = []                          # greaterQ is an empty list to which we will append all the elements greater than the chosen pivot

# with this for loop we are looking for every element smaller than the pivot and appending them to smallerQ
    for element in array: 
        if element < q and element != q:
            smallerQ.append(element)

# with this for loop we are looking for every element greater than the pivot and appending them to greaterQ
    for element in array:
        if element > q:
            greaterQ.append(element)

# we are now creating and printing a permutated array B given by the sum of smallerQ, the pivot and greaterQ
    B = smallerQ + [q] + greaterQ
    print(*B)

n = 9
numbersA = '7 2 5 6 1 3 9 4 8'
numbers_listA = numbersA.split()
arrayA = [int(num) for num in numbers_listA]

two_way_partition(arrayA)