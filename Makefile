install:
	poetry install

lint:
	poetry run flake8 lactose_free_bot

run:
	poetry run python lactose_free_bot/first.py
