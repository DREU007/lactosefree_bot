install:
	poetry install

lint:
	poetry run flake8 lactosefree_bot

run:
	poetry run python lactosefree_bot/bot.py
