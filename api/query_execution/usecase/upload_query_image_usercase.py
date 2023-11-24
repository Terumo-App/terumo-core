from typing import Any, List

from query_execution.domain.image.image_entity import (
    ImageEntity,
    ImageFileEntity,
)
from query_execution.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)


class ImageUploadUseCase:
    def __init__(
        self,
        image_repository: ImageRepositoryInterface,
    ):
        self._image_repository = image_repository

    def execute(self, file: ImageFileEntity) -> ImageEntity:
        image_location = self._image_repository.persist_image_on_file_storage(
            file
        )
        result = self._image_repository.persist_image_metadata(
            file.name, image_location
        )
        return result
