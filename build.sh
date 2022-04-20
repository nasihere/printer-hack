rm -rf build dist tray.spec                  
pyinstaller --add-data "*.png:." --add-data "*.ini:." tray.py