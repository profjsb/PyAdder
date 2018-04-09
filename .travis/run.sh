#!/bin/bash

set -e
set -x

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    PYENV_ROOT="$HOME/.pyenv-adder"
    PATH="$PYENV_ROOT/bin:$PATH"
    hash -r
    eval "$(pyenv init -)"
fi

python setup.py build_ext -i
python -m compileall -f .
py.test tests/test.py --cov=codecov 
# python setup.py test

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
  python setup.py bdist_wheel
fi