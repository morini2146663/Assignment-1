'''
DNA exercise

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

'''
# s is the DNA string from which we want to count how many times each base occurs
s ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# we define the 4 counter for keeping tracks of the bases
counterA = 0
counterC = 0
counterG = 0
counterT = 0

# in the for loop we are checking each base and increasing the respective counter as the loop proceeds 
for element in s:
    if element == 'A':
        counterA += 1
    elif element == 'C':
        counterC +=1
    elif element == 'G':
        counterG +=1
    else:
        counterT += 1
print (counterA, counterC, counterG, counterT)