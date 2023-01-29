from dataclasses import asdict

import mlflow
import torch
from app.common.config import Config
from torch import nn

conf_dict = asdict(Config())
mlflow.set_tracking_uri(conf_dict["MLFLOW_URI"])


def load_rf_model(name: str):
    model = mlflow.sklearn.load_model(f"models:/{name}/latest")
    return model


def load_gan_model(pretrained: str) -> tuple[nn.Module]:
    model = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "generator", pretrained=pretrained
    )
    face2paint = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "face2paint", size=512
    )

    return model, face2paint
