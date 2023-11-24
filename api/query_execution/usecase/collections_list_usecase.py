from typing import List
from query_execution.adapters.collection_repository_imp import CollectionRepositoryImp
from query_execution.domain.image.vector_db_interface import VectorDBInterface

from query_execution.domain.collection.collection_entity import (
    CollectionEntity,
)
from query_execution.domain.collection.collection_repository_interface import (
    CollectionRepositoryInterface,
)


class ListCollectionUseCase:
    _collection_repository: CollectionRepositoryInterface
    _vector_db_repositiry: VectorDBInterface

    def __init__(self, 
                 collection_repository: CollectionRepositoryInterface,
                 vector_db_repository: VectorDBInterface
                 ):
        self._collection_repository = collection_repository
        self._vector_db_repository = vector_db_repository

    def execute(self) -> List[CollectionEntity]:
        user_collections = self._collection_repository.list_collections()
        milvus_collections = self._vector_db_repository.list_collections()
        colls = self._get_collections_available(user_collections, milvus_collections)
        return colls


    def _get_collections_available(self, user_collections: List[CollectionEntity], milvus_collections:List[str])->List[CollectionEntity]:
        milvus_coll_ids = [int(_id[1:]) for _id in milvus_collections]

        coll_avail = []
        for user_coll in user_collections:
            if user_coll.id in milvus_coll_ids:
                coll_avail.append(user_coll)

        return coll_avail