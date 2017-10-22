#!/bin/bash

cd "$(dirname "$0")"

source activate py34
if [[ $? == 0 ]]; then
	jupyter-notebook
else
	which ipython3
	if [[ $? == 0 ]]; then
		jupyter-notebook
	else
		jupyter-notebook
	fi
fi
