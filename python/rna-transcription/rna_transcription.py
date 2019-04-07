def to_rna(dna_strand):
    compliment = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(map(lambda x: compliment[x], list(dna_strand)))

