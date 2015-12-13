#!/bin/bash

for subdir in c cpp matplotlib networkx sympy R; do
    pushd $subdir
    make
    popd
done
