#!/bin/bash
echo "Creating directories"
mkdir build
mkdir build/mineshaft2d
echo "Installing requirements"
pip3 install -r requirements.txt
echo "Copying files and directories"
cp main.py build/mineshaft2d/__main__.py
cp -r assets build/mineshaft2d/
cp -r render build/mineshaft2d/
cp -r modes build/mineshaft2d/
cp -r resources build/mineshaft2d/
cp -r gen build/mineshaft2d/
cp buildtools/setup.py build/setup.py
cp README.md build/README.md
cp LICENSE build/LICENSE
echo "Going into build"
cd build
echo "----------Setup.py check----------"
python3 setup.py check
echo "----------Source distribution----------"
python3 setup.py sdist
echo "\n\n\n\nInstalling wheel\n\n\n\n"
pip3 install wheel
echo "----------Wheel distribution----------"
python3 setup.py bdist_wheel
echo "\n\n\n\n\n\ndone"
