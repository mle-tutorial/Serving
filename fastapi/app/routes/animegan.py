from app.schemas.animegan import PreTrainedModel
from app.services.animegan import inference_animegan
from fastapi.responses import Response

from fastapi import APIRouter, Form, UploadFile

router = APIRouter()


@router.post("/animegan", name="AnimeGANv2")
async def animegan(img: UploadFile, pretrained: PreTrainedModel = Form(...)):
    img = await img.read()
    anime_img = inference_animegan(img, pretrained.value)

    img_response = Response(content=anime_img, media_type="image/png")

    return img_response
