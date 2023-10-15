from typing import List, Union

from collection_management.adapters.cytomine_server.cytomine import (
    CytomineWrapper,
)
from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)
from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from config.environment import EnvironmentSettings


class CollectionRepositoryImp(CollectionRepositoryInterface):
    _cytomine: CytomineWrapper
    _config: EnvironmentSettings

    def __init__(self, config: EnvironmentSettings, public_key: str, private_key: str) -> None:
        self._cytomine = CytomineWrapper(config, public_key, private_key)
        self._config = config

    def create_collection(self, collection_name: str) -> CollectionEntity:
        proj = self._cytomine.create_collection(collection_name)
        if not proj:
            raise ValueError('Error creating collection.')

        project = CollectionEntity(
            proj.id, proj.created, proj.name, proj.numberOfImages,
            self._get_project_type(proj.name),
            self._get_project_owner(proj.name)
        )
        return project

    def list_collections(self) -> List[CollectionEntity]:
        projects = self._cytomine.list_collections()
        projects = [
            CollectionEntity(p.id, p.created, p.name,
                             p.numberOfImages, self._get_project_type(p.name),
                             self._get_project_owner(p.name))
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
                self._get_project_type(project.name),
                self._get_project_owner(project.name)
            )
        return False

    def _get_project_type(self, project_name: str):
        if project_name == self._config.GLOBAL_PROJECT:
            return "Public"
        return "Private"

    def _get_project_owner(self, project_name: str):
        if project_name == self._config.GLOBAL_PROJECT:
            return "Terumo"
        return "User"
