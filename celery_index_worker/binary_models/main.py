from cytomine import Cytomine
from cytomine.models import ImageInstanceCollection

from celery_index_worker.binary_models.binary_extractor_imp import extract

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
    dados = images.data()
    for img in range(len(dados)):
        file_location = f"{file_storage}/{dados[0].user}/{dados[0].filename}"
        vector, _ = extract(file_location)
        matrix.append(vector)

    print(len(matrix))
    print('success')
    return True