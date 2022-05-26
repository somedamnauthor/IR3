# Setup

- Install elastic search, and run service from terminal
	- If re-installing, remove the /var/lib/elasticsearch/nodes directory
- pip install --upgrade pip
- pip install -r requirements.txt

# Notebooks
- ES_Interactions.ipynb: Gets the query results from elastic search
- reranking.ipynb: Calculates document ranks per query according to BM25 variants
- metrics.ipynb: Calculates ndcg, precision and mean reciprocal rank  
