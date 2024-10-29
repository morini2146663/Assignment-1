'''
HS exercise

Given: A positive integer n≤10^5 and an array A[1...n] of integers from -10^5 to 10^5.

Return: A sorted array A
'''

# we define a function, 'create_heap', which is able create a correct heap
def create_heap(A, n, i):
    largest_node = i                                                     # we find the largest node 
    left_son = 2 * i                                                     # we find its left son 
    right_son = 2 * i + 1                                                # we find its right son

# we now compare the largest node with its sons
    if left_son <= n and A[left_son - 1] > A[largest_node -1]:           # if the left son is inside the array and bigger than largest node
        largest_node = left_son                                          # it becomes the largest node
    
    if right_son <= n and A[right_son - 1] > A[largest_node - 1]:        # if the right son is inside the array and bigger than largest node
        largest_node = right_son                                         # it becomes the largest node
    
    if largest_node != i:                                                # if largest node is no longer the largest
        A[i - 1], A[largest_node - 1] = A[largest_node - 1], A[i - 1]    # we swap it with the bigger one
        create_heap(A, n, largest_node)                                  # we recall the function to compute the swaps until we have created a correct heap

# with the function, 'max_heap', we move back inside the array and by recalling  
# the previous function we check if the array follows the maximum heap rules
def max_heap(A):
    n = len(A)
    for i in range(n //2, 0, -1):
        create_heap(A, n, i)

# with the function, 'heap_sort', we recall 'max_heap' to make sure that the array is a maximum heap
# then we move the biggest node to the end of the array and reduce the heap by 1 unit 
# lastly we recall 'create_heao' again to restore the maximum heap in the riduced array
def heap_sort(A):
    n = len(A)
    max_heap(A)

    for i in range(n, 1, -1):
        A[i-1], A[0] = A[0], A[i-1]
        create_heap(A, i-1, 1)

n = 9
numbers = '2 6 7 1 3 5 4 8 9'
a = [int(num) for num in numbers.split()]
heap_sort(a)
print(*a)