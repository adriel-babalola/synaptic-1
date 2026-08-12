import os
import csv
from urllib.request import urlopen
# Intsall biopython and dotenv to use
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv()

# getting the porj directory, and creating my save path and save name
project_dir = os.path.dirname(__file__)
data_path = os.path.join(project_dir, "output", "results.csv")

print("__ Fetch Started __")

# Telling Entrez who i am
Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"


# Serach Query
query="""
PfDHFR[Title/Abstract] AND (inhibitor[Title/Abstract] OR docking[Title/Abstract] OR "binding affinity"[Title/Abstract]) AND antimalarial[Title/Abstract] AND "journal article"[pt] NOT "clinical trial"[pt] AND "free full text"[filter] AND 2015:2026[dp]
""" 

# Initial search to get the IDs
stream = Entrez.esearch(db="pubmed", term=query, retmax="30")
records = Entrez.read(stream)
records_ids = records["IdList"]

title = ["ID", "TITLE", "ABSTARCT"]

# data to append
info_to_append = [title,]

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
    abstract_content = abstract_content.replace("\n", " ")
    abstract_stream.close()
    
    info = [id, paper_title, abstract_content]
    info_to_append.append(info)
    
# Writing my search into a csv file : reults.csv
file = open(data_path, "a", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerows(info_to_append)
file.close()

print("__ Fetch Successful __")