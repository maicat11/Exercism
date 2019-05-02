def proteins(strand):

    protein_dict = {'AUG': ['Methionine'],
                    'UUU': ['Phenylalanine'],
                    'UUC': ['Phenylalanine'],
                    'UUA': ['Leucine'],
                    'UUG': ['Leucine'],
                    'UCU': ['Serine'],
                    'UCC': ['Serine'],
                    'UCA': ['Serine'],
                    'UCG': ['Serine'],
                    'UAU': ['Tyrosine'],
                    'UAC': ['Tyrosine'],
                    'UGU': ['Cysteine'],
                    'UGC': ['Cysteine'],
                    'UGG': ['Tryptophan'],
                    'UAA': [],
                    'UAG': [],
                    'UGA': []
                    }

    protein_list =[]
    for i in range(0, len(strand), 3):
        if protein_dict[strand[i:i+3]] == []:
            break
        protein_list += protein_dict[strand[i:i+3]]

    return protein_list
