#!/bin/bash

cd "$(dirname "$0")"
which ipython3
if [[ $? == 0 ]]; then
	ipython3 notebook --matploblib=inline
else
	ipython notebook --matplotlib=inline
fi
