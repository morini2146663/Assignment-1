''' 
PS exercise

Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5, a positive integer k≤1000.

Return: The k smallest elements of a sorted array  A
'''

# we define a function thorugh which we sort in scending order a given array and than 
# we print k smallest elements by extracting them from the sorted array
def partial_sort(array, index):
    sorted_array = sorted(array)       # we sort the array
    if 0 <= index < len(array):        # if the given index is bigger than or equal to 0 and smaller than the maximum index supported by the array
        print (*sorted_array[0:index]) # we print the k smallest elements by extracting all the elements from index 0 to index k

n = 10
k = 3
numbers = '4 -6 7 8 -9 100 12 13 56 17'
numbers_list = numbers.split()
a = [int(num) for num in numbers_list]

partial_sort(a, k)