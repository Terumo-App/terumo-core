from fastapi import APIRouter, Depends, HTTPException, status

from collection_management.adapters.cytomine_server.collection_repository_imp import (
    CollectionRepositoryImp,
)
from collection_management.adapters.web.routes.requests import (
    CollectionCretionRequest,
    BasicRequest,
)
from collection_management.usecase.collection_create_usecase import (
    CreateColllectionUseCase,
)
from collection_management.usecase.collections_list_usecase import (
    ListCollectionUseCase,
)
from config.environment import get_environment_variables

env = get_environment_variables()

collection_router = APIRouter(prefix='/v1/collection')


@collection_router.post('/')
def get_collections(body: BasicRequest):
    try:
        list_collection_usecase = ListCollectionUseCase(
            CollectionRepositoryImp(env, body.public_key, body.private_key)
        )

        projects = list_collection_usecase.execute()
        print(projects)
        return {'message': 'Success', 'data': projects}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@collection_router.post('/create')
def create_collection(body: CollectionCretionRequest):
    try:
        create_collection_usecase = CreateColllectionUseCase(
            CollectionRepositoryImp(env, body.public_key, body.private_key)
        )

        project = create_collection_usecase.execute(body.collection_name)
        return {'message': 'Success', 'data': project}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
