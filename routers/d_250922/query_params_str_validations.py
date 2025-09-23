from typing import List
from fastapi import APIRouter, Query

router = APIRouter(
    prefix='/query-params-str-validations',
    tags=['Query Params str Validations']
)


@router.get("/items/")
async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50)):
    """
    `q` 가 선택적이지만 값이 주어질 때마다 아래와 같은 조건 강제

    - `q: str | None`: Union 또는 Optional 타입 보다 더 간결하고 현대적인 방식으로 표현한 선택적 매개변수 사용 명시 방법. `| None` 제거 시, 필수 매개변수로 전환.
    - `default`: 기본값 지정. `None` 허용. `default` 에 값이 지정되었을 경우, 선택적 매개변수로 취급.
    - `min_length`: 값이 최소 3글자
    - `max_length`: 값이 최대 50글자
    - `pattern`: **'fixedquery'** 라는 문자열과 정확히 일치하는 값만 허용 (**정규 표현식**)
    """

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@router.get('/list/')
async def read_list(q: List[str] = Query(default=['One', 'Two'])):
    """
    쿼리 매개변수로 리스트 전달 및 default 적용 예시.
    """

    query_items = {'q': q}
    return query_items


@router.get('/alias/')
async def alias_params(q: str | None = Query(defualt=None, alias='item-query')):
    """
    브라우저에서 쿼리 매개변수를 `q` 대신 `item-query` 라는 이름으로 받아 사용하는 예제.
    """

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
