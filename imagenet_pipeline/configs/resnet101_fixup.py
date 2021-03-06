from .base import ConfigImageNetBase

from torch.nn import DataParallel


from pipeline.models.image_models.resnet_fixup import resnet101

MODEL_SAVE_PATH = "models/imagenet_resnet_101_fixup"


class Config(ConfigImageNetBase):
    def __init__(self, model_save_path=MODEL_SAVE_PATH):
        super().__init__(model=DataParallel(resnet101()), model_save_path=model_save_path, use_mixup=True, batch_size=128 * 8, learning_rate=0.1 * 8)
