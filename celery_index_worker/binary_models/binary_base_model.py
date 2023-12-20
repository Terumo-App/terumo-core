import os

import numpy as np
import torch
from binary_models.model import Net
from PIL import Image
from torchvision import transforms
import torch.nn.functional as F

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
DEVICE = 'cpu'

ON_CONTAINER = os.getenv('ON_CONTAINER')
# ON_CONTAINER = True
PATH_PREFIX = 'src/' if ON_CONTAINER else ''

# WEIGHTS = {
#     'HIPER': f'binary_models/artifacts/hiper_others_2023-05-12-18-06-48/4_fold_max_acc_checkpoint.pth.tar',
#     'MEMBR': f'binary_models/artifacts/membran_others_2023-05-12-20-31-18/0_fold_max_acc_checkpoint.pth.tar',
#     'NORM': f'binary_models/artifacts/normal_others_2023-05-12-15-45-47/4_fold_max_acc_checkpoint.pth.tar',
#     'SCLER': f'binary_models/artifacts/sclero_others_2023-05-12-13-27-54/4_fold_max_acc_checkpoint.pth.tar',
#     'PODOC': f'binary_models/artifacts/podoc_others_2023-05-17-08-46-23/2_fold_max_acc_checkpoint.pth.tar',
#     'CRESC': f'binary_models/artifacts/cresc_others_2023-05-17-13-22-44/2_fold_max_acc_checkpoint.pth.tar',
# }
WEIGHTS = {
    'HIPER': f'binary_models/artifacts_new/Hypercelularidade_2023-12-04-20-43-20/3_fold_max_acc_checkpoint.pth.tar',
    'MEMBR': f'binary_models/artifacts_new/Membranous_2023-12-05-01-14-12/2_fold_max_acc_checkpoint.pth.tar',
    'NORM': f'binary_models/artifacts_new/Normal_2023-12-05-08-57-50/1_fold_max_acc_checkpoint.pth.tar',
    'SCLER': f'binary_models/artifacts_new/Sclerosis_2023-12-05-05-11-12/4_fold_max_acc_checkpoint.pth.tar',
    'PODOC': f'binary_models/artifacts_new/Podocitopatia_2023-12-05-13-24-37/3_fold_max_acc_checkpoint.pth.tar',
    'CRESC': f'binary_models/artifacts_new/Crescent_2023-12-05-17-27-36/3_fold_max_acc_checkpoint.pth.tar',
}

def get_transform():
    return transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
        ]
    )


class ModelInfer:
    def __init__(self, model_type) -> None:
        self._model = None
        self._weights_path = WEIGHTS[model_type]
        self._transform = get_transform()
        self._load_model()
        self._load_model_weights()

    def _load_model(self) -> None:
        self._model = Net(net_version='b0', num_classes=2).to(DEVICE)
        print('model loaded')

    def process(self, image: Image.Image) -> np.ndarray:
        image_processed = self._transform(image)
        image_processed = image_processed.unsqueeze(0)
        return image_processed

    def predict(self, image: np.ndarray):
        self._model.eval()

        with torch.no_grad():

            output = self._model(image.to(DEVICE))
            scores = torch.sigmoid(output)
            predictions = (scores > 0.5).float()
            _, pred = torch.min(predictions, 1)

        return pred.item()
    
    def predict_target_prob(self, image: np.ndarray):
        self._model.eval()

        with torch.no_grad():
            output = self._model(image.to(DEVICE))
            probabilidades = F.softmax(output, dim=1)

        return probabilidades.squeeze()[0].item()

    def _load_model_weights(self):
        checkpoint = torch.load(
            self._weights_path, map_location=torch.device(DEVICE)
        )
        self._model.load_state_dict(checkpoint['state_dict'])
