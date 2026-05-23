import os
import csv
from urllib.request import urlopen
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv() 

# Telling Entrez who i am
Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"

# Initial search to get the IDs
stream = Entrez.esearch(db="pubmed", term="PfDHFR (Plasmodium falciparum dihydrofolate reductase)", retmax="10")
records = Entrez.read(stream)
records_ids = records["IdList"]

# data to append
info_to_append = []

# Loop over IDs
for id in records_ids:
    # Obtain the title from the summary
    paper_stream = Entrez.esummary(db="pubmed", id=id)
    paper_summary = Entrez.read(paper_stream)
    paper_stream.close()
    paper_title = paper_summary[0]["Title"]
    # obtain the abstarct still using the id
    abstract_stream = Entrez.efetch(db="pubmed", id=id, rettype="abstract", retmode="text")
    abstract_content = abstract_stream.read()
    abstract_stream.close()
    
    info = [id, paper_title, abstract_content]
    info_to_append.append(info)
    # print(info)
    
    # print(f"| ID : {id} | Title : {paper_title} | Abstarct : {abstract_content} ")
    
print(info_to_append)
    
    
