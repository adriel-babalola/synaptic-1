import os
from urllib.request import urlopen
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv() 

Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"

stream = Entrez.efetch(db="pubmed", id="41282777", rettype="abstract", retmode="text")
content = stream.read()
print(content)
stream.close()