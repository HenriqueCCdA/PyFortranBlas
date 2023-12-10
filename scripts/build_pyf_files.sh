#!/usr/bin/env bash

set -e
# set -x # debug

source .venv/bin/activate

cd src/pyfortran/lib

python -m numpy.f2py fblas.f90 -h fblas.pyf -m fblas

deactivate
