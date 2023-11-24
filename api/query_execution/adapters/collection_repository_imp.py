from typing import List, Union

from query_execution.adapters.cytomine_server.cytomine import (
    CytomineWrapper,
)
from query_execution.domain.collection.collection_entity import (
    CollectionEntity,
)
from query_execution.domain.collection.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from config.environment import EnvironmentSettings


class CollectionRepositoryImp(CollectionRepositoryInterface):
    _cytomine: CytomineWrapper
    _config: EnvironmentSettings

    def __init__(
        self, config: EnvironmentSettings, public_key: str, private_key: str
    ) -> None:
        self._cytomine = CytomineWrapper(config, public_key, private_key)
        self._config = config


    def list_collections(self) -> List[CollectionEntity]:
        projects = self._cytomine.list_collections()
        projects = [
            CollectionEntity(
                p.id,
                p.created,
                p.name,
                p.numberOfImages,
                self._get_project_type(p.name),
                self._get_project_owner(p.name),
            )
            for p in projects
        ]
        return projects


    def _get_project_type(self, project_name: str):
        if project_name == self._config.GLOBAL_PROJECT:
            return 'Public'
        return 'Private'

    def _get_project_owner(self, project_name: str):
        if project_name == self._config.GLOBAL_PROJECT:
            return 'Terumo'
        return 'User'
