SHELL = /bin/bash
dist/mineshaft.AppImage:
	python3 -m venv ./env
	source ./env/bin/activate; pip3 install -r requirements.txt; pip3 install pyinstaller; pyinstaller --onefile main.py; deactivate
	mv dist/main dist/mineshaft.AppImage
	rm -r build main.spec env

clean:
	rm -r dist
