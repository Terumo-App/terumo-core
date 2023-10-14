from typing import List

from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)
from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepository,
)


class ListCollectionUseCase:
    def __init__(self, collection_repository: CollectionRepository):
        self._collection_repository = collection_repository

    def execute(self) -> List[CollectionEntity]:
        collections = self._collection_repository.list_collections()
        return collections
