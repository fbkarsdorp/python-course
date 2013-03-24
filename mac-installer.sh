#!/bin/bash
mkdir tmp
cd tmp
curl http://python.org/ftp/python/3.3.0/python-3.3.0-macosx10.6.dmg > python-3.3.0-macosx10.6.dmg
hdiutil attach python-3.3.0-macosx10.6.dmg
cd /Volumes/Python\ 3.3.0
sudo installer -pkg Python.mpkg -target /
cd -
curl https://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz > distribute-0.6.35.tar.gz
tar xf distribute-0.6.35.tar.gz
cd distribute-0.6.35
python3 setup.py install
cd ..
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 ipython
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 readline
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 tornado
/Library/Frameworks/Python.framework/Versions/3.3/bin/easy_install-3.3 pyzmq
cd ..
echo "export PATH=\"/Library/Frameworks/Python.framework/Versions/3.3/bin/:\$PATH\"" >> ~/.bash_profile
echo "export PATH=\"/Library/Frameworks/Python.framework/Versions/3.3/bin/:\$PATH\"" >> ~/.profile
export PATH="/Library/Frameworks/Python.framework/Versions/3.3/bin/:$PATH"
