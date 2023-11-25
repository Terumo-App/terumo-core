from typing import List

from cytomine import Cytomine
from cytomine.models import (
    ImageInstance,
    ImageInstanceCollection,
    Project,
    ProjectCollection,
)
from query_execution.domain.image.image_entity import ImageMetaDataEntity, Name, Picture


class CytomineWrapper:
    def __init__(self, config, public_key, private_key) -> None:
        self._host = config.HOST
        self._public_key = public_key
        self._private_key = private_key

    def list_collections(self) -> List[Project]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            projects = ProjectCollection().fetch()
            return projects.data()
        
    def list_images(self, collection_id: int) -> List[ImageMetaDataEntity]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            images = ImageInstanceCollection().fetch_with_filter(
                'project', collection_id
            )
            img: ImageInstance
            collection = []
            for img in images.data():
                collection.append(
                    ImageMetaDataEntity(
                                        id=img.id,
                                        image_url=img.preview,
                                        picture=Picture(
                                            large=img.preview, medium=img.preview, thumbnail=img.thumb
                                        ),
                                        name=Name(last=img.originalFilename),
                                    )
                )
            return collection
