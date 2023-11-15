from cytomine import Cytomine
from cytomine.models import ImageInstanceCollection

from binary_models.binary_extractor_imp import extract
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

#terumo_admin
_public_key = 'e4c84130-d5d4-41bd-8db0-0384339f31c2'
_private_key = '98a22af6-17de-491a-88d3-3e798ada03fb'

_host = 'http://maods.homelab.core'

def start_collection_indexing(collection_id:int):

    with Cytomine(host=_host, public_key=_public_key, private_key=_private_key):

        images = ImageInstanceCollection().fetch_with_filter("project", collection_id)

    file_storage = './file_storage'
    # file_storage = '//wsl.localhost/Ubuntu/home/maodsunix/cytomine/data/images'
    matrix = []
    image_ids = []
    dados = images.data()
    logger.info(f'project image number: {len(dados)}')
    logger.info(f'Starting attribute extraction...')
    for img in dados:
        logger.info(img.filename)
        file_location = f"{file_storage}/{img.user}/{img.filename}"
        vector, _ = extract(file_location)
        matrix.append(vector)
        image_ids.append(img.id)
        logger.info(img.filename)

    logger.info(f'Finishing attribute extraction...')
    matriz_float = [[float(element) for element in row] for row in matrix]
    logger.info(matriz_float)
    data = [
        image_ids,
        matriz_float
    ]


    return True