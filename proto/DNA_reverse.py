## Converts DNA template to reverse complement

dna = input("Please provide template: ")
dna = dna.upper()

def reversed(dna):
    return dna[::-1]
reversed_dna = reversed(dna)

def complement(dna):
    complement = ""                 #creates blank complement
    for base in reversed_dna:
        if base == "A":             # A to T
            complement += "T"
        elif base == "T":           # T to A
            complement += "A"
        elif base == "C":           # C to G
            complement += "G"
        elif base == "G":           # G to C
            complement += "C"
    return complement
print("Reversed complement DNA (5' to 3'): " , complement(dna))

