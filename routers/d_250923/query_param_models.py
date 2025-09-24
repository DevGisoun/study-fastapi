from typing import Annotated, Literal
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

router = APIRouter(
    prefix='/query-param-models',
    tags=['Query Param Models']
)


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}  # 모델에 정의되지 않은 추가적인 쿼리 매개변수 불허용.

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@router.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    """
    쿼리 매개변수를 Pydantic 모델로 묶어 관리 및 검증하는 예제.

    - `model_config`: 모델에 정의되지 않은 추가적인 쿼리 매개변수 불허용.
    - `Query()`: `filter_query` 가 쿼리 매개변수임을 명시.
    - `Annotated[FilterParams, Query()]`: `filter_query` 의 데이터 구조. 데이터(모델) 타입과 처리 방식(Query, Path, Body 등) 작성.
    """

    return filter_query
