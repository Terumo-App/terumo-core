import base64
import io
from typing import List, Tuple

from binary_models.binary_base_model import ModelInfer
from celery.utils.log import get_task_logger
from PIL import Image

logger = get_task_logger(__name__)

MODELS = [
    ModelInfer('HIPER'),
    ModelInfer('MEMBR'),
    ModelInfer('NORM'),
    ModelInfer('SCLER'),
    ModelInfer('PODOC'),
    ModelInfer('CRESC'),
]
MODELS_NAME = [
    'hypercellularity',
    'membranous',
    'normal',
    'sclerosis',
    'podocytopathy',
    'crescent',
]


def extract(image_path):
    vector = []
    att = []
    image = Image.open(image_path).convert('RGB')
    for model, name in zip(MODELS, MODELS_NAME):
        vector.append(model.predict_target_prob(model.process(image)))
        att.append(name)
    return vector, att
