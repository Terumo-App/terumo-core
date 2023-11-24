from typing import Any, List

from query_execution.domain.image.image_entity import (
    ImageEntity,
    ImageMetaDataEntity,
)
from query_execution.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)
from query_execution.domain.image.image_service_interface import (
    ImageServiceInterface,
)
from query_execution.domain.image.sql_db_interface import SQLDBInterface


class ImageSearchUseCase:
    _image_repository: ImageRepositoryInterface
    _sqldb_repository: SQLDBInterface
    _image_service: ImageServiceInterface

    def __init__(
        self,
        image_repository: ImageRepositoryInterface,
        image_service: ImageServiceInterface,
    ):
        self._image_repository = image_repository
        self._image_service = image_service

    def execute(
        self, search_request: ImageEntity
    ) -> List[ImageMetaDataEntity]:
        image_path = self._image_repository.get_image_path(
            search_request.image_id
        )
        print(image_path)
        image = self._image_service.load_image(image_path)
        attributes = self._image_service.extract_attributes(image)
        print(f'att {attributes}')
        img_ids, img_dist = self._image_repository.search_similar_images(
            attributes, search_request.collection_id
        )
        print(f'att {img_ids}')
        similar_imgs = self._image_service.consolidate_image_info(
            img_ids, img_dist, search_request.collection_id
        )
        return similar_imgs
