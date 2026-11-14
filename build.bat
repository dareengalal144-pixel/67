@echo off
chcp 65001 >nul
echo [1/3] Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pyinstaller
echo [2/3] Building ASHE.exe ...
python -m PyInstaller --noconfirm --onefile --windowed --name ASHE --collect-all webview ashe.py
echo [3/3] Done. The program is at: dist\ASHE.exe
pause
