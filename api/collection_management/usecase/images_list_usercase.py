from collection_management.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)


class ImageListUseCase:
    def __init__(self, image_repository: ImageRepositoryInterface):
        self._image_repository = image_repository

    def execute(self, collection_id: int) -> int:
        images = self._image_repository.list_images(collection_id)
        return images
