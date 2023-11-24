from abc import ABC, abstractmethod
from typing import Any, List, Tuple

from query_execution.domain.image.image_entity import ImageEntity


class VectorDBInterface(ABC):
    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def search(
        self, collection_id: int, vector: List[int | float], top_k: int
    ) -> Tuple[List[int], List[str]]:
        pass

    @abstractmethod
    def list_collections()->List[str]:
        pass