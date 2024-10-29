'''
SUBS exercise

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of  s.
'''

# we define a funciton, 'subs', that is able to check when a particular motif t is encountered in a DNA string s

def subs(s, t):
    position = []                             # position is an empty list to which we will append the motif's starting indexes
    for element in range(len(s)):             # if all the element from an index to index+n (that correspond to the motif lenght)
        if t == s[element: element+len(t)]:   # are identical to elements of the motif
            position.append(element+1)        # we add the starting index of the motif to the empty list 
    print (*position)

s = 'GATATATGCATATACTT'
t = 'ATAT'

subs (s,t)