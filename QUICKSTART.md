# Smart Parking System - Quick Start Guide

## 🚀 5-Minute Setup

### Step 1: Verify keyfile.json is in place
```
Your project folder should have:
- main.py
- config.py (NEW - created for you)
- keyfile.json (Your Firebase credentials)
- All other files...
```

### Step 2: Install Python packages
```powershell
# Open PowerShell in your project directory

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

⏱️ **Wait 3-5 minutes for installation to complete**

### Step 3: Run the app
```powershell
python main.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 4: Open in Browser
```
http://localhost:5000
```

---

## 📋 What Was Done For You

✅ **Created config.py**
- Centralized all configuration
- Fixed all hardcoded paths
- All API keys stored safely
- Cross-platform path handling

✅ **Updated main.py**
- Uses config.py for settings
- Fixed Firebase initialization
- Fixed all file paths
- Better error handling

✅ **Updated naive_bayes.py**
- Uses config.py for paths
- Can retrain ML model anytime
- Better logging

✅ **Created SETUP_GUIDE.md**
- Comprehensive documentation
- Troubleshooting section
- Architecture explanation

---

## 🧪 Test Checklist

After app starts, test these:

- [ ] Visit http://localhost:5000 → See home page
- [ ] Click "Register" → Create test account (username: test, password: test123)
- [ ] Click "Login" → Enter credentials
- [ ] See dashboard with available/booked slots
- [ ] Click "Reserve" → Make a reservation
- [ ] Logout → Return to home

---

## 🐛 Common Issues & Fixes

### "Module not found: firebase_admin"
```powershell
pip install firebase-admin --upgrade
```

### "keyfile.json not found"
- Check file is in project root (same folder as main.py)
- File name must be exactly: `keyfile.json`

### "Port 5000 already in use"
```powershell
# Use port 5001 instead
# Edit config.py last line, or run:
python -c "from main import app; app.run(port=5001)"
```

### "Connection refused"
- Check internet connection
- Verify Firebase database URL in config.py
- Ensure keyfile.json is valid

---

## 📞 Need Help?

1. Read SETUP_GUIDE.md (more detailed)
2. Check the error message in terminal
3. Review Troubleshooting section in SETUP_GUIDE.md

---

**Status**: ✅ Ready to Run!
