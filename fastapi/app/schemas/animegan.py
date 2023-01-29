from enum import Enum


class PreTrainedModel(str, Enum):
    celeba_distill = "celeba_distill"
    face_paint_512_v1 = "face_paint_512_v1"
    face_paint_512_v2 = "face_paint_512_v2"
