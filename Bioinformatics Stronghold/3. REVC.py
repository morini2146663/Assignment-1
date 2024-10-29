'''
REVC exercise

Given: A DNA string of length at most 1000 bp.

Return: The reverse complement t of s.
'''

# t is the DNA stirng we want to find the complementary to
t = 'AAAACCCGGT'

# reverse is a new variable we are creating to reverse the t DNA string 
reverse = t[::-1]

# we now define each base in order to find its complementary 
element1 = 'A'
element2 = 'T'
element3 = 'G'
element4 = 'C'

# complement is an empty string in which we are going to add the complementary bases we'll find through the for loop
complement = ''

# in the for loop we are checking each base in the string t and substituing it with its complementary 
for element in reverse:
    if element == element1:
        complement += 'T'
    elif element == element2:
        complement += 'A'
    elif element == element3:
        complement += 'C'
    else:
        complement += 'G'
print (complement)