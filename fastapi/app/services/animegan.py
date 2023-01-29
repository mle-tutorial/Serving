import io

from app.repository.model_registry import load_gan_model
from PIL import Image


def inference_animegan(img: bytes, pretrained: str) -> bytes:
    img_bytesio = io.BytesIO(img)
    img = Image.open(img_bytesio).convert("RGB")

    model, face2paint = load_gan_model(pretrained)
    f2p_img = face2paint(model, img)

    img_bytesio = io.BytesIO()
    f2p_img.save(img_bytesio, "PNG")
    img_bytes = img_bytesio.getvalue()

    return img_bytes
