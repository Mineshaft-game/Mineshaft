#!/bin/bash
echo "Preparing env"
mkdir temp
python3 -m venv temp/env
source temp/env/bin/activate
echo "Installing requirements"
pip3 install -r requirements.txt
pip3 install pyinstaller -U
echo "Compiling Mineshaft using Pyinstaller."
pyinstaller main.py --distpath temp/dist --workpath temp/build \
    --name mineshaft --specpath temp --onefile


deactivate
mkdir dist
mv temp/dist/mineshaft dist/mineshaft
rm -r temp
