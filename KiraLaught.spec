# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['KiraLaught.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('kira.png', '.'),               # ���������� kira.png � ������
        ('laugh.mp3', '.'),              # ���������� laugh.mp3 � ������
        ('laugh1.mp3', '.'),             # ���������� laugh1.mp3 � ������
        ('Scream_loud.mp3', '.')         # ���������� Scream_loud.mp3 � ������
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='KiraLaught',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
