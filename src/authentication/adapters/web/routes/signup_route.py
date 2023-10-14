from fastapi import APIRouter, Depends, HTTPException, status

from authentication.adapters.cytomine_server.cytomine_repository import (
    CytomineRepository,
)
from authentication.adapters.web.routes.requests import SignupRequest
from authentication.usecase.signup_usecase import SignupUseCase
from config.environment import get_environment_variables

env = get_environment_variables()

signup_router = APIRouter(prefix='/v1/auth')

signup_usecase = SignupUseCase(CytomineRepository(env))


@signup_router.post('/signup')
def signup(signup_data: SignupRequest):
    try:
        print(signup_data)
        user_id = signup_usecase.execute(signup_data)
        return {'message': 'User created successfully', 'data': user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
