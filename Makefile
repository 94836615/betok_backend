run_backend:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

run_test:
	pytest src/tests
