import os
from typing import Any, List, Union

from config.environment import EnvironmentSettings
from PIL import Image
from query_execution.adapters.cytomine_server.cytomine import CytomineWrapper
from query_execution.adapters.binary_models.binary_extractor_imp import extract
from query_execution.domain.image.image_entity import (
    ImageFileEntity,
    ImageMetaDataEntity,
)
from query_execution.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)
from query_execution.domain.image.image_service_interface import (
    ImageServiceInterface,
)

ROOT_REFERENCE = os.getcwd()


class ImageServiceImp(ImageServiceInterface):
    _cytomine: CytomineWrapper
    _config: EnvironmentSettings

    def __init__(
        self, config: EnvironmentSettings, public_key: str, private_key: str
    ) -> None:
        self._cytomine = CytomineWrapper(config, public_key, private_key)
        self._config = config

    def load_image(self, image_path: str) -> Image.Image:
        return Image.open(image_path).convert('RGB')

    def extract_attributes(self, image_path: str) -> List[int | float]:
        # TODO IMPLEMENT GRPC CALL
        vector = extract(image_path)
        return vector
        # return [1, 0, 0, 1, 1, 0]

    def consolidate_image_info(
        self, img_ids: List[int], img_distances: List[str], collection_id: int
    ) -> List[ImageMetaDataEntity]:
        images_metadata = self._cytomine.list_images(collection_id)
        similar_images = self._mapsort_distances(
            images_metadata, img_ids, img_distances
        )

        return similar_images

    def _mapsort_distances(
        self,
        images_metadata: List[ImageMetaDataEntity],
        img_ids: List[int],
        img_distances: List[str],
    ) -> List[ImageMetaDataEntity]:
        img: ImageMetaDataEntity

        similar_images = []
        for i, id in enumerate(img_ids):
            for img in images_metadata:
                if img.id == id:
                    img.score = img_distances[i]
                    similar_images.append(img)
                    continue

        return similar_images
