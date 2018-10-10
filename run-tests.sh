#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
for subdir in c cpp matplotlib networkx sympy R ipython; do
    pushd "$DIR/$subdir"
    make
    popd
done
