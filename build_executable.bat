@echo off
REM One-Click Desktop Executable Builder
REM This will create PPT-Generator.exe in the dist folder

setlocal enabledelayedexpansion

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║     PPT Generator - Build Standalone Executable               ║
echo ║     (This will take 5-10 minutes)                             ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Step 1: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found
    pause
    exit /b 1
)

REM Step 2: Install PyInstaller
echo 📦 Ensuring PyInstaller is installed...
python -m pip install PyInstaller -q
if errorlevel 1 (
    echo ⚠️  PyInstaller installation might have failed
)

REM Step 3: Build frontend
echo.
echo 📦 Building React frontend...
cd frontend
call npm run build >nul 2>&1
cd ..

REM Step 4: Copy to static
echo 📁 Preparing static files...
if exist "static" rmdir /s /q static >nul 2>&1
mkdir static
xcopy /E /I /Y frontend\dist static >nul 2>&1

REM Step 5: Create spec file
echo ⚙️  Creating PyInstaller configuration...

(
echo # -*- mode: python ; coding: utf-8 -*-
echo a = Analysis(
echo     ['app.py'],
echo     pathex=[],
echo     binaries=[],
echo     datas=[
echo         ('static', 'static'),
echo         ('generated_ppts', 'generated_ppts'),
echo     ],
echo     hiddenimports=['flask', 'flask_cors', 'pptx', 'requests', 'webbrowser'],
echo     hookspath=[],
echo     hooksconfig={},
echo     runtime_hooks=[],
echo     excludedimports=[],
echo     noarchive=False,
echo ^)
echo pyz = PYZ(a.pure, a.zipped_data, cipher=None^)
echo exe = EXE(
echo     pyz,
echo     a.scripts,
echo     a.binaries,
echo     a.zipfiles,
echo     a.datas,
echo     [],
echo     name='PPT-Generator',
echo     debug=False,
echo     bootloader_ignore_signals=False,
echo     strip=False,
echo     upx=True,
echo     upx_exclude=[],
echo     runtime_tmpdir=None,
echo     console=False,
echo     disable_windowed_traceback=False,
echo     target_arch=None,
echo     codesign_identity=None,
echo     entitlements_file=None,
echo ^)
) > app.spec

REM Step 6: Build with PyInstaller
echo.
echo 🔨 Building executable (this may take a few minutes)...
echo.
python -m PyInstaller app.spec --distpath dist --workpath build

REM Step 7: Verify
echo.
if exist "dist\PPT-Generator\PPT-Generator.exe" (
    echo ✅ SUCCESS! Executable created!
    echo.
    echo 📁 Location: dist\PPT-Generator\PPT-Generator.exe
    echo.
    echo 🚀 To run:
    echo    1. Double-click: dist\PPT-Generator\PPT-Generator.exe
    echo    2. Or run: call dist\PPT-Generator\PPT-Generator.exe
    echo.
    echo 📦 To distribute:
    echo    1. Zip folder: dist\PPT-Generator
    echo    2. Share PPT-Generator.zip with users
    echo    3. Users extract and run PPT-Generator.exe
    echo.
    echo Size: ~500MB (includes Python + all dependencies^)
    echo.
    echo ✨ Your desktop app is ready!
) else (
    echo ❌ Build failed. Exe not created at dist\PPT-Generator\PPT-Generator.exe
    echo.
    echo Try these fixes:
    echo 1. Ensure Python 3.9+ is installed
    echo 2. Run: pip install PyInstaller
    echo 3. Check disk space (need ~1GB free^)
    echo 4. Try again: python -m PyInstaller app.spec --distpath dist --workpath build
)

echo.
pause
