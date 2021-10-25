main:
	pipenv run uvicorn api.main:app --reload

start:
	pipenv run uvicorn api.main:app
