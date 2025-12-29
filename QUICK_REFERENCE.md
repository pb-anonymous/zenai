# 🎤 PPT Generator - Quick Reference Card

## 🚀 Quick Start (60 seconds)

### Step 1: Start Services
```bash
# Terminal 1: Backend
python app.py

# Terminal 2: Frontend (in frontend folder)
npm run dev
```

### Step 2: Access Feature
1. Open browser → http://localhost:5173
2. Click **"📊 Generate PPT"** button in top nav

### Step 3: Create Slide
1. Click **"🎤 Start Speaking"**
2. Speak your content
3. Click **"➕ Add Slide"**

### Step 4: Generate & Download
1. Click **"📊 Generate PowerPoint"**
2. File downloads automatically
3. Open with PowerPoint or Google Slides

---

## 🎤 Speaking Tips

### DO's ✅
- Speak clearly and naturally
- Use descriptive keywords
- Complete thoughts
- Speak at normal pace
- Test microphone first

### DON'Ts ❌
- Don't rush or mumble
- Don't use jargon alone
- Don't be too quiet
- Don't have background noise
- Don't forget permissions

### Example Good Input
```
"The impact of renewable energy on climate change"
"Cloud computing revolutionizes business infrastructure"
"Data analytics drives strategic decision making"
```

---

## 🎨 UI Quick Guide

| Button | Function |
|--------|----------|
| 🎤 Start Speaking | Begin voice input |
| 🎤 Listening... | Stop listening |
| ➕ Add Slide | Save spoken content |
| 🗑️ | Delete a slide |
| 📊 Generate PowerPoint | Create & download PPT |
| ✕ | Close generator |

---

## 📋 File Locations

```
Frontend Components:
  • PPTGenerator.jsx (Main component)
  • PPTGenerator.css (Styling)
  
Backend:
  • app.py (REST endpoints)
  
Output:
  • generated_ppts/ (PowerPoint files)
  
Documentation:
  • PPT_GENERATOR_README.md
  • PPT_USAGE_GUIDE.md
  • IMPLEMENTATION_SUMMARY.md
```

---

## 🔧 Setup Commands

```bash
# Install dependencies
python setup_ppt_generator.py

# Or manually
pip install flask flask-cors python-pptx requests

# Create output directory
mkdir generated_ppts
```

---

## 📊 What You Get

```
Title Slide:
  ✓ Presentation Title
  ✓ Current Date
  ✓ Professional Format

Content Slides (per slide):
  ✓ Title in Cyan (#00d4ff)
  ✓ High-quality image
  ✓ Your spoken text
  ✓ Dark professional background
  ✓ Ready-to-present format
```

---

## 🌐 APIs & Services

| Service | Purpose | Free? | Key? |
|---------|---------|-------|------|
| Web Speech API | Voice recognition | ✅ | ✅ |
| Pexels API | Image search | ✅ | Included |
| Flask | Backend server | ✅ | ✅ |

---

## ⚙️ System Requirements

- Python 3.7+
- Node.js 14+
- Modern browser (Chrome/Edge/Safari)
- Internet connection
- Microphone
- ~50MB disk space

---

## 🐛 Troubleshooting (Instant Fixes)

| Problem | Fix |
|---------|-----|
| No microphone | Allow permission in browser |
| Speech not recognized | Speak louder, clearer |
| Images not loading | Check internet connection |
| PPT won't generate | Verify Flask running on :5000 |
| File won't download | Check browser download settings |

---

## 🎯 Common Workflows

### Marketing Pitch
```
1. "Company Overview and Mission"
2. "Product Features and Benefits"
3. "Market Opportunity and Growth"
4. "Contact Information and Call to Action"
```

### Educational Presentation
```
1. "Topic Introduction and Importance"
2. "Key Concept Explanation"
3. "Real-World Examples"
4. "Summary and Conclusions"
```

### Product Demo
```
1. "Problem Statement"
2. "Solution Overview"
3. "Key Features Demonstration"
4. "Pricing and Availability"
```

---

## 📱 Browser Compatibility

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome | ✅ Excellent | Recommended |
| Edge | ✅ Excellent | Recommended |
| Safari | ✅ Good | iOS/macOS |
| Firefox | ⚠️ Limited | May need setup |

---

## 💾 File Management

```
Generated Files:
  Location: generated_ppts/
  Format: .pptx (PowerPoint 2016+)
  Size: 2-10 MB
  Editable: Yes, fully editable
  Shareable: Yes, via email/cloud
```

---

## ⏱️ Typical Timings

| Task | Time |
|------|------|
| Open feature | 1 sec |
| Speak & add slide | 30 sec |
| Add 5 slides | 2-3 min |
| Generate PPT | 5-10 sec |
| Download | < 5 sec |
| **Total** | **~5 min** |

---

## 🎓 Pro Tips

1. **Plan First** - Write outline before speaking
2. **Use Keywords** - Mention key topics for images
3. **Keep Concise** - 1-2 sentences per slide best
4. **Natural Tone** - Avoid robotic speech
5. **Check Output** - Review before sharing

---

## 🔐 Security & Privacy

- ✅ All data processed locally (no cloud save)
- ✅ Images from free royalty-free service
- ✅ No personal data stored
- ✅ Files deleted after download
- ✅ HTTPS for image fetch

---

## 📞 Quick Support

### Issue: Voice not working
```
→ Check microphone permissions
→ Refresh browser page
→ Try Chrome/Edge if using Firefox
```

### Issue: Images not showing
```
→ Check internet connection
→ Wait 5 min and try again
→ Fallback images still work
```

### Issue: PPT generation fails
```
→ Verify Flask running (python app.py)
→ Check generated_ppts folder exists
→ Install dependencies (python setup_ppt_generator.py)
```

---

## 📚 Full Documentation

For complete details, see:
- **PPT_GENERATOR_README.md** (Feature guide)
- **PPT_USAGE_GUIDE.md** (Examples & tips)
- **IMPLEMENTATION_SUMMARY.md** (Technical details)

---

## ✨ Feature Highlights

🎤 **Voice Input** - Speak naturally
🎨 **Beautiful Design** - Professional theme
🖼️ **Auto Images** - Relevant images auto-selected
📊 **Easy Export** - One-click PowerPoint download
⚡ **Fast** - 5-10 seconds per slide
✏️ **Editable** - Fully editable output files
📱 **Responsive** - Works on all devices

---

**🚀 Ready to create amazing presentations?**

*Click the button and start speaking!*
