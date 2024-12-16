#NCBI acess assignment

from Bio import Entrez, SeqIO
import sys
import csv
from datetime import datetime
import os

Entrez.email = "santiago.mon.1996@gmail.com"


print("Please provide the following:")
print("python ncbi.py database TERM(word or id number) type of document(gb, abstract or fasta) Number of items")
import sys
print(sys.argv)

try:
    database = str(sys.argv[1])
    search_term = str(sys.argv[2])
    file_type = str(sys.argv[3])
    number_of_items = int(sys.argv[4])
except:
    print("Data is lacking, try providing all the required data")
    exit()



handle = Entrez.esearch(db=database, term=search_term, retmax=number_of_items) 
# data = handle.read()
search_results = Entrez.read(handle)

handle.close()

ids = search_results["IdList"]
total_found = int(search_results["Count"])

records = []
i=0
for id in ids:
    try:

        if file_type == "abstract":  
            efetch_handle = Entrez.efetch(db=database, id=id, rettype="abstract", retmode="text")
            abstract = efetch_handle.read()
            filename = f"{search_term}_{i}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(abstract)
            print(filename)
            i=i+1

        else: # Handle other file types (like: gb, fasta)
            efetch_handle = Entrez.efetch(db=database, id=id, rettype=file_type, retmode="text")
            record = SeqIO.read(efetch_handle, file_type)
            records.append(record)  
            efetch_handle.close()

    except Exception as e:
        print(f"Error retrieving record {id}: {e}")


if file_type != "abstract":  
    for i,record in enumerate(records):
        filename = f"{search_term}_{i}.{file_type}"
        with open(filename, "w") as fh:
            SeqIO.write(record, fh, file_type)
        print(filename)

for i, record in enumerate(records):
    filename = f"{search_term}_{i}.{file_type}"
    with open(filename, "w") as fh:
        SeqIO.write(record, fh, file_type)
    print(filename)



current_date = datetime.now().strftime("%Y-%m-%d")
csv_data = [[current_date, database, search_term, number_of_items, total_found]]

file_exists = os.path.isfile("ncbi_metadata.csv") 

with open("ncbi_metadata.csv", "a", newline="") as csvfile:  
    writer = csv.writer(csvfile)
    if not file_exists: 
        writer.writerow(["Date", "Database", "Search Term", "Items Requested", "Total Found"])
    writer.writerows(csv_data)


print("Metadata appended to ncbi_metadata.csv")

print("\nCSV Data:")
try:
    with open("ncbi_metadata.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError: 
    print("ncbi_metadata.csv not found.")