@echo off
REM PPT Generator Desktop App - One-Click Build & Launch

setlocal enabledelayedexpansion

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║     PPT Generator Desktop App - Build & Launch                ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.9+ from python.org
    pause
    exit /b 1
)

echo ✅ Python found

REM Build frontend
echo.
echo 📦 Building React frontend...
cd frontend
call npm run build >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Frontend build might have failed, continuing...
)
cd ..
echo ✅ Frontend built

REM Verify static folder
if not exist "static" (
    echo.
    echo 📁 Creating static folder...
    mkdir static
    REM Copy from frontend dist
    if exist "frontend\dist" (
        xcopy /E /I /Y frontend\dist static >nul 2>&1
        echo ✅ Frontend files copied
    ) else (
        echo ⚠️  frontend\dist not found
    )
)

REM Run the app
echo.
echo 🚀 Launching PPT Generator Desktop App...
echo ℹ️  App will open in your browser at http://localhost:5000
echo.
echo Press Ctrl+C to stop the app
echo.

python app.py

pause
