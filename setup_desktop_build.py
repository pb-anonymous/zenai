#!/usr/bin/env python3
"""
Complete Setup Guide for Building Desktop App
Handles all dependencies and configuration
"""

import os
import subprocess
import sys
from pathlib import Path

def run_cmd(cmd, description=""):
    """Run command and print status"""
    if description:
        print(f"\n{'='*60}")
        print(f"📦 {description}")
        print(f"{'='*60}")
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed: {description}")
        return False
    return True

def main():
    root = Path(__file__).parent
    
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║         PPT Generator Desktop App - Build Setup               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Install Python dependencies
    print("\n✅ Step 1: Installing Python dependencies...")
    if not run_cmd("pip install -r requirements-desktop.txt", "Python Dependencies"):
        sys.exit(1)
    
    # Step 2: Install Node.js dependencies
    print("\n✅ Step 2: Installing Node.js dependencies for frontend...")
    if not run_cmd("cd frontend && npm install", "Frontend Dependencies"):
        sys.exit(1)
    
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                    SETUP COMPLETE! ✨                         ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║                                                               ║
    ║  Next Step: Build the Desktop Application                    ║
    ║  Run: python build_desktop_app.py                            ║
    ║                                                               ║
    ║  This will:                                                  ║
    ║  1. Build React frontend                                     ║
    ║  2. Package with Flask backend                               ║
    ║  3. Create Windows executable                                ║
    ║  4. Generate launch script                                   ║
    ║                                                               ║
    ║  Output: dist/PPT-Generator/PPT-Generator.exe                ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

if __name__ == "__main__":
    main()
