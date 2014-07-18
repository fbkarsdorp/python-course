# Python Programming for the Humanities

The programming language [Python](http://www.python.org) is widely used within many scientific domains nowadays and the language is readily accessible to scholars from the Humanities. Python is an excellent choice for dealing with (linguistic as well as literary) textual data, which is so typical of the Humanities. In this book you will be thoroughly introduced to the language and be taught to program basic algorithmic procedures. The book expects no prior experience with programming, although we hope to provide some interesting insights and skills for more advanced programmers as well. The book consists of 10 chapters. Chapter 5 and Chapter 6 are still in draft status and not ready for use.

- [Chapter 1](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%201%20-%20Getting%20started.ipynb) starts with the very basics where we will try to whet your appetite. You will be asked to do many short quizes to test whether you really understand the material.
- [Chapter 2](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%202%20-%20First%20steps.ipynb) will introduce you to the task of text processing. You will learn how to read files from 
 your computer, how to clean them and compute a frequency distribution over words. 
- [Chapter 3](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%203%20-%20Text%20analysis.ipynb) deals with preprocessing text. You will learn some of the elementary tools to analyse your data. 
- [Chapter 4](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%204%20-%20Programming%20principles.ipynb) is a more theoretical chapter that explains to you some of the basic programming principles, common practices and where to find documentation. 
- In [Chapter 5](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%25205%2520-%2520Building%2520NLP%2520Applications.ipynb) things are becoming increasingly difficult. First, you will write a program to compute the readability of texts. Next, you will implement the basic algorithm that is behind authorship attribution!
- In [Chapter 6](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%206%20-%20Object%20Oriented%20Programming.ipynb) we will introduce you to the concept of Object Oriented Programming. You will implement a network structure with which you can analyze relations between people on Twitter.
- From Chapter 7 onwards, we will start working on more real applications. In [Chapter 7](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%207%20-%20Archiving%20and%20Searching.ipynb) we will work on systems for searching through collections of text. We introduce you to the field of Information Retrieval and build a simple information retrieval system. This chapter furthers your knowledge about Object Oriented Programming.
- In [Chapter 8](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%208%20-%20PDF%20Search%20App.ipynb) we create a complete web application to search through your own library of PDF files. This will be our first real application ready for use by end-users. The chapter introduces you to many modules available in the standard library as well as third-party modules.
- [Chapter 9](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%209%20-%20Learning%20from%20Examples.ipynb) will introduce you to some of the more advanced techniques used in automatic classification. We will implement a naive bayes classifier, show you a number of evaluation metrics and strategies and briefly address the question of parameter optimization.
- [Chapter 10](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%2010%20-%20Learning%20without%20Supervision.ipynb) focusses on hierarchical clustering, one of the important methods for unsupervized learning. We explain the basic methods for doining hierarchical clustering and create a simple implementation in Python.

This document describes the installation procedure for all the software needed for the Python class. If your stuck anywhere in the installation procedure, please do not hesitate to contact Folgert Karsdorp (folgert.karsdorp@meertens.knaw.nl).

## Sublime text

We advice you to install a good text editor, Sublime text 2 for example. However, you are absolutely free to use your own favorite editor. For Sublime Text 2 go to http://www.sublimetext.com/ download the version for your operating system and install.

In the course we will be using software that works best with Google Chrome. Firefox 6 (or above) and Safari will also work. Internet Explorer is not supported. 

We will be using Python 3 for our course. Lower versions are more or less supported, but not recommended.


## Installation
### All platforms

**We strongly advice you to install the Anaconda Python Distribution.** This distribution contains all the necessary modules and packages needed for this course. It is available for all platforms and provides a simple installation procedure/ You can download it from: http://continuum.io/downloads. More detailed installation instructions can be found here: http://docs.continuum.io/anaconda/install.html 

Anaconda's default installation is Python 2.7. However, we will use Python 3 in this course. To install all necessary packages for Python 3, type 

    conda create -n py34 python=3.4 anaconda

followed by

    source activate py34

at the command line. If you work on a Windows machine, use the following command instead:

    activate py34

(If this doesn't work, have a look here: http://continuum.io/blog/anaconda-python-3). After that you can start the course with double clicking the file start-windows.bat (if you are working on Windows) or start-unix.sh if you work with Linux or start-osx.command if you work on Mac OS X.

### Windows
Download and install the Anaconda Python Distribution (see above).

Double click the file start-windows.bat.

If everything goes right, this should open your browser (preferably Google Chrome or Firefox) on a page http://127.0.0.1:8888/ (or something similar) which says `IP[y]: Notebook'. If for some reason, the notebook is opened by Internet Explorer, copy the URL and paste that in either Google Chrome or Firefox.

### OS X 
Only take these steps if you know what you are doing. Otherwise, simply download and install the Anaconda Python Distribution (see above). After that, double click the file start-osx.command.

First you will need to install Xcode from the App Store. After you have successfully installed Xcode, open Xcode and go to Xcode -> preferences -> Downloads. Now click on the install button next to commandline tools. 

Open spotlight and type in `terminal' to open the terminal application. (You can also go to your applications folder and then to utilities where you'll find the terminal.app)

Cd to the folder where you downloaded or saved the file mac-installer.sh (probably in ~/Downloads) by using

    cd /folder/of/mac-installer.sh 

Run the installer with the following command. The installer will download some packages and will request for your password to install them.

    . mac-installer.sh

To check your installation, relaunch the terminal.app. Then type in 

    ipython3 notebook --matplotlib=inline

If everything went well this should open your browser (best with Google Chrome or Firefox) on the page http://127.0.0.1:8888/ which says IP[y]: Notebook.

### Linux (Ubuntu/Debian)

Only take these steps if you know what you are doing. Otherwise, simply download and install the Anaconda Python Distribution

First open a terminal, then type

    sudo apt-get install python3 ipython3 ipython3-notebook numpy scipy matplotlib 

If you run another Linux distribution, similar packages should be available. Finally execute the file start-unix.sh.

## Static Notebooks

This is a fall-back method.

[Chapter 1 - Getting started](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%201%20-%20Getting%20started.ipynb)

[Chapter 2 - First steps into text processing](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%202%20-%20First%20steps.ipynb)

[Chapter 3 - Text Analysis](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%203%20-%20Text%20analysis.ipynb)

[Chapter 4 - Programming principles](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%204%20-%20Programming%20principles.ipynb)

[Chapter 5 - Building NLP applications](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%25205%2520-%2520Building%2520NLP%2520Applications.ipynb)

[Chapter 6 - Objected Oriented Programming](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%206%20-%20Object%20Oriented%20Programming.ipynb)

[Chapter 7 - Searching large Collections of Text](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%207%20-%20Archiving%20and%20Searching.ipynb)

[Chapter 8 - Practical: Searching your own PDF library](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%208%20-%20PDF%20Search%20App.ipynb)

[Chapter 9 - Learning from Examples](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%209%20-%20Learning%20from%20Examples.ipynb)

[Chapter 10 - Learning without Supervision](http://nbviewer.ipython.org/urls/raw.github.com/fbkarsdorp/python-course/master/Chapter%2010%20-%20Learning%20without%20Supervision.ipynb)

## Contributors
- Folgert Karsdorp
- Maarten van Gompel
- Matt Munson