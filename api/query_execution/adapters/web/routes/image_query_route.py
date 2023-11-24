from config.environment import get_environment_variables
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi_pagination import Page, paginate
from query_execution.adapters.image_repository_imp import ImageRepositoryImp
from query_execution.adapters.image_service_imp import ImageServiceImp
from query_execution.adapters.miulvas.miulvas import MilvusDBImp
from query_execution.adapters.sqllite.sqllite_db import SQLLiteDBImp
from query_execution.adapters.web.routes.requests import SearchRequest
from query_execution.adapters.web.routes.responses import ImageResponse
from query_execution.domain.image.image_entity import (
    ImageEntity,
    ImageFileEntity,
)
from query_execution.usecase.image_search_usercase import ImageSearchUseCase
from query_execution.usecase.upload_query_image_usercase import (
    ImageUploadUseCase,
)

env = get_environment_variables()
sqllite_db = SQLLiteDBImp()
milvus_db = MilvusDBImp()

image_query_router = APIRouter(prefix='/v1/image-query')


@image_query_router.post('/upload-query-image/')
def upload_query_images(file: UploadFile = File(...)):
    try:
        image_upload_usecase = ImageUploadUseCase(
            ImageRepositoryImp(env, sqllite_db, milvus_db)
        )
        result = image_upload_usecase.execute(
            ImageFileEntity(binary=file.file.read(), name=file.filename)
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@image_query_router.post('/search/', response_model=Page[ImageResponse])
def search_images(
    body: SearchRequest,
):
    try:
        image_search_usecase = ImageSearchUseCase(
            ImageRepositoryImp(env, sqllite_db, milvus_db),
            ImageServiceImp(env, body.public_key, body.private_key),
        )
        images = image_search_usecase.execute(
            ImageEntity(body.image_id, body.collection_id)
        )
        return paginate(images)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
