@echo off
REM ============================================
REM  Build EXE for ElecnoTech Wi-Fi Tool
REM  Run this on a Windows machine with Python installed
REM ============================================
echo [1/3] Installing dependencies...
pip install pywifi colorama tqdm pyinstaller

echo [2/3] Cleaning old builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo [3/3] Building EXE...
pyinstaller --onefile --console ^
  --name "ElecnoTech-WiFi-Tool" ^
  --hiddenimport pywifi ^
  --hiddenimport colorama ^
  --hiddenimport tqdm ^
  --collect-all pywifi ^
  wifi.py

echo.
echo Done! Your EXE is in the "dist" folder.
pause
