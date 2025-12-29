#!/usr/bin/env python3
"""
Build Script for Desktop Application
Creates a standalone Windows executable combining React frontend and Flask backend
"""

import os
import subprocess
import shutil
import sys
import json
from pathlib import Path

def run_command(cmd, cwd=None):
    """Execute a command and handle errors"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"❌ Error: Command failed with return code {result.returncode}")
        sys.exit(1)
    return result

def main():
    print("🚀 Building Desktop Application...")
    
    root_dir = Path(__file__).parent
    frontend_dir = root_dir / "frontend"
    build_dir = root_dir / "build"
    dist_dir = root_dir / "dist"
    
    # Step 1: Build React frontend
    print("\n📦 Step 1: Building React frontend...")
    if not frontend_dir.exists():
        print(f"❌ Frontend directory not found: {frontend_dir}")
        sys.exit(1)
    
    try:
        run_command("npm install", cwd=str(frontend_dir))
        run_command("npm run build", cwd=str(frontend_dir))
        print("✅ Frontend built successfully!")
    except Exception as e:
        print(f"❌ Failed to build frontend: {e}")
        sys.exit(1)
    
    # Step 2: Copy built frontend to Flask static folder
    print("\n📋 Step 2: Setting up Flask static files...")
    frontend_dist = frontend_dir / "dist"
    if not frontend_dist.exists():
        print(f"❌ Frontend dist not found: {frontend_dist}")
        sys.exit(1)
    
    # Clean and prepare static directory
    static_dir = root_dir / "static"
    if static_dir.exists():
        shutil.rmtree(static_dir)
    static_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy all frontend files
    for item in frontend_dist.iterdir():
        if item.is_dir():
            shutil.copytree(item, static_dir / item.name)
        else:
            shutil.copy2(item, static_dir / item.name)
    
    print("✅ Frontend files copied to static directory!")
    
    # Step 3: Create PyInstaller spec file
    print("\n⚙️  Step 3: Creating PyInstaller configuration...")
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('static', 'static'),
        ('templates', 'templates'),
        ('generated_ppts', 'generated_ppts'),
        ('ppt_templates', 'ppt_templates'),
    ],
    hiddenimports=['flask', 'flask_cors', 'pptx', 'requests', 'ollama'],
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
    icon='app_icon.ico',
)
'''
    
    spec_file = root_dir / "app.spec"
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    print(f"✅ Created spec file: {spec_file}")
    
    # Step 4: Build executable with PyInstaller
    print("\n🔨 Step 4: Building executable with PyInstaller...")
    try:
        run_command(f"pyinstaller app.spec --distpath dist --workpath build --specpath .", cwd=str(root_dir))
        print("✅ Executable built successfully!")
    except Exception as e:
        print(f"❌ Failed to build executable: {e}")
        sys.exit(1)
    
    # Step 5: Create launcher batch file
    print("\n📝 Step 5: Creating launcher files...")
    launcher_batch = root_dir / "launch.bat"
    launcher_content = '''@echo off
echo Starting PPT Generator Desktop App...
cd /d "%~dp0"
start "" "dist\\PPT-Generator\\PPT-Generator.exe"
'''
    with open(launcher_batch, 'w') as f:
        f.write(launcher_content)
    print(f"✅ Created launcher: {launcher_batch}")
    
    # Step 6: Print results
    exe_path = root_dir / "dist" / "PPT-Generator" / "PPT-Generator.exe"
    print("\n" + "="*60)
    print("✨ Desktop Application Built Successfully! ✨")
    print("="*60)
    print(f"\n📁 Location: {exe_path}")
    print(f"\n🚀 To run the app:")
    print(f"   1. Double-click: launch.bat")
    print(f"   2. Or run: {exe_path}")
    print(f"\n📦 Application folder: {root_dir / 'dist' / 'PPT-Generator'}")
    print(f"\n💾 For distribution, zip the folder: {root_dir / 'dist' / 'PPT-Generator'}")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
