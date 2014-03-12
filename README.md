# Python Programming for the Humanities

This document describes the installation procedure for all the software needed for the Python class. If your stuck anywhere in the installation procedure, please do not hesitate to contact Folgert Karsdorp (folgert.karsdorp@meertens.knaw.nl).

## Sublime text

We advice you to install a good text editor, Sublime text 2. However, you are absolutely free to use your own favourite editor. For Sublime Text 2 go to http://www.sublimetext.com/ download the version for your operating system and install.

In the course we will be using software that works best with Google Chrome.  Firefox 6 (or above) and Safari will also work. Internet Explorer is not supported. 

We will be using Python 3 for our course, so lower versions of Python are not sufficient. 

## Installation
### All platforms

We strongly advice you to install the Anaconda Python Distribution. This distribution contains all the necessary modules and packages needed for this course. It is available for all platforms and provides a simple installation procedure/ You can download it from: http://continuum.io/downloads. More detailed installation instructions can be found here: http://docs.continuum.io/anaconda/install.html 

Anaconda's default installation is Python 2.7. However, we will use Python 3 in this course. To install all necessary packages for Python 3, type 

    conda create -n py3k python=3 anaconda

followed by

    source activate py3k

at the command line. (If this doesn't work, have a look here: http://continuum.io/blog/anaconda-python-3). After that launch ipython with:

    ipython notebook --pylab=inline

### Windows
Download and install the Anaconda Python Distribution (see above).

Follow the instructions of Anaconda to launch ipython notebook.

If everything goes right, this should open your browser (preferably Google Chrome or Firefox) on a page http://127.0.0.1:8888/ (or something similar) which says `IP[y]: Notebook'. If for some reason, the notebook is opened by IE, copy the URL and paste that in either Google Chrome or Firefox.

### OS X 
Only take these steps if you know what you are doing. Otherwise, simply download and install the Anaconda Python Distribution (see above).

First you will need to install Xcode from the App Store. After you have successfully installed Xcode, open Xcode and go to Xcode -> preferences -> Downloads. Now click on the install button next to commandline tools. 

Open spotlight and type in `terminal' to open the terminal application. (You can also go to your applications folder and then to utilities where you'll find the terminal.app)

Cd to the folder where you downloaded or saved the file mac-installer.sh (probably in ~/Downloads) by using

    cd /folder/of/mac-installer.sh 

Run the installer with the following command. The installer will download some packages and will request for your password to install them.

    . mac-installer.sh

To check your installation, relaunch the terminal.app. Then type in 

    ipython3 notebook --pylab=inline

If everything went well this should open your browser (best with Google Chrome or Firefox) on the page http://127.0.0.1:8888/ which says IP[y]: Notebook.

### Linux (Ubuntu/Debian)

Only take these steps if you know what you are doing. Otherwise, simply download and install the Anaconda Python Distribution

First open a terminal, then type

    sudo apt-get install python3 ipython3 ipython3-notebook numpy scipy matplotlib 

If you run another Linux distribution, similar packages should be available.

## Static Notebooks

This is a fall-back method.

[Chapter 1 - Getting started](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%201%20-%20Getting%20started.ipynb)

[Chapter 2 - First steps into text processing](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%202%20-%20First%20steps.ipynb)

[Chapter 3 - Text Analysis](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%203%20-%20Text%20analysis.ipynb)

[Chapter 4 - Programming principles](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%204%20-%20Programming%20principles.ipynb)

[Chapter 5 - Building NLP applications](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%25205%2520-%2520Building%2520NLP%2520Applications.ipynb)


