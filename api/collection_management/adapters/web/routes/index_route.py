import os

from celery import Celery
from config.environment import get_environment_variables
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Param

env = get_environment_variables()

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
# ON_CONTAINER = True
CELERY_BROKER_URL = (
    CELERY_BROKER_URL
    if CELERY_BROKER_URL
    else 'amqp://admin:mypass@localhost:5673'
)


simple_app = Celery('tasks', broker=CELERY_BROKER_URL, backend='rpc://')


index_router = APIRouter(prefix='/v1/index')


### TEST


@index_router.get('/simple_start_task')
def call_method():
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    return r.id


@index_router.get('/task_status/{task_id}')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id)
    print(status)
    print('Invoking Method ')
    return 'Status of the Task ' + str(status.state)


@index_router.get('/task_result/{task_id}')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return 'Result of the Task ' + str(result)


### TERUMO


@index_router.get('/collection-index/{collection_id}')
def call_collection(collection_id):
    if not collection_id:
        raise ValueError('No collection id provided.')
    r = simple_app.send_task(
        'tasks.indexing', kwargs={'collection_id': collection_id}
    )
    return r.id
