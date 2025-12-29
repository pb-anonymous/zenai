#!/usr/bin/env python3
"""
PPT Generator - Feature Verification Script
Verifies that all components are properly installed and ready to use
"""

import os
import sys

def check_python_packages():
    """Check if required Python packages are installed"""
    print("\n🔍 Checking Python Packages...")
    packages = ["flask", "flask_cors", "pptx", "requests"]
    all_ok = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} (MISSING)")
            all_ok = False
    
    return all_ok

def check_file_structure():
    """Check if all necessary files exist"""
    print("\n📁 Checking File Structure...")
    
    required_files = {
        "Frontend": [
            "frontend/src/components/PPTGenerator.jsx",
            "frontend/src/components/PPTGenerator.css",
            "frontend/src/components/MainPage.jsx",
        ],
        "Backend": [
            "app.py",
            "executor.py",
            "ollama_brain.py",
        ],
        "Documentation": [
            "PPT_GENERATOR_README.md",
            "PPT_USAGE_GUIDE.md",
            "IMPLEMENTATION_SUMMARY.md",
            "QUICK_REFERENCE.md",
            "INSTALLATION_CHECKLIST.md",
            "VISUAL_GUIDE.md",
            "COMPLETE_README.md",
            "INDEX.md",
        ],
        "Setup": [
            "setup_ppt_generator.py",
        ]
    }
    
    all_ok = True
    for category, files in required_files.items():
        print(f"\n  {category}:")
        for file in files:
            if os.path.exists(file):
                print(f"    ✅ {file}")
            else:
                print(f"    ❌ {file} (MISSING)")
                all_ok = False
    
    return all_ok

def check_directories():
    """Check if required directories exist or can be created"""
    print("\n📂 Checking Directories...")
    
    directories = [
        "frontend/src/components",
        "generated_ppts",
    ]
    
    all_ok = True
    for directory in directories:
        if os.path.exists(directory):
            print(f"  ✅ {directory}")
        else:
            try:
                os.makedirs(directory, exist_ok=True)
                print(f"  ✅ {directory} (created)")
            except Exception as e:
                print(f"  ❌ {directory} (cannot create: {e})")
                all_ok = False
    
    return all_ok

def print_summary():
    """Print verification summary"""
    print("\n" + "="*60)
    print("✨ PPT GENERATOR VERIFICATION SUMMARY")
    print("="*60)
    
    python_ok = check_python_packages()
    files_ok = check_file_structure()
    dirs_ok = check_directories()
    
    print("\n" + "="*60)
    print("📊 VERIFICATION RESULTS:")
    print("="*60)
    
    results = {
        "Python Packages": python_ok,
        "File Structure": files_ok,
        "Directories": dirs_ok,
    }
    
    for check, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{check:30} {status}")
    
    overall = python_ok and files_ok and dirs_ok
    
    print("\n" + "="*60)
    if overall:
        print("🎉 OVERALL STATUS: ✅ READY TO USE")
    else:
        print("⚠️  OVERALL STATUS: ❌ NEEDS SETUP")
    print("="*60)
    
    if not overall:
        print("\n💡 NEXT STEPS:")
        if not python_ok:
            print("  1. Install Python packages:")
            print("     python setup_ppt_generator.py")
        if not files_ok:
            print("  2. Check that files were created correctly")
        if not dirs_ok:
            print("  3. Create missing directories manually:")
            print("     mkdir -p generated_ppts")
        print("\n  Then run this script again to verify!")
    else:
        print("\n🚀 QUICK START:")
        print("  Terminal 1: python app.py")
        print("  Terminal 2: cd frontend && npm run dev")
        print("  Then open: http://localhost:5173")
        print("  Click: 📊 Generate PPT button")

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════╗
║   PPT GENERATOR VERIFICATION 🔍      ║
║   Checking System Status             ║
╚══════════════════════════════════════╝
    """)
    
    print_summary()
    
    print("\n📚 Documentation:")
    print("  • Quick Start: QUICK_REFERENCE.md")
    print("  • Installation: INSTALLATION_CHECKLIST.md")
    print("  • Usage Guide: PPT_USAGE_GUIDE.md")
    print("  • Full Index: INDEX.md")
    
    print("\n" + "="*60)
