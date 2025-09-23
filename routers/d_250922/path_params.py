from fastapi import APIRouter

router = APIRouter(
    prefix='/path-params',
    tags=['Path Params']
)


@router.get('/stock/{stock_number}')
def read_stock(stock_number: int):
    """
    경로 매개변수

    주식 번호를 입력하면 기업명을 반환합니다.
    """

    stocks = {1: '삼성전자', 2: 'SK하이닉스', 3: '네이버'}
    return {'stock_number': stock_number, 'name': stocks[stock_number]}
