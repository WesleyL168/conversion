dna = input("Provide template strand:")
dna = dna.upper()
dna = dna[::-1]

def reverse_complement(dna):
  diction = {"A": "T", "T": "A", "G": "C", "C": "G"}
  complement = ""
  for base in dna:
    complement += diction[base]
  return complement

print(reverse_complement(dna))

    
