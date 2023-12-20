import os

from pymilvus import (
    Collection,
    CollectionSchema,
    DataType,
    FieldSchema,
    connections,
    utility,
)

MIULVAS_HOST = os.environ.get('MIULVAS_HOST')
MIULVAS_HOST = MIULVAS_HOST if MIULVAS_HOST else 'localhost'


def connect_miulvas_db():
    connections.connect(
        alias='default',
        user='username',
        password='password',
        host=MIULVAS_HOST,
        port='19530',
    )


def create_collection(collection_id):
    coll_name = '_' + str(collection_id)

    if utility.has_collection(coll_name):
        collection = Collection(coll_name)
        collection.drop()

    vector_dimension = 6
    vector_id = FieldSchema(
        name='vector_id',
        dtype=DataType.INT64,
        descrition='int64',
        is_primary=True,
    )
    vector = FieldSchema(
        name='vector',
        dtype=DataType.FLOAT_VECTOR,
        descrition='semantic vector',
        dim=vector_dimension,
    )
    schema = CollectionSchema(
        fields=[vector_id, vector],
        description='collection_description',
        enable_dynamic_field=True,
    )
    collection = Collection(name=coll_name, schema=schema)

    # index_params = {
    #     'metric_type': 'L2',  # Euclidean distance (L2 norm)
    #     'index_type': 'IVF_FLAT',
    #     'params': {'nlist': 1024},
    # }

    index_params = {
    "metric_type":"COSINE", # (Cosine similarity)
    "index_type":"FLAT", # https://milvus.io/docs/index.md
    "params":{"nlist":1024}
    }
    collection.create_index(field_name='vector', index_params=index_params)

    return collection


def search(collection_id, vector, top_k=100):
    coll_name = '_' + str(collection_id)

    if not utility.has_collection(coll_name):
        raise ValueError('Collection does not exist')

    collection = Collection(coll_name)

    # search_params = {
    #     'metric_type': 'L2',
    #     'offset': 5,
    #     'ignore_growing': False,
    #     'params': {'nprobe': 10},
    # }
    search_params = {
    "metric_type": "COSINE", 
    "offset": 0, 
    "ignore_growing": False, 
    }


    results = collection.search(
        data=[vector],
        anns_field='vector',
        # the sum of `offset` in `param` and `limit`
        # should be less than 16384.
        param=search_params,
        limit=top_k,
        expr=None,
        # set the names of the fields you want to
        # retrieve from the search result.
        output_fields=['vector_id','vector'],
        consistency_level='Strong',
    )

    return results
