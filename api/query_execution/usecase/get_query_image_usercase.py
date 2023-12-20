from typing import Any, List
import logging

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

logger = logging.getLogger(__name__)

class GetQueryImageUseCase:
    _image_repository: ImageRepositoryInterface
    _sqldb_repository: SQLDBInterface
   

    def __init__(
        self,
        image_repository: ImageRepositoryInterface,

    ):
        self._image_repository = image_repository


    def execute(
        self, image_id: str
    ) -> str:
        image_path = self._image_repository.get_image_path(
            image_id
        )
        return image_path
