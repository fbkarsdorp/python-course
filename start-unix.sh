#!/bin/bash

cd "$(dirname "$0")"

source activate py34
if [[ $? == 0 ]]; then
	jupyter-notebook || ipython-notebook --matplotlib=inline
else
	which ipython3
	if [[ $? == 0 ]]; then
		 jupyter-notebook || ipython-notebook --matplotlib=inline
	else
		jupyter-notebook || ipython-notebook --matplotlib=inline
	fi
fi
