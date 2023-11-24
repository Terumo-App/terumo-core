from typing import List, Union

from collection_management.adapters.cytomine_server.cytomine import (
    CytomineWrapper,
)
from collection_management.domain.image.image_entity import (
    ImageEntity,
    Name,
    Picture,
)
from collection_management.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)
from config.environment import EnvironmentSettings


class ImageRepositoryImp(ImageRepositoryInterface):
    _cytomine: CytomineWrapper
    _config: EnvironmentSettings

    def __init__(
        self, config: EnvironmentSettings, public_key: str, private_key: str
    ) -> None:
        self._cytomine = CytomineWrapper(config, public_key, private_key)
        self._config = config

    def list_images(self, collection_id: int) -> List[ImageEntity]:
        images = self._cytomine.list_images(collection_id)
        images = [
            ImageEntity(
                id=img.id,
                image_url=img.preview,
                picture=Picture(
                    large=img.preview, medium=img.preview, thumbnail=img.thumb
                ),
                name=Name(last=img.originalFilename),
            )
            for img in images
        ]
        return images
