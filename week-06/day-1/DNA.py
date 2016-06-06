def reverse_complement(dna):
    nucleotids = {'T':'A', 'A':'T', 'C':'G', 'G':'C'}
    revList = []
    for i in dna:
        if i not in nucleotids:
            return "Invalid sequence"
        else:
            revList += nucleotids.get(i)
    s = ""
    newDNA = s.join(revList)
    newDNA = newDNA[::-1]
    return newDNA
         
print (reverse_complement("TTCCGGAA"))