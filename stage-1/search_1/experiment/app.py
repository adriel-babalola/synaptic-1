import os
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv() 

Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"

# To Get the Records
stream = Entrez.esearch(db="pubmed", term="PfDHFR (Plasmodium falciparum dihydrofolate reductase)", retmax="10")
records = Entrez.read(stream)
records_ids =  records["IdList"]

for id in records_ids:
    stream = Entrez.esummary(db="pubmed", id=id)
    exact_record = Entrez.read(stream)
    exact_record_title = exact_record[0]["Title"]
    print(f"| Record Id : {id} | Record Title : {exact_record_title}")

# To get a specific record
# We dont need to search again since we have the id 
# stream = Entrez.esearch(db="pubmed", term="Potential Anti Malaria Drugs", retmax="30")
# stream = Entrez.esummary(db="pubmed", id="42107903")
# record = Entrez.read(stream)

# print(record[0]["Title"])

stream.close()


