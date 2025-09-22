install:
	uv add -r requirements.txt

dev:
	uv run uvicorn main:app --reload

serve:
	uv run uvicorn main:app --host 0.0.0.0 --port 80

# 의존성 목록 생성 (npm install <pkg> --save 와 유사 후 목록 업데이트)
sync:
	uv pip freeze > requirements.txt