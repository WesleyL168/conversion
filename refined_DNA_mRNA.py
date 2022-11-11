dna = input("Provide DNA template:")
dna = dna.upper()

def transcription(dna):
  diction = {"A": "U", "T": "A", "G": "C", "C": "G"}
  mrna = ""
  for base in dna:
    mrna += diction[base]
  return mrna

print(transcription(dna))
