from abc import ABC, abstractmethod
from collection_management.domain.image.image_entity import (
    ImageEntity,
)
from typing import List

# TODO: Define properly the data structure that each method should return

class ImageRepositoryInterface(ABC):
#     @abstractmethod
#     def create_collection(self, collection_name: str) -> int: pass

#     @abstractmethod
#     def delete_collection(self, collection_name: str) -> int: pass

#     @abstractmethod
#     def find_collection_by_name(self, collection_name: str) -> bool: pass

    @abstractmethod
    def list_images(self, collection_id: int) -> List[ImageEntity]: pass

#     @abstractmethod
#     def add_user(self, username: int, collection_name: str) -> bool: pass

#     @abstractmethod
#     def remove_user(self, username: int, collection_name: str) -> bool: pass
