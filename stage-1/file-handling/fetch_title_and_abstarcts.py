import os
from urllib.request import urlopen
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv() 

Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"

stream = Entrez.esearch(db="pubmed", term="PfDHFR (Plasmodium falciparum dihydrofolate reductase)", retmax="10")
records = Entrez.read(stream)
records_ids = records["IdList"]

for id in records_ids:
    paper_stream = Entrez.esummary(db="pubmed", id=id)
    paper_summary = Entrez.read(paper_stream)
    paper_stream.close()
    paper_title = paper_summary[0]["Title"]
    
    abstract_stream = Entrez.efetch(db="pubmed", id=id, rettype="abstract", retmode="text")
    abstract_content = abstract_stream.read()
    abstract_stream.close()
    
    print(f"| ID : {id} | Title : {paper_title} | Abstarct : {abstract_content} ")
    
    
