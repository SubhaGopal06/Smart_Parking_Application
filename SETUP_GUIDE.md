# Smart Parking System - Complete Setup Guide

## 📋 Project Overview

This is a **Smart Parking System** that:
- ✅ Predicts the best parking slot for users using Machine Learning (Naive Bayes)
- ✅ Provides real-time occupancy data from IoT sensors (ThingSpeak)
- ✅ Manages user authentication and reservations (Firebase)
- ✅ Displays a user-friendly web dashboard (Flask + Bootstrap)

---

## 🏗️ Architecture

```
┌──────────────────┐
│  Web Browser     │ (User Interface)
└────────┬─────────┘
         │
┌────────▼──────────┐
│  Flask App        │ (Backend Server)
│  (main.py)        │
└────────┬──────────┘
         │
    ┌────┴────┬────────┬──────────┐
    │          │        │          │
    ▼          ▼        ▼          ▼
 Firebase   ThingSpeak  ML Model  Static Files
 (Auth)     (IoT Data)  (Predict) (CSS/JS/Images)
```

---

## 📦 Prerequisites

Before you start, ensure you have:
- ✅ **Python 3.8+** (Download from [python.org](https://www.python.org/))
- ✅ **Firebase Project** (Created and configured)
- ✅ **keyfile.json** (Downloaded from Firebase console)
- ✅ **Git** (Optional, for version control)

---

## 🚀 Installation Steps

### Step 1: Set Up Python Environment

#### Windows:
```powershell
# Open PowerShell in your project directory
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Mac/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
# Ensure you're in the project directory with requirements.txt
pip install -r requirements.txt
```

**What gets installed:**
- `Flask` - Web framework
- `firebase-admin` - Firebase integration
- `scikit-learn` - Machine Learning library
- `pandas` - Data processing
- `numpy` - Numerical computing
- `requests` - HTTP requests
- And many more (see requirements.txt)

**Expected time:** 3-5 minutes

### Step 3: Configure Firebase

1. **Place keyfile.json in project root**
   - Download from Firebase Console → Project Settings → Service Accounts
   - Save it as `keyfile.json` in the same directory as `main.py`

2. **Verify the file path:**
   ```
   SmartParkingSystem-master/
   ├── main.py
   ├── config.py
   ├── keyfile.json  ← Should be here
   ├── data.csv
   ├── finalized_model.sav
   └── ... other files
   ```

### Step 4: Verify Configuration

Open `config.py` and verify:

```python
# Should point to your keyfile
FIREBASE_KEYFILE = PROJECT_ROOT / 'keyfile.json'

# Should match your Firebase database URL
FIREBASE_DB_URL = 'https://smartparkingsystem-58ec8-default-rtdb.firebaseio.com/'

# All parking slots should be configured
PARKING_SLOTS = {
    'A': {'x': 50, 'y': 0, 'price': 15, 'num': 1},
    'B': {'x': 0, 'y': 50, 'price': 20, 'num': 2},
    'C': {'x': 50, 'y': 100, 'price': 25, 'num': 3},
    'D': {'x': 100, 'y': 50, 'price': 30, 'num': 4}
}
```

---

## ▶️ Running the Application

### Start the Flask Server

```bash
# Make sure you're in the project directory
# And your virtual environment is activated

python main.py
```

**Expected output:**
```
WARNING in app.run_with_reloader: This is a development server. Do not use it in production.
Running on http://127.0.0.1:5000
```

### Access the Application

Open your browser and go to:
```
http://localhost:5000
```

You should see the **Smart Parking System Home Page**.

---

## 🧪 Testing the Application

### 1. **Test Home Page** ✅
- Navigate to `http://localhost:5000`
- You should see the index page

### 2. **Register New User**
- Click "Register" button
- Enter username and password
- System stores in Firebase

### 3. **Login**
- Enter registered credentials
- System authenticates via Firebase
- ML model predicts best parking slot
- You're redirected to dashboard

### 4. **Dashboard**
- View available and booked slots
- See real-time occupancy from ThingSpeak
- View your assigned slot and price

### 5. **Make Reservation**
- Enter car mark and number
- Click reserve
- Reservation saved to Firebase
- ThingSpeak updated with count

---

## 📊 How the ML Model Works

### Training Process
```python
# Run once to retrain model:
python naive_bayes.py
```

### Prediction Process
1. **User logs in** → Random coordinates generated (0-100, 0-100)
2. **Calculate distances** → Distance from user to each slot
3. **Create feature vector** → [dist_A, dist_B, dist_C, dist_D, price_A, price_B, price_C, price_D]
4. **ML prediction** → Naive Bayes classifier outputs best slot (A/B/C/D)
5. **Store in session** → User's parking space, distance, and rate

### Example
```
User Location: (30, 40)
Distances: A=50, B=45, C=70, D=85
Prices: A=15, B=20, C=25, D=30
Features: [50, 45, 70, 85, 15, 20, 25, 30]
Prediction: B (Best option based on distance + price)
```

---

## 📁 Project File Structure

```
SmartParkingSystem-master/
│
├── main.py                 # Main Flask application
├── config.py              # Configuration settings (NEW)
├── naive_bayes.py         # ML model training script
├── app.py                 # Unused (can be deleted)
│
├── data.csv               # ML training data (48 samples)
├── finalized_model.sav    # Trained Naive Bayes model
├── keyfile.json           # Firebase credentials (keep private!)
│
├── requirements.txt       # Python dependencies
├── links.txt              # ThingSpeak channel links
│
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   ├── login.html         # Login/Register page
│   ├── dashboard.html     # Parking dashboard
│   └── reservation.html   # Reservation page
│
├── static/                # Static files
│   ├── css/               # Stylesheets
│   │   ├── bootstrap.min.css
│   │   ├── styleDashboard.css
│   │   ├── styleRegister.css
│   │   ├── styleReserve.css
│   │   └── templatemo-style.css
│   ├── js/                # JavaScript files
│   │   ├── bootstrap.min.js
│   │   ├── jquery-1.9.1.min.js
│   │   ├── reservation.js
│   │   └── jquery.singlePageNav.min.js
│   ├── images/            # Images
│   └── fontawesome-5.5/   # Font Awesome icons
│
├── slot1.json             # ThingSpeak data for Slot A
├── slot2.json             # ThingSpeak data for Slot B
├── slot3.json             # ThingSpeak data for Slot C
├── slot4.json             # ThingSpeak data for Slot D
│
├── smartparkingsystem.json
├── sps.json
├── spsm.json
│
├── .gitignore
├── README.md
└── SETUP_GUIDE.md         # This file
```

---

## 🐛 Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'firebase_admin'"
**Solution:**
```bash
pip install firebase-admin
```

### Issue 2: "keyfile.json not found"
**Solution:**
- Ensure `keyfile.json` is in the project root directory
- Check the `config.py` path matches your file location
- Run from the correct directory

### Issue 3: "Database connection refused"
**Solution:**
- Verify Firebase database URL in `config.py`
- Check internet connection
- Verify Firebase credentials are valid

### Issue 4: "Port 5000 already in use"
**Solution:**
```bash
# Use a different port:
python -c "from main import app; app.run(port=5001)"

# Or stop the process using port 5000:
# Windows: netstat -ano | findstr :5000
# Mac/Linux: lsof -i :5000
```

### Issue 5: "Template not found"
**Solution:**
- Ensure `templates/` folder exists
- Check HTML files are in `templates/` directory
- Verify filenames match (case-sensitive on Mac/Linux)

---

## 🔐 Security Considerations

⚠️ **IMPORTANT**: Before deploying to production:

1. **Keep keyfile.json private** - Never commit to GitHub
2. **Change SECRET_KEY** - Update in `config.py`
3. **Remove DEBUG mode** - Set `DEBUG = False` in `config.py`
4. **Use environment variables** - For sensitive data:
   ```python
   import os
   SECRET_KEY = os.getenv('SECRET_KEY', 'default-key')
   ```
5. **Update passwords** - Hash them properly (use werkzeug.security)

---

## 📈 What Was Fixed

### Before (Broken Code):
```python
# ❌ Hardcoded paths
with open('D:\Download\SmartParkingSystemm\SmartParkingSystem-master\slot1.json') as f:
    data = json.load(f)

# ❌ API keys exposed
url = "https://api.thingspeak.com/update?api_key=7LHBQ6TZCKKWAYND&field1="+total

# ❌ Wrong Firebase path
cred = credentials.Certificate('SmartParkingSystem-master\keyfile.json')
```

### After (Fixed Code):
```python
# ✅ Relative paths from config
slot_json_path = config.get_slot_json_path(parking_space)
with open(slot_json_path, 'r') as f:
    data = json.load(f)

# ✅ API keys in config file
api_key = config.get_thingspeak_api_key(parking_space)
url = f"https://api.thingspeak.com/update?api_key={api_key}&field1={total}"

# ✅ Proper Firebase initialization
cred = credentials.Certificate(str(config.FIREBASE_KEYFILE))
firebase_admin.initialize_app(cred, {'databaseURL': config.FIREBASE_DB_URL})
```

---

## 📚 Additional Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Firebase Admin SDK**: https://firebase.google.com/docs/admin/setup
- **scikit-learn (ML Library)**: https://scikit-learn.org/
- **ThingSpeak**: https://thingspeak.com/docs

---

## 🤝 Next Steps

1. ✅ Install dependencies
2. ✅ Configure Firebase
3. ✅ Run the application
4. ✅ Test all features
5. 🔄 (Optional) Retrain ML model: `python naive_bayes.py`
6. 🚀 (Optional) Deploy to cloud (Heroku, AWS, Google Cloud)

---

## 📞 Support

If you encounter issues:
1. Check the **Troubleshooting** section above
2. Review the error message carefully
3. Ensure all files are in the correct locations
4. Verify all dependencies are installed: `pip list`

---

**Last Updated**: May 29, 2026  
**Project**: Smart Parking System  
**Status**: ✅ Ready for Testing
