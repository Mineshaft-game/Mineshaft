#!/bin/bash
VERSION=1
echo "Mineshaft 2D installer script v" $VERSION
echo
echo "This script will install the required packages,"
echo "Set up the repository,"
echo "And create the remotes"
echo

echo "Installing requirements"
pip3 install -r requirements.txt -q

echo "Initializing submodules"
git submodule init

echo "Creating the remotes"
git remote add gitlab https://gitlab.com/double-fractal/mineshaft2d/Mineshaft.git

echo
echo "Done"

