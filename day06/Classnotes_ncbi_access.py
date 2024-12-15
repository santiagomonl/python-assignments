#Classnotes ncbi access

#API usually send you back JSON structures, but one can use a library in python
#Biopython

from Bio import Entrez
Entrez.email = "email" #have to add the email

term = "Cypripedioideae[Orgn] AND matK[Gene]"

handle = Entrez.esearch(db="nucleotide", term=term, idtype="acc", retmax=30)
record = Entrez.read(handle)
print(record["Count"])       # 538
print(record["IdList"])      # ['MK792700.1', 'MK792699.1', 'MK792698.1', ..., 'MK792681.1']
print(len(record["IdList"])) # 30
handle.close()


#Now to download the nucleotides
from Bio import Entrez, SeqIO

Entrez.email = "email" #have to add the email

#doc_id = 'MK792700.1'
doc_id = "EU490707"

# rettype="fasta"
handle = Entrez.efetch(db="nucleotide", id=doc_id, rettype="gb", retmode="text")
data = handle.read()
handle.close()
#print(data)

filename = "temp.data"
with open(filename, 'w') as fh:
    fh.write(data)

file_type = "genbank"
for seq_record in SeqIO.parse(filename, file_type):
    print(seq_record.id)
    print(repr(seq_record.seq))  # A short part of the sequence
    print()
    print(seq_record.seq)   # The full sequence
    print()
    print(len(seq_record.seq))
    print()
    print(seq_record.name)
    print()
    print(seq_record.annotations)
    #print()
    #print(dir(seq_record))