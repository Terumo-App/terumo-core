from typing import List

from cytomine import Cytomine
from cytomine.models import Project, ProjectCollection, ImageInstanceCollection, ImageInstance 

from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)


class CytomineWrapper:
    def __init__(self, config, public_key, private_key) -> None:
        self._host = config.HOST
        self._public_key = public_key
        self._private_key = private_key

    def create_collection(self, collection_name: str):
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            project = Project(collection_name).save()
            return project

    def list_collections(self) -> List[Project]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            projects = ProjectCollection().fetch()
            return projects.data()

    def find_collection_by_name(self, collection_name: str) -> Project | bool:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            projects = ProjectCollection().fetch()
            proj_list = [
                proj
                for proj in projects.data()
                if proj.name == collection_name
            ]
            if proj_list:
                return proj_list.pop()
            return False

    def list_images(self, collection_id: int) -> List[ImageInstance]:
        with Cytomine(
            host=self._host,
            public_key=self._public_key,
            private_key=self._private_key,
        ):
            images = ImageInstanceCollection().fetch_with_filter("project", collection_id)
            return images.data()
