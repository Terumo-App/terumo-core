from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Param
from fastapi_pagination import Page, paginate, Params

from collection_management.adapters.cytomine_server.image_repository_imp import (
    ImageRepositoryImp,
)
from collection_management.adapters.web.routes.responses import (
    ImageResponse,
)
from collection_management.adapters.web.routes.requests import (
    BasicRequest, ImageRequest
)
from collection_management.usecase.images_list_usercase import (
    ImageListUseCase,
)
# from collection_management.usecase.image_upload_usecase import (

# )


from config.environment import get_environment_variables

env = get_environment_variables()

image_router = APIRouter(prefix='/v1/image')


@image_router.post('/', response_model=Page[ImageResponse])
def get_images(
    body: ImageRequest,

):
    try:
        list_image_usecase = ImageListUseCase(
            ImageRepositoryImp(env, body.public_key, body.private_key)
        )
        images = list_image_usecase.execute(body.collection_id)

        return paginate(images)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
