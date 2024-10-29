'''
IPRB exercise

Given: Three positive integers k, m and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing 
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

from math import comb

# we define a function, mendels_first_law, through which we can calculate the probability of randomly obatining a dominant induvidual 
def mendels_first_law(k, m, n):
    # k -> AA organisms
    # m -> Aa organisms
    # n -> aa organisms

    # total is a new variable that corresponds to the total number of possible children genotypes
    total = 4*comb(k+m+n, 2)

    # total rec is the number combination of recessive child genotypes
    # n x n -> 4/4 recessive
    # n x m -> 2/4 recessive
    # m x m -> 1/4 recessive
    # k x any -> 0/4 receesive 
    total_rec = 4*comb(n, 2) + 2*n*m + comb(m,2)

    # the proability of having a dominant allele, therefore a dominat phenotype is 
    # 1 (maximum value when talking about probabilities) - total_rec
    print (1 - total_rec/total)

k, m, n = 2, 2, 2
mendels_first_law (k, m, n)