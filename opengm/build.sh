#!/bin/bash

## add these channels which include boost and hdf5. These are required.
#conda config --add channels https://conda.binstar.org/mutirri

cmake -DWITH_BOOST=ON -DBUILD_COMMANDLINE=ON -DBUILD_PYTHON_WRAPPER=ON -DWITH_HDF5=ON -DCMAKE_INSTALL_PREFIX=$PREFIX .
make
make install