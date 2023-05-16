#!/usr/bin/env bash
#set -E -o functrace
#set -ex

PIPENV_IGNORE_VIRTUALENVS=1 black pizza_django
PIPENV_IGNORE_VIRTUALENVS=1 black --check pizza_django
PIPENV_IGNORE_VIRTUALENVS=1 flake8 pizza_django
PIPENV_IGNORE_VIRTUALENVS=1 pylint --rcfile=.pylintrc --output-format=colorized pizza_django


tempfile=$(mktemp -t tmp.XXXXXX)
trap "rm -f ${tempfile}; exit 1" 1 2 3 15

#[ -z "$REVRANGE" ] && REVRANGE="master..HEAD^1"
#git diff --name-only $REVRANGE | grep '\.py$' > ${tempfile}
oe '.py$' | ohne 'env\/|docs\/|.eggs|doc\/' > ${tempfile}

py_files=()
while read line; do
    if [[ -f "${line}" ]]; then
        echo "fast-styling ${line}"
        # fiximports ${line};
        autopep8 --in-place --recursive  ${line}
        yapf --style .yapf --recursive -i ${line}
    fi
done < ${tempfile}
