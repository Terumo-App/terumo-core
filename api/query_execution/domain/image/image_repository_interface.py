from abc import ABC, abstractmethod
from typing import Any, List, Tuple

from query_execution.domain.image.image_entity import (
    ImageEntity,
    ImageFileEntity,
)


class ImageRepositoryInterface(ABC):
    @abstractmethod
    def search_similar_images(
        self, attributes: List[int], collection_id: int
    ) -> Tuple[List[int], List[str]]:
        pass

    @abstractmethod
    def persist_image_on_file_storage(self, image: ImageFileEntity) -> str:
        pass

    @abstractmethod
    def load_image_from_file_storage(self, image_path: str) -> bytes:
        pass
    
    @abstractmethod
    def get_image_path(self, image_id: str) -> str:
        pass

    @abstractmethod
    def persist_image_metadata(
        self, file_name: str, image_location: str
    ) -> ImageEntity:
        pass
