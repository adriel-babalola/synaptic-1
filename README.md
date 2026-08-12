# synaptic-1

This is for the developement of synaptic-1 a resaerch triaging, repurposing and validation tool, with the purpose to cut down time spent on reaserch and simulation of drugs.

**Intrctuions**

# clone the repo 
git clone https://github.com/adriel-babalola/synaptic-1.git

# Move into a stage directory 
cd to a particular stage 
cd stage-1 
cd file-handiling

# 2. Create the virtual environment (if not already done)
python3 -m venv venv

# 3. Activate the environment
<!-- For Linux -->
source venv/bin/activate

or ./venv/bin/activate

# 4. Install all dependencies
pip install -r requirements.txt













### Day 1 : 
I explored pymed and querying PubMed to get papers

### Day 2 : 
went with biopython which alot more easier. I ran into issues with biopython for the majority of today, turns out it was a linter issue. After spending hours on the documentation i was able to create a working paper title fetcher script by id, all without AI touching my code code.🥳🥳, but i used it to find out why my env wasn't loading though

## Day 3 :
Today I was able to extract abstracts of research papers from the pub med central database.
But I just realized I don't know what exactly I'm looking for in a research paper for it too work. so i am going to start shifting more my time into understanding papers that can solve the porblem, and what exactly am i supposed to look for in a paper. Cause i've been seeing alot of big grammars and names that are confusing me.