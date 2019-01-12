# -*- mode: python -*-

block_cipher = None


a = Analysis(['shumaguan.py'],
             pathex=['/Users/zhanggong/Documents/Learn_file/Learn_Code/shumaguan'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='shumaguan',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='pic.ico')
app = BUNDLE(exe,
             name='shumaguan.app',
             icon='pic.ico',
             bundle_identifier=None)
