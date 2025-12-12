all:
	uv pip install -e .
	uv run src/cairn_realmify/generate.py

test:
	uv pip install -e .
	uv run pytest tests

format:
	uvx ruff format .
