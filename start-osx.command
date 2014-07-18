#!/bin/bash

source activate py34

cd "$(dirname "$0")"
which ipython3
if [[ $? == 0 ]]; then
	ipython3 notebook --matplotlib=inline
else
	ipython notebook --matplotlib=inline
fi
