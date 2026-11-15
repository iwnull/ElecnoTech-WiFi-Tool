# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for ElecnoTech Wi-Fi Tool
# Build on a Windows machine with:  pyinstaller ElecnoTech-WiFi-Tool.spec

a = Analysis(
    ['wifi.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pywifi', 'colorama', 'tqdm'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ElecnoTech-WiFi-Tool',
    console=True,
    icon='icon.ico' if __import__('os').path.exists('icon.ico') else None,
    upx=False,
)
