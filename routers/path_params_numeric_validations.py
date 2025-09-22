from fastapi import APIRouter, Path

router = APIRouter(
    prefix='/path-params-numeric-validations',
    tags=['Path Params Numeric Validations']
)


@router.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="조회할 Item의 ID", ge=1), q: str):
    """
    - `*` 를 사용하여 모든 매개변수를 키워드 전용으로 만들어 FastAPI가 경로와 쿼리 매개변수를 명확하게 구분
    - `ge=1`: `item_id` 가 1보다 크거나 같아야 한다.
        - `gt`: 크거나(**g**reater **t**han)
        - `ge`: 크거나 같은(**g**reater than or **e**qual)
        - `lt`: 작거나(**l**ess **t**han)
        - `le`: 작거나 같은(**l**ess than or **e**qual)
    """

    results = {"item_id": item_id}

    if q:
        results.update({"q": q})

    return results
