from typing import Set
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/body-nested-models',
    tags=['Body Nested Models']
)


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: Set[str] = set()
    image: Image | None = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    - 중첩, 중복 데이터 처리 예제.
    - `tags`: Set 자료형을 사용하여 배열 매개변수를 받았을 때, 중복을 제거.
    - `image`: `Image` 모델에 정의된 구조에 맞춰 자동으로 파싱하고 유효성을 검사.
    """

    results = {"item_id": item_id, "item": item}
    return results
