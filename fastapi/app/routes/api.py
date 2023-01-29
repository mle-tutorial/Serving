from app.routes import animegan, stock

from fastapi import APIRouter

router = APIRouter()
router.include_router(stock.router, tags=["stock"], prefix="/stock")
router.include_router(animegan.router, tags=["image"], prefix="/gan")
