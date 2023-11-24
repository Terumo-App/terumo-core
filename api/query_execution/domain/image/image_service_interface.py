from abc import ABC, abstractmethod
from typing import Any, List

from PIL import Image
from query_execution.domain.image.image_entity import (
    ImageFileEntity,
    ImageMetaDataEntity,
)


class ImageServiceInterface(ABC):
    @abstractmethod
    def load_image(self, image_path: str) -> Image.Image:
        pass

    # @abstractmethod
    # def proccess_image(self, image:Image.Image)-> Any:
    #     pass
    @abstractmethod
    def extract_attributes(self, image: bytes) -> List[int | float]:
        pass

    @abstractmethod
    def consolidate_image_info(
        self, img_ids: List[int], img_distances: List[str]
    ) -> List[ImageMetaDataEntity]:
        pass
