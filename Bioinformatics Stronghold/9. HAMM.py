'''
HAMM exercise

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance between s and t
'''

# we define a funciton, 'HammingDistance', through which we can calculate how many bases do the s and t DNA strings differ from one another 

def HammingDistance(s, t):
    result = 0
    index = 0

# the while loop allows us to countinously check the string, increasing each time the index we are checking
    while index < len (s):
        if s [index] == t [index]:     # if the element at a specified index in the s stirng is equal to the element at said index in the t string 
            result += 0                # the loop adds nothing to the result 
        else:                          # if instead at the same index the 2 elements are different
            result += 1                # the loop adds 1 to the result
        index += 1                     # we proceed to the following index
    print (result)

s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
HammingDistance (s, t)