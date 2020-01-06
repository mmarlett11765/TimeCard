# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Time_card.py'],
             pathex=['C:\\Users\\mmarlett\\Documents\\Python Scripts\\TimeCard'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('Timer.png','C:\\Users\\mmarlett\\Documents\\Python Scripts\\TimeCard\\Timer.png', "DATA"),
			('timer_256x256.ico','C:\\Users\\mmarlett\\Documents\\Python Scripts\\TimeCard\\timer_256x256.ico', "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='TimeCard',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
		  icon = 'C:\\Users\\mmarlett\\Documents\\Python Scripts\\TimeCard\\timer_256x256.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='TimeCard')
