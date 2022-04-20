rm -rf build dist tray.spec                  
#pyinstaller --noconsole --add-data "*.pdf:." --add-data "*.png:." --add-data "*.ini:." tray.py
pyinstaller --noconsole --windowed --add-data "*.pdf:." --add-data "*.png:." --add-data "*.ini:." tray.py
