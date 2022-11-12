## Converts DNA coding strand to protein polypeptide

# translation to mRNA
dna = input("Provide DNA template:")
dna = dna.upper()

def transcription(dna):
  diction = {"A": "U", "T": "A", "G": "C", "C": "G"}
  mrna = ""
  for base in dna:
    mrna += diction[base]
  return mrna

mrna = transcription(dna)

# mRNA to protein
# Codon table
codons = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I",
    "AUC": "I", "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "UCU": "S", "UCC": "S",
    "UCA": "S", "UCG": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T", "ACC": "T", "ACA": "T",
    "ACG": "T", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D",
    "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W", "CGU": "R", "CGC": "R",
    "CGA": "R", "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G",
    "GGG": "G"
}

def translate(mrna):
    protein = ""
    if len(mrna)%3 == 0:
        for i in range(0, len(mrna), 3):
            codon = mrna[i:i+3]
            protein += codons[codon]
    elif len(mrna)%3 != 0:
      print("Check sequence, interuption detected.")
    return protein

print(translate(mrna))
