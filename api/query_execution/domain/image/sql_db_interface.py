from abc import ABC, abstractmethod
from typing import Any, List, Tuple

from query_execution.domain.image.image_entity import ImageEntity


class SQLDBInterface(ABC):
    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def get_image_path(self, image_id: str) -> str:
        pass

    @abstractmethod
    def save_image(self, file_name: str, image_location: str) -> ImageEntity:
        pass
