from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/req-body',
    tags=['Request Body Example']
)


class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None


@router.post('/items')
async def create_item(item: Item):
    """
    Pydantic 의 BaseModel 을 활용한 Request Body 예제
    """

    return item


@router.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    """
    Request Body + Path Params 예제
    """

    return {'item_id': item_id, **item.model_dump()}
