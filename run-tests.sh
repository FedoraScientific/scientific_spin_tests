#!/bin/bash

for subdir in c cpp matplotlib networkx sympy R ipython; do
    pushd $subdir
    make
    popd
done
