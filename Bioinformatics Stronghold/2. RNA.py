'''
RNA exercise

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.'''

# we define the 2 bases we are interested in 
element1 = 'T'
element2 = 'U'

# we define a function, 'DNA2RNA', that is able to check every base in the DNA string,
def DNA2RNA(t):
    result = ''
    for element in t:
        if element == element1:   # if it encounters an 'T' base it  
            result += element2    # automatically changes it into a 'U' base
        else:
            result += element     # if not it just adds the elemnt to the result string
    print (result)
        
in_DNA = 'GATGGAACTTGACTACGTAAATT'
DNA2RNA (in_DNA)