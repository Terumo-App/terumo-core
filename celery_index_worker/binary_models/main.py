from binary_models.binary_extractor_imp import extract
from binary_models.miulvas import connect_miulvas_db, create_collection
from celery.utils.log import get_task_logger
from cytomine import Cytomine
from cytomine.models import ImageInstanceCollection
import os

logger = get_task_logger(__name__)

# terumo_admin
# _public_key = 'e4c84130-d5d4-41bd-8db0-0384339f31c2'
# _private_key = '98a22af6-17de-491a-88d3-3e798ada03fb'
_public_key = os.getenv('PUBLIC_KEY')
_private_key = os.getenv('PRIVATE_KEY')

HOST = os.getenv('CYTOMINE_HOST')

connect_miulvas_db()


def start_collection_indexing(collection_id: int):

    with Cytomine(
        host=HOST, public_key=_public_key, private_key=_private_key
    ):

        images = ImageInstanceCollection().fetch_with_filter(
            'project', collection_id
        )

    file_storage = './file_storage'
    # file_storage = '//wsl.localhost/Ubuntu/home/maodsunix/cytomine/data/images'
    matrix = []
    image_ids = []

    if not images:
        raise ValueError('Collection has no images')

    data = images.data()
    logger.info(f'project image number: {len(data)}')
    logger.info(f'Starting attribute extraction...')
    for i, img in enumerate(data):
        file_location = f'{file_storage}/{img.user}/{img.filename}'

        logger.info(f'{file_location} - {str(i).zfill(5)}')
        vector, _ = extract(file_location)
        matrix.append(vector)
        image_ids.append(img.id)

    logger.info(f'Finishing attribute extraction...')
    matriz_float = [[float(element) for element in row] for row in matrix]
    logger.info(matriz_float)
    data = [image_ids, matriz_float]

    logger.info(f'Creating collection...')
    collection = create_collection(collection_id)

    logger.info(f'Inserting data into the collection: {collection_id} ...')
    mr = collection.insert(data)
    collection.flush()

    return True
