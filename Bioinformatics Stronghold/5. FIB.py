'''
FIB exercise

Given: Positive integers n ≤ 40 and k ≤ 5

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair 
and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

# we define a funcion, 'fib', that is able to check the value of n and calculate the corresponding numbers of rabbit pairs

def fib(n, k):
    if n <= 2:         # if n is smaller than or equal to 2 than we'll only have 1 pair 
        return 1       # of rabbits because the reproduction starts i  the 3rd month
    else:
        return fib(n-1,k) + k * fib(n-2,k) 
# when n is greater than 2 the number of rabbit pairs is calculate as the sum between the pairs we had the previous month and
# the product of k (numer of pairs each pair of rabbits produces each month) and the number of pairs we had 2 months before
    
n = 5
k = 3
rabbits = fib(n,k)
print (rabbits)