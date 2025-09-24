from fastapi import FastAPI
from routers.d_250922 import path_params, path_params_numeric_validations, query_params, query_params_str_validations, req_body
from routers.d_250923 import body_nested_models

app = FastAPI()

# 250922
app.include_router(path_params.router)
app.include_router(query_params.router)
app.include_router(req_body.router)
app.include_router(query_params_str_validations.router)
app.include_router(path_params_numeric_validations.router)

# 250923
app.include_router(body_nested_models.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
