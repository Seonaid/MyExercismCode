def to_rna(dna_strand):
    dna_rna={'C':'G', 'G':'C', 'T':'A', 'A':'U'}
    return ''.join([dna_rna[letter] for letter in dna_strand])

