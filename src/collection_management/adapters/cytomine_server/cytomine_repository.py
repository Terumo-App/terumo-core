from typing import List, Union

from collection_management.adapters.cytomine_server.cytomine import (
    CytomineWrapper,
)
from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)
from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepository,
)


class CytomineRepository(CollectionRepository):
    cytomine: CytomineWrapper

    def __init__(self, config, public_key, private_key) -> None:
        self._cytomine = CytomineWrapper(config, public_key, private_key)

    def create_collection(self, collection_name: str) -> CollectionEntity:
        proj = self._cytomine.create_collection(collection_name)
        if not proj:
            raise ValueError('Error creating collection.')

        project = CollectionEntity(
            proj.id, proj.created, proj.name, proj.numberOfImages
        )
        return project

    def list_collections(self) -> List[CollectionEntity]:
        projects = self._cytomine.list_collections()
        projects = [
            CollectionEntity(p.id, p.created, p.name, p.numberOfImages)
            for p in projects
        ]
        return projects

    def find_collection_by_name(
        self, collection_name: str
    ) -> CollectionEntity | bool:
        project = self._cytomine.find_collection_by_name(collection_name)
        if project:
            return CollectionEntity(
                project.id,
                project.created,
                project.name,
                project.numberOfImages,
            )
        return False
