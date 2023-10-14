from abc import ABC, abstractmethod
from typing import Any, List, Union

from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)


class CollectionRepository(ABC):
    @abstractmethod
    def create_collection(
        self, collection_name: str
    ) -> Union[CollectionEntity, bool]:
        pass

    @abstractmethod
    def list_collections(self, collection_name: str) -> List[CollectionEntity]:
        pass

    @abstractmethod
    def find_collection_by_name(
        self, collection_name: str
    ) -> Union[CollectionEntity, bool]:
        pass

    # @abstractmethod
    # def delete_collection(self, collection_name: str) -> bool: pass

    # @abstractmethod
    # def add_user(self, username: int, collection_name: str) -> bool: pass

    # @abstractmethod
    # def remove_user(self, username: int, collection_name: str) -> bool: pass
