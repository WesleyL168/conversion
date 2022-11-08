dna = input("Please provide template: ")
dna = dna.upper()

def complement(dna):
    complement = ""                 #creates blank complement
    for base in dna:
        if base == "A":             # A to T
            complement += "T"
        elif base == "T":           # T to A
            complement += "A"
        elif base == "C":           # C to G
            complement += "G"
        elif base == "G":           # G to C
            complement += "C"
    return complement
print(complement(dna))
