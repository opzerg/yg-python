from fastapi import APIRouter

from api.hello.hello import hello_router

router = APIRouter()
router.include_router(hello_router, prefix="/hello", tags=["Hello"])


__all__ = ["router"]
