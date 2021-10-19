#!/bin/bash
echo "creating directories"
mkdir build
mkdir build/mineshaft2d
echo "installing requirements"
pip3 install -r requirements.txt
echo "copying files and directories"
cp main.py build/mineshaft2d/__main__.py
cp -r assets build/mineshaft2d/
cp -r render build/mineshaft2d/
cp -r modes build/mineshaft2d/
cp -r resources build/mineshaft2d/
cp -r gen build/mineshaft2d/
cp buildtools/setup.py build/setup.py
cp README.md build/README.md
cp LICENSE build/LICENSE
echo "going into build"
cd build
echo "setup.py check"
python3 setup.py check
echo "Source distribution"
python3 setup.py sdist
echo "installing wheel"
pip3 install wheel
echo "Wheel distribution"
python3 setup.py bdist_wheel
echo "done"
