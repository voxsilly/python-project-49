install:
    poetry install

reinstall:
    python3 -m pip install --force-reinstall --user dist/*.whl

brain-games:
    poetry run brain-games

brain-even:
    poetry run brain-even

brain-calc:
    poetry run brain-calc

build:
    poetry build

publish:
    poetry publish --dry-run

package-install:
    python3 -m pip install --user dist/*.whl

lint:
    poetry run flake8 brain_calc
