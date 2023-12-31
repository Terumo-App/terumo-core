from authentication.adapters.web.routes.signup_route import signup_router
from collection_management.adapters.web.routes.collection_route import (
    collection_router,
)
from collection_management.adapters.web.routes.image_route import image_router
from collection_management.adapters.web.routes.index_route import index_router
from config.environment import get_environment_variables
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from query_execution.adapters.web.routes.image_query_route import (
    image_query_router,
)

env = get_environment_variables()


app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(signup_router)
app.include_router(collection_router)
app.include_router(image_router)
app.include_router(index_router)
app.include_router(image_query_router)

add_pagination(app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
