import time
from celery import Celery
from celery.utils.log import get_task_logger
import os 
from binary_models.main import start_collection_indexing


logger = get_task_logger(__name__)


app = Celery(__name__)
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(20)
    logger.info('Work Finished ')
    return x + y

@app.task()
def indexing(collection_id):
    logger.info('Got Request - Starting work ')
    result = start_collection_indexing(collection_id)
    logger.info('Work Finished ')
    return result