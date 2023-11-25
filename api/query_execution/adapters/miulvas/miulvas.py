import os
from typing import Any, List, Tuple
from pymilvus import Collection, connections, utility
from query_execution.domain.image.vector_db_interface import VectorDBInterface
import logging

logger = logging.getLogger(__name__)

class MilvusDBImp(VectorDBInterface):
    def __init__(self):
        self.milvus_host = os.environ.get('MIULVAS_HOST')
        self.milvus_host = (
            self.milvus_host if self.milvus_host else 'localhost'
        )
        print(self.milvus_host)
        self.setup()

    def setup(self):
        connections.connect(
            alias='default',
            user='username',
            password='password',
            host=self.milvus_host,
            port='19530',
        )

    def list_collections(self,)->List[str]:
        return utility.list_collections()

    def search(self, collection_id, vector, top_k=100):
        coll_name = '_' + str(collection_id)

        if not utility.has_collection(coll_name):
            raise ValueError('Collection does not exist')

        collection = Collection(coll_name)
        collection.load()

        search_params = {
            'metric_type': 'L2',
            'offset': 5,
            'ignore_growing': False,
            'params': {'nprobe': 10},
        }
        print(f'--------------vector')
        print(f'---: {vector}')

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
            output_fields=['vector_id'],
            consistency_level='Strong',
        )
        # collection.release()

        return results[0].ids, results[0].distances
