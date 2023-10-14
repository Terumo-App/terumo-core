from fastapi import APIRouter, Depends, HTTPException, status

from collection_management.adapters.cytomine_server.cytomine_repository import (
    CytomineRepository,
)
from collection_management.adapters.web.routes.requests import (
    CollectionCretionRequest,
    CollectionRequest,
)
from collection_management.usecase.create_collection_usecase import (
    CreateColllectionUseCase,
)
from collection_management.usecase.list_collections_usecase import (
    ListCollectionUseCase,
)
from config.environment import get_environment_variables

env = get_environment_variables()

collection_router = APIRouter(prefix='/v1/collection')


@collection_router.post('/')
def get_collections(body: CollectionRequest):
    try:
        list_collection_usecase = ListCollectionUseCase(
            CytomineRepository(env, body.primary_key, body.public_key)
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
            CytomineRepository(env, body.primary_key, body.public_key)
        )

        project = create_collection_usecase.execute(body.collection_name)
        return {'message': 'Success', 'data': project}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
