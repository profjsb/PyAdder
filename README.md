# PyAdder

[![Python package](https://github.com/profjsb/PyAdder/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/profjsb/PyAdder/actions/workflows/test.yml)

[![DOI](https://zenodo.org/badge/74057441.svg)](https://zenodo.org/badge/latestdoi/74057441)

[![codecov](https://codecov.io/gh/profjsb/PyAdder/branch/master/graph/badge.svg)](https://codecov.io/gh/profjsb/PyAdder)

[![PyPi version](https://badgen.net/pypi/v/PyAdder/)](https://pypi.com/project/PyAdder)

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

[![GitHub latest commit](https://badgen.net/github/last-commit/profjsb/PyAdder)](https://GitHub.com/profjsb/PyAdder/commit/)


Show off the structure of a Python codebase.

```
> tree PyAdder/ -a -T PyAdder -C --noreport -I ".git|*.pyc|.cache|.pytest_cache|*~|.DS_Store"
PyAdder/
├── .coveragerc
├── .github
│   └── workflows
│       └── test.yml
├── .gitignore
├── .travis
│   └── run.sh
├── .travis.yml
├── CHANGES.txt
├── Dockerfile
├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── adder
│   ├── __init__.py
│   ├── __pycache__
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       └── test_one_number.py
├── requirements.txt
├── setup.cfg
└── setup.py
```
