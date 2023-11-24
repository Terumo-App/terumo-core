import os
from datetime import datetime
from typing import Any, List, Tuple, Union

from config.environment import EnvironmentSettings
from query_execution.adapters.sqllite.sqllite_db import SQLLiteDBImp
from query_execution.domain.image.image_entity import (
    ImageEntity,
    ImageFileEntity,
)
from query_execution.domain.image.image_repository_interface import (
    ImageRepositoryInterface,
)
from query_execution.domain.image.sql_db_interface import SQLDBInterface
from query_execution.domain.image.vector_db_interface import VectorDBInterface


class ImageRepositoryImp(ImageRepositoryInterface):

    _config: EnvironmentSettings
    _sql_db: SQLDBInterface
    _vector_db: VectorDBInterface

    def __init__(
        self,
        config: EnvironmentSettings,
        sql_db: SQLDBInterface,
        vector_db: VectorDBInterface,
    ) -> None:
        self._config = config
        self._sql_db = sql_db
        self._vector_db = vector_db
        self.root_referemce = os.getcwd()

    def persist_image_on_file_storage(self, image: ImageFileEntity) -> str:
        folder_name = './image_storage'
        # TODO: create routine to delete search images periodcly
        # TODO: Get folder name from env variables

        folder_path = os.path.join(self.root_referemce, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        timestamp = str(datetime.now().timestamp())
        file_location = os.path.join(folder_path, f'{timestamp}_{image.name}')

        with open(file_location, 'wb') as f:
            f.write(image.binary)

        return file_location
    
    def load_image_from_file_storage(self, image_path: str) -> bytes:
        with open(image_path, 'rb') as f:
            binary_image = f.read()
        return binary_image
    
    def persist_image_metadata(
        self, file_name: str, image_location: str
    ) -> ImageEntity:
        image_id = self._sql_db.save_image(file_name, image_location)
        return image_id

    def search_similar_images(
        self, attributes: List[int], collection_id: int
    ) -> Tuple[List[int], List[str]]:
        return self._vector_db.search(collection_id, attributes)

    def get_image_path(self, image_id: str) -> str:
        result = self._sql_db.get_image_path(image_id)
        return result['filepath']
