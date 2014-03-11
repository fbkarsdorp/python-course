#!/bin/bash
mkdir tmp
cd tmp
echo "Downloading Python 3"
curl http://www.python.org/ftp/python/3.3.5/python-3.3.5-macosx10.6.dmg > python-3.3.5-macosx10.6.dmg


sleep 1
hdiutil attach python-3.3.5-macosx10.6.dmg
sleep 2

cd /Volumes/Python\ 3.3.5
echo "The installer will query for your password in order to install Python 3 on your system"
sudo installer -pkg Python.mpkg -target /
cd -

echo "Downloading and installing distribute tools"
curl https://pypi.python.org/packages/source/d/distribute/distribute-0.6.49.tar.gz > distribute-0.6.49.tar.gz
tar xf distribute-0.6.49.tar.gz
cd distribute-0.6.49.tar.gz
python3 setup.py install


echo "Downloading and installing iPython 3 and dependencies"
cd ..
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 ipython
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 readline
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 tornado
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 pyzmq
cd ..
#echo "export PATH=\"/Library/Frameworks/Python.framework/Versions/3.3/bin/:\$PATH\"" >> ~/.bash_profile

echo -n "Do you want the installer to add Python 3 to your default path in your ~/.profile? (y/n)"
read yn
yn="$(tr [A-Z] [a-z] <<< "$yn")"
if [ "$yn" == "y" ]; then
    echo "export PATH=\"/Library/Frameworks/Python.framework/Versions/3.3/bin/:\$PATH\"" >> ~/.profile
else
    echo "Python should now be installed in /Library/Frameworks/Python.framework/Versions/3.3/bin/"
fi

curl https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.js > $(ipython locate)/nbextensions/toc.js
curl https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.css > $(ipython locate)/nbextensions/toc.css
echo "IPython.load_extensions('toc');" >> $(ipython locate profile)/static/custom/custom.js

export PATH="/Library/Frameworks/Python.framework/Versions/3.3/bin/:$PATH"
