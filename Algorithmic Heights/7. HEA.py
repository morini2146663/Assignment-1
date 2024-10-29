'''
HEA exercise

Given: A positive integer n≤10^5 and array A[1..n] of integers from -10^5 to 10^5.

Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].

'''

# we define a function, 'create_heap', that is able to create an heap
def create_heap(array):
    heap = [0]
    for element in array:
        heap.append(element)
        index = len(heap) - 1                                              # index of the appended element
        while heap[index // 2] < heap[index] and index // 2 > 0:           # we are now checking if the element is bigger than its 'parent' 
            heap[index], heap[index // 2] = heap[index // 2], heap[index]  # if it is, we swap them to have the smaller element as the 'son'
            index = index // 2                                             # by putting it at the partent's index (Bubble up process)
    return heap[1:]                                                        # we now delete the element at 0 index 

n = 5
numbers = '1 3 5 7 2'
numbers_list = numbers.split()
a = [int(num) for num in numbers_list]

heap = create_heap(a)
print (*heap)