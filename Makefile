setup:	install build publish package-reinstall


start:	diff

check:	pytest lint

install:
	poetry install

diff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov


.PHONY: gendiff
