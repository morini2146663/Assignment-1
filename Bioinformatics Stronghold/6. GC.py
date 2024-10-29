'''
GC exercie 

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''
#the 'fasta_parser' function is able to initialize data in FASTA format and returns its ID and label
def fasta_parser(data): 
    fasta_dict = {}                                      
    label = ''                                           

# with the for loop we check every line of the given data
    for line in data.splitlines():
        if line.startswith(">"):                         
            label = line[1:]  
            fasta_dict[label] =''  
        else:
            fasta_dict[label] += line 
    
    return fasta_dict

# the 'gc_content' function count the number of G and C elements and return their sum as a percentage
def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

# the 'find_highest_gc_content' function finds the highest gc content ID by recalling the gc_content function 
def find_highest_gc_content(data):
    highest_gc_label = ''
    highest_gc_content = 0.0
    
    for label, sequence in fasta_dict.items():
        gc = gc_content(sequence)
        if gc > highest_gc_content:
            highest_gc_content = gc
            highest_gc_label = label
    
    return highest_gc_label, highest_gc_content

dataset = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''

fasta_dict = fasta_parser(dataset)

label, gc_content_value = find_highest_gc_content(fasta_dict)

print(label)
print(f"{gc_content_value:.6f}")