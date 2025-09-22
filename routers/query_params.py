from fastapi import APIRouter
from typing import Union

router = APIRouter(
    prefix='/query_params',
    tags=['Query Params']
)


@router.get("/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    기본값이 있는 쿼리 매개변수
    """

    fake_items_db = [{"item_name": "Foo"}, {
        "item_name": "Bar"}, {"item_name": "Baz"}]

    return fake_items_db[skip: skip + limit]


@router.get("/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """
    필수 쿼리 매개변수
    """

    item = {"item_id": item_id, "needy": needy}
    return item


@router.get("/hello/{hello_id}")
def read_hello(hello_id: int, q: Union[str, None] = None):
    """
    선택적 쿼리 매개변수
    """

    if q:
        return {"hello_id": hello_id, "q": q}

    return {"hello_id": hello_id}
