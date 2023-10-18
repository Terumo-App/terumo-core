from typing import List

from collection_management.domain.collection.collection_entity import (
    CollectionEntity,
)
from collection_management.domain.collection.collection_repository_interface import (
    CollectionRepository,
)


class UploadImagesUseCase:
    def __init__(
        self, file_storage_service, cytomine_service, message_broker_service
    ):
        self.file_storage_service = file_storage_service
        self.cytomine_service = cytomine_service
        self.message_broker_service = message_broker_service

    def execute(
        self, image_binaries: List[bytes], project_name: str
    ) -> List[str]:
        # 1. Salvar imagens no file storage e obter os caminhos dos arquivos
        image_paths = self.file_storage_service.save_images(image_binaries)

        # 2. Salvar imagens no Cytomine
        self.cytomine_service.upload_images(image_paths, project_name)

        # 3. Enviar um evento para RabbitMQ para indexar as imagens
        project_id = self.cytomine_service.get_project_id(project_name)
        self.rabbitmq_service.send_indexing_event(project_id)

        return image_paths
