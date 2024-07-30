setup:	install build publish package-reinstall


start:	diff

check:	pytest lint

install:
	poetry install

diff-stylish-json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

diff-stylish-yml:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

diff-plain-yml:
	poetry run gendiff -f plain tests/fixtures/file1.yml tests/fixtures/file2.yml

diff-plain-json:
	gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json

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
	poetry run flake8 tests

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov
	poetry run pytest --cov=gendiff --cov-report xml


.PHONY: gendiff
