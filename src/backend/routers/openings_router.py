
from fastapi import APIRouter, Query, Body, Request, Response

router = APIRouter()


@router.post("/hello")
async def hello():
    pass