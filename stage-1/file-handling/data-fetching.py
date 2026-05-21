import os
from Bio import Entrez
from dotenv import load_dotenv

load_dotenv() 

Entrez.api_key = os.getenv("ENTREZ_API_KEY")
Entrez.email = os.getenv("ENTREZ_EMAIL")
Entrez.tool = "synaptic-1"

stream = Entrez.efetch(db="pmc", id="13136524", rettype="medline", retmode="text")
# for abstract rettype: abstract and retmode : text

print(stream.read())
stream.close()