from Bio import Entrez, SeqIO
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

Entrez.email = "willingram02@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_001172751, JX308819, JX475045, NM_000641, JX308817, JQ867082, NM_002124, JQ796071, NM_001271262, FJ817486"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

lengths = []
for i in range(len(records)):
    lengths.append(len(records[i].seq))

# get index of minimum length
min_len_index = lengths.index(min(lengths))

print(">" + records[min_len_index].description)
print(records[min_len_index].seq)