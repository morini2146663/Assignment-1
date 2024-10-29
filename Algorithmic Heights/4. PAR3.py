'''
PAR3 exercise

Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5.

Return: An array B[1...n] such that it is a permutation of A and there are indices 1≤q≤r≤n
        such that B[i]<A[1] for all 1≤i≤q-1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n
'''

# we define a function through which we can permutate the array A following the given instructions
def three_way_partition(array):
    q = array[0]                               # q is our pivot, it is the element at index 0 in the array A
    smallerQ = []                              # smallerQ is an empty list to which we will append all the elements smaller than the chosen pivot
    equalQ = []                                # equalQ is an empty list to which we will append all the elements equal to the chosen pivot
    greaterQ = []                              # greaterQ is an empty list to which we will append all the elements greater than the chosen pivot

# with the for loop we compare each element of the array A with the pivot and we append it to the correct empty list
    for element in array:
        if element < q:                        # if the element is smaller than the pivot we append it to smallerQ
            smallerQ.append(element)
        elif element == q:                     # if the element is equal to the pivot we append it to equalQ
            equalQ.append(element)
        else:                                  # if the element is greater than the pivot we append it to greaterQ
            greaterQ.append(element)

# we are now creating  ad printing a permutated array B given by the sum of smallerQ, equalQ and greaterQ
    B = smallerQ + equalQ + greaterQ
    print (*B)

n = 9
numbersA = '4 5 6 4 1 2 5 7 4'
numbers_listA = numbersA.split()
arrayA = [int(num) for num in numbers_listA]

three_way_partition(arrayA)