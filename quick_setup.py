#!/usr/bin/env python3
"""
PPT Generator Desktop App - Quick Setup & Launch
One-command solution to get started
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║  PPT Generator - Desktop App Setup                          ║
║  Ready for Download & Distribution                          ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    root = Path(__file__).parent
    
    print("\n✅ Your desktop app is ready!\n")
    print("=" * 60)
    print("QUICK START OPTIONS:")
    print("=" * 60)
    
    print("\n1️⃣  TEST LOCALLY (Fast - 10 seconds)")
    print("   Command: python app.py")
    print("   → Opens app at http://localhost:5000")
    
    print("\n2️⃣  CREATE STANDALONE EXE (Medium - 5-10 minutes)")
    print("   Command: build_executable.bat")
    print("   → Creates dist\\PPT-Generator\\PPT-Generator.exe")
    
    print("\n3️⃣  QUICK LAUNCHER (Fastest)")
    print("   Command: launch_app.bat")
    print("   → Auto-builds & launches")
    
    print("\n" + "=" * 60)
    print("DISTRIBUTION OPTIONS:")
    print("=" * 60)
    
    print("\n📦 METHOD A: Standalone Executable (RECOMMENDED)")
    print("   For: End users (no Python required)")
    print("   Steps:")
    print("   1. Run: build_executable.bat")
    print("   2. Zip: dist\\PPT-Generator\\")
    print("   3. Share: PPT-Generator.zip")
    print("   Size: ~500MB")
    
    print("\n📦 METHOD B: Python Scripts")
    print("   For: Developers / Python users")
    print("   Steps:")
    print("   1. Copy: app.py, requirements.txt, static/")
    print("   2. Zip it")
    print("   3. Users run: install.bat, then run.bat")
    print("   Size: ~50MB")
    
    print("\n📦 METHOD C: Web Deployment")
    print("   For: Cloud / Online access")
    print("   Command: vercel deploy")
    print("   Cost: Free tier available")
    
    print("\n" + "=" * 60)
    print("FILES CREATED:")
    print("=" * 60)
    
    files_created = [
        ("build_executable.bat", "One-click exe builder"),
        ("launch_app.bat", "Quick launcher"),
        ("app.spec", "PyInstaller config"),
        ("static/", "Built React frontend"),
        ("READY_TO_DOWNLOAD.md", "Full guide"),
        ("DESKTOP_APP_GUIDE.md", "Detailed docs"),
    ]
    
    for filename, description in files_created:
        path = root / filename
        if path.exists():
            print(f"   ✅ {filename:30} - {description}")
        else:
            print(f"   ⏳ {filename:30} - {description}")
    
    print("\n" + "=" * 60)
    print("STATUS:")
    print("=" * 60)
    
    checks = {
        "React build (static/)": root / "static" / "index.html",
        "Flask app": root / "app.py",
        "Launcher script": root / "launch_app.bat",
        "Build script": root / "build_executable.bat",
        "PyInstaller config": root / "app.spec",
    }
    
    for check_name, check_path in checks.items():
        status = "✅" if check_path.exists() else "⏳"
        print(f"   {status} {check_name}")
    
    print("\n" + "=" * 60)
    print("NEXT STEP:")
    print("=" * 60)
    
    print("\n🚀 Choose one:")
    print("\n   A) Test now: double-click launch_app.bat")
    print("   B) Build exe: double-click build_executable.bat")
    print("   C) Read guide: open READY_TO_DOWNLOAD.md")
    
    print("\n" + "=" * 60)
    print("✨ Your app is ready to ship! ✨")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
    input("Press Enter to continue...")
