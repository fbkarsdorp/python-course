#!/bin/bash
which ipython3
if [[ $? == 0 ]]; then
	ipython3 notebook
else
	ipython notebook
fi
