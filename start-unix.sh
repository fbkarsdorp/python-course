#!/bin/bash
which ipython3
if [[ $? == 0 ]]; then
	ipython3 notebook --pylab=inline
else
	ipython notebook --pylab=inline
fi
