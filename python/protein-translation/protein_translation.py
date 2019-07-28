def proteins(strand):
    proteins = []

    amino_acids={'AUG': 'Methionine','UUU':'Phenylalanine','UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','UCU':'Serine','UCC':'Serine','UCA':'Serine','UCG':'Serine','UAU':'Tyrosine','UAC':'Tyrosine','UGU':'Cysteine','UGC':'Cysteine','UGG':'Tryptophan','UAA':'STOP','UAG':'STOP','UGA':'STOP'}

    num_proteins = int(len(strand)/3)
    
    for i in range(num_proteins):
        proteins.append(amino_acids[strand[0:3]])
        strand = strand[3:]
        i == i+1

        if proteins[-1] == 'STOP': 
            del (proteins[-1])
            break            
    
    return proteins
