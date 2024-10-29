'''
MED exercise

Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5, a positive number k≤n.

Return: The k-th smallest element of A.
'''

# we define a function, 'median', thorugh which we sort in ascending order a given array and than we print k-th element by extracting it from the sorted array
def median(array, index):
    sorted_array = sorted(array)       # we sort the array
    if 0 <= index < len(array):        # if the given index is bigger than or equal to 0 and smaller than the maximum index supported by the array
        print (sorted_array[index-1])  # we print the element at said index-1 to obtain the element in position k

n = 11
k = 8

numbers = '2 36 5 21 8 13 11 20 5 4 1'
numbers_list = numbers.split()
a = [int(num) for num in numbers_list]

median (a, k)