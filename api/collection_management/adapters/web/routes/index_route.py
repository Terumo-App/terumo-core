from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Param
from celery import Celery


from config.environment import get_environment_variables

env = get_environment_variables()


simple_app = Celery(__name__,
                    broker='amqp://admin:mypass@localhost:5673',
                    backend='rpc://')


index_router = APIRouter(prefix='/v1/index')


### TEST

@index_router.get('/simple_start_task')
def call_method():
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    return r.id

@index_router.get('/simple_task_status/{task_id}')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id)
    print(status)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@index_router.get('/simple_task_result/{task_id}')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


### TERUMO

@index_router.get('/collection-index/{collection_id}')
def call_method(collection_id):
    r = simple_app.send_task('tasks.indexing', kwargs={'collection_id': collection_id})
    return r.id