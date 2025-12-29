#!/usr/bin/env python3
"""
PPT Generator Setup and Installation Guide
==========================================

This script helps you set up the PowerPoint Generator feature.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required Python packages"""
    print("📦 Installing Python requirements...")
    requirements = [
        "flask",
        "flask-cors", 
        "python-pptx",
        "requests"
    ]
    
    for package in requirements:
        try:
            print(f"  Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"  ✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"  ❌ Failed to install {package}")
            return False
    
    return True

def create_directories():
    """Create required directories"""
    print("\n📁 Creating directories...")
    directories = [
        "generated_ppts",
        "frontend/public",
        "zen-backend"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✅ Created/verified: {directory}")
    
    return True

def verify_installation():
    """Verify all dependencies are installed"""
    print("\n🔍 Verifying installation...")
    
    modules = ["flask", "flask_cors", "pptx", "requests"]
    all_ok = True
    
    for module in modules:
        try:
            __import__(module)
            print(f"  ✅ {module} is installed")
        except ImportError:
            print(f"  ❌ {module} is NOT installed")
            all_ok = False
    
    return all_ok

def print_instructions():
    """Print usage instructions"""
    print("\n" + "="*60)
    print("🎉 PPT GENERATOR SETUP COMPLETE!")
    print("="*60)
    print("""
🚀 QUICK START:

1. Start the backend:
   python app.py
   
   The Flask server will start on http://localhost:5000

2. In another terminal, start the frontend:
   cd frontend
   npm run dev
   
   The React app will start on http://localhost:5173

3. Open your browser and go to http://localhost:5173

4. Click the "📊 Generate PPT" button in the top navigation

5. Start speaking to create slides with images!

📋 FEATURES:
   ✅ Voice input for slide content
   ✅ Auto-fetch high-quality images
   ✅ Professional PowerPoint output
   ✅ Easy slide management
   ✅ One-click download

🎨 WHAT EACH BUTTON DOES:
   • 🎤 Start Speaking - Begin voice input
   • ➕ Add Slide - Save the spoken content as a slide
   • 🗑️ - Delete a slide
   • 📊 Generate PowerPoint - Create and download the PPT

⚙️ CONFIGURATION:
   - Image API: Pexels (free, high-quality)
   - Backend Port: 5000
   - Frontend Port: 5173
   - Output Directory: generated_ppts/

📚 FOR MORE INFO:
   - Read: PPT_GENERATOR_README.md
   - Check: app.py for backend endpoints
   - Check: frontend/src/components/PPTGenerator.jsx for UI

🐛 TROUBLESHOOTING:
   - Microphone not working? Check browser permissions
   - Images not loading? Check internet connection
   - PPT generation failed? Verify Flask is running
   
⚠️ IMPORTANT REQUIREMENTS:
   - Python 3.7+
   - Node.js 14+
   - Modern browser (Chrome, Edge, Safari)
   - Internet connection (for fetching images)

Happy presenting! 🎉
""")
    print("="*60)

def main():
    print("""
╔══════════════════════════════════════╗
║   PPT GENERATOR SETUP WIZARD 🎤      ║
║   Speak to Create PowerPoint          ║
╚══════════════════════════════════════╝
    """)
    
    # Step 1: Install requirements
    if not install_requirements():
        print("\n❌ Failed to install requirements")
        sys.exit(1)
    
    # Step 2: Create directories
    if not create_directories():
        print("\n❌ Failed to create directories")
        sys.exit(1)
    
    # Step 3: Verify installation
    if not verify_installation():
        print("\n⚠️  Some packages may not be installed correctly")
    
    # Step 4: Print instructions
    print_instructions()

if __name__ == "__main__":
    main()
