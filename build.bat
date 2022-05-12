rm -rf build dist tray.spec                  
pyinstaller.exe --onefile --add-data "*.exe;." --noconsole --windowed --add-data "*.pdf;." --add-data "*.png;." --add-data "*.ini;." tray.py