'''
PROT exercise 

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''
# string is the RNA string we want to translate into a protein string
string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

# codon_table is a dictionary that tells us which codon corresponds to which amino acid
codon_table = {
           "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}


# we now define a function, 'RNA2PROT', through which we are able to check every codon and associate to each of them its corresponding amino acid
def RNA2PROT(string):
    protein = ''
    for element in range (0, len(string), 3): 
        codon = string[element:element+3]       # we take into consideration a string up to lenght 3
        aminoacid = codon_table.get(codon, "")  # we associate to each amino acid its corresponding codon by getting it from codon_table 
        if aminoacid =='Stop':                  # if the corresponding amino acid is 'Stop' 
            break                               # the loop breaks the translation
        protein += aminoacid
    print (protein)

string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
protein = RNA2PROT (string)