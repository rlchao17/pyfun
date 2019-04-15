def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotide = 0
    for char in dna:
        if char == nucleotide:
            num_nucleotide = num_nucleotide + 1
    return num_nucleotide

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) != -1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence dna is valid (that is, it contains
    no characters other than 'A', 'T', 'C' and 'G').
    
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('atcg')
    False

    """
    valid_sequence = True
    for char in dna:
        if not char in 'ATCG':
            valid_sequence = False
            
    return valid_sequence

def insert_sequence(dna1, dna2, position):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 into dna1 at the given
    position.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 5)
    'CCGGAT'

    """
    return dna1[:position] + dna2 + dna1[position:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    
    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given dna sequence.
    
    >>> get_complementary_sequence('AT')
    'TA'

    """
    comp_dna = ''
    for nucleotide in dna:
        comp_dna = comp_dna + get_complement(nucleotide)

    return comp_dna

    
