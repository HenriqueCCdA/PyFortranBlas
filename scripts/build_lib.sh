#!/usr/bin/env bash

set -e
# set -x # debug

source .venv/bin/activate

cd src/pyfortran/lib

rm -vf *.so

python -m numpy.f2py -c fblas.f90 fblas.pyf

deactivate
