dna = input("Provide DNA template:" )

def transcription(dna):
    mrna = ""
    for base in dna:
        if base == "A":
            mrna += "U"
        elif base == "T":
            mrna += "A"
        elif base == "G":
            mrna += "C"
        elif base == "C":
            mrna += "G"
    return mrna
print(transcription(dna))
