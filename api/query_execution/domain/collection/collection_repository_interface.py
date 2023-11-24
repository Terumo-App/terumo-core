from abc import ABC, abstractmethod
from typing import Any, List, Union

from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)


class CollectionRepositoryInterface(ABC):
    @abstractmethod
    def list_collections(self, collection_name: str) -> List[CollectionEntity]:
        pass

 