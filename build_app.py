#!/usr/bin/env python3
"""
Simplified Desktop App Builder
Creates a Windows executable from React frontend + Flask backend
"""

import os
import subprocess
import shutil
import sys
from pathlib import Path

def run_cmd(cmd, cwd=None):
    """Run shell command"""
    print(f"▶️ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"❌ Failed!")
        sys.exit(1)
    return result

def main():
    root = Path(__file__).parent
    frontend_dir = root / "frontend"
    static_dir = root / "static"
    frontend_dist = frontend_dir / "dist"
    
    print("""
╔═══════════════════════════════════════════════════════════════╗
║         Building PPT Generator Desktop Application            ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Verify frontend build exists
    print("\n📦 Step 1: Checking frontend build...")
    if not frontend_dist.exists():
        print(f"❌ Frontend dist not found. Building...")
        run_cmd("npm run build", cwd=str(frontend_dir))
    else:
        print("✅ Frontend build found")
    
    # Step 2: Copy frontend to static folder
    print("\n📁 Step 2: Preparing static files...")
    if static_dir.exists():
        shutil.rmtree(static_dir)
    static_dir.mkdir(parents=True, exist_ok=True)
    
    for item in frontend_dist.iterdir():
        if item.is_dir():
            shutil.copytree(item, static_dir / item.name)
        else:
            shutil.copy2(item, static_dir / item.name)
    print(f"✅ Copied frontend files to {static_dir}")
    
    # Step 3: Create PyInstaller spec
    print("\n⚙️ Step 3: Creating PyInstaller configuration...")
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('static', 'static'),
        ('generated_ppts', 'generated_ppts'),
    ],
    hiddenimports=['flask', 'flask_cors', 'pptx', 'requests', 'webbrowser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PPT-Generator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    spec_file = root / "app.spec"
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    print(f"✅ Created spec file")
    
    # Step 4: Build with PyInstaller
    print("\n🔨 Step 4: Building executable...")
    build_cmd = f"python -m PyInstaller app.spec --distpath dist --workpath build"
    run_cmd(build_cmd, cwd=str(root))
    
    # Step 5: Verify build
    exe_path = root / "dist" / "PPT-Generator" / "PPT-Generator.exe"
    if exe_path.exists():
        print(f"✅ Executable created: {exe_path}")
    else:
        print(f"❌ Executable not found at {exe_path}")
        sys.exit(1)
    
    # Step 6: Create launcher batch file
    print("\n📝 Step 6: Creating launcher...")
    launcher = root / "launch.bat"
    with open(launcher, 'w') as f:
        f.write('''@echo off
title PPT Generator - Desktop App
echo.
echo Starting PPT Generator...
echo.
cd /d "%~dp0"
start "" "dist\\PPT-Generator\\PPT-Generator.exe"
''')
    print(f"✅ Created launcher: {launcher}")
    
    # Summary
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                   ✨ BUILD SUCCESSFUL! ✨                     ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📁 Executable Location:                                      ║
║     dist\\PPT-Generator\\PPT-Generator.exe                    ║
║                                                               ║
║  🚀 To Launch:                                                ║
║     1. Double-click: launch.bat                              ║
║     2. Or run: dist\\PPT-Generator\\PPT-Generator.exe         ║
║                                                               ║
║  📦 To Distribute:                                            ║
║     Zip the folder: dist\\PPT-Generator                      ║
║     Users can extract and double-click PPT-Generator.exe     ║
║                                                               ║
║  💾 Size: ~500MB (includes Python + all dependencies)        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print(f"✅ Full path: {exe_path}")

if __name__ == "__main__":
    main()
