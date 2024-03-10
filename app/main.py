from fastapi import FastAPI
import datetime
import pymongo
from elasticsearch import Elasticsearch
app = FastAPI()
es = Elasticsearch(['elasticsearch:9200'])


@app.get('/time')
async def time():

    client = pymongo.MongoClient('mongodb://mongodb:27017/')
    db = client['data']
    collection = db['time']
    current_time = datetime.datetime.now()
    collection.insert_one({'time': current_time})
    es.index(index='time_index', body={'time': current_time.isoformat()})
    return {'time': current_time}
