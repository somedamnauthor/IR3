# import ir_datasets
# dataset = ir_datasets.load("clinicaltrials/2021")

#Test elasticsearch

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, body=doc)
print('\n Response Result:',resp['result'])

resp = es.get(index="test-index", id=1)
print('\n Response Source:',resp['_source'])

es.indices.refresh(index="test-index")

resp = es.search(index="test-index", body={"match_all": {}})
print("\nGot %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])