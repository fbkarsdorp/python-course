#!/bin/bash

cd "$(dirname "$0")"

source activate py34
if [[ $? == 0 ]]; then
	ipython notebook --matplotlib=inline
else
	which ipython3
	if [[ $? == 0 ]]; then
		ipython3 notebook --matplotlib=inline
	else
		ipython notebook --matplotlib=inline
	fi
fi
