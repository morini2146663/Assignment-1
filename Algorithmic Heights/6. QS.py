'''
QS exercise

Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5.

Return: A sorted array A[1...n].
'''

def qs (array):
    if len(array) <= 1:
        return array
    else: 
        q = array[len(array)//2]                                    # q is the pivot, it is the middle element of the array
        smallerQ = [element for element in array if element < q]    # these are the elements smaller than the chosen pivot
        equalQ = [element for element in array if element == q]     # these are the elements equal to the chosen pivot
        greaterQ = [element for element in array if element > q]    # these are the elements greater than the chosen pivot
        return qs(smallerQ) + equalQ + qs(greaterQ)                 # we create a sorted list in ascending order 

n = 7
numbers = '5 -2 4 7 8 -10 11'
numbers_list = numbers.split()
a = [int(num) for num in numbers_list]

QuickSort = qs(a)
print(*QuickSort)