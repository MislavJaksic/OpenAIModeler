## OpenAI Modeler

'''
* Give an instruction
* Give few examples
    * Give lots of examples by fine-tuning the model
* Adjust temperature

https://platform.openai.com/examples
https://platform.openai.com/docs/guides/chat/introduction
https://github.com/openai/openai-cookbook/
'''

## Development

```
# Note: Install Python 3
# You may also need to install or update pip, virtualenv (dependency encapsulator) and black (linter)

# Note: install Poetry for your OS
```

```
# Note: `.toml` project name and package have to match (openai-modeler; openai_modeler)
$: poetry install  # install all dependencies
```

```
Rename secrets-template.py to secrets.py and paste your OpenAI API key into it.
```

### dist

```
$: pip install dist/openai_modeler-0.0.1-py3-none.any.whl

$: openai-modeler
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### openai_modeler

```
$: poetry run openai-modeler --help
$: poetry run python ./openai_modeler/runner.py --help

$: poetry run python ./openai_modeler/runner.py -x 2 -y -1 -tuple A B C -list D -list E -list F -move rock
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=openai_modeler --cov-report=html tests
# Note: see coverage report in htmlcov/index.html
# Note: exclude directories from coverage report through .coveragerc
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add [-D] Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.


### Linters

```
$: poetry run black .
```

### MyPy

```
$: poetry run mypy ./openai_modeler ./tests
```

### cProfile

```
$: poetry run python ./openai_modeler/profiler.py
```

### Build and publish

```
$: poetry build

# Note: get the token from your PiPy account
$: poetry config pypi-token.pypi PyPI-Api-Access-Token
```

```
$: poetry publish --build
```

```
https://pypi.org/project/openai-modeler/
```
