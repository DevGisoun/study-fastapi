from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello/{hello_id}")
def read_hello(hello_id: int, q: Union[str, None] = None):
    return {"hello_id": hello_id, "q": q}


@app.get('/stock/{stock_number}')
def read_stock(stock_number: int):
    """
    주식 번호를 입력하면 기업명을 반환합니다.
    """
    stocks = {1: '삼성전자', 2: 'SK하이닉스', 3: '네이버'}
    return {'stock_number': stock_number, 'name': stocks[stock_number]}
