# Use PrimerBank (“google PrimerBank”) to look up PCR primers for your favorite
# gene
#       Use Search By: “NCBI Gene Symbol”, Species: “Human” to find PCR primers for
#       your gene. 
#       Write a program to compute the reverse complement sequence of both the
#       forward and reverse primer (in one program).
# Gene = HERC2

# Primers for Primer Pair 1
primer = 'TCGCCTCGACTCCAAATGG'
reversePrimer = 'TCTTTGTTCCACTTGGTTCGAC'

# function complement returns complementary nucs
def complement(nuc):
    if nuc in 'Aa':
        comp = 'T'
    elif nuc == 'T' or nuc == 't':
        comp = 'A'
    elif nuc == 'C' or nuc == 'c':
        comp = 'G'
    elif nuc == 'G' or nuc == 'g':
        comp = 'C'
    else:
        comp = nuc
    return comp

# function reverse_complement returns reversed and complemented primers
def reverse_complement(primers):
    reverse_comp = '' # empty string to build reverse complement by concatenating nucs
    for nuc in primers: # iterate through sequence
        reverse_comp = complement(nuc) + reverse_comp  # add nucs to beginning of string instead of end of string
    return reverse_comp

# Output the primers and nucs of reverse_complement
print("Reverse complement of",primer,"is",reverse_complement(primer))
print("Reverse complement of",reversePrimer,"is",reverse_complement(reversePrimer))
