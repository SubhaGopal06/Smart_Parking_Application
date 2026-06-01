"""
Smart Parking System Configuration File
All settings in one place for easy management
"""

import os
from pathlib import Path

# Get the project root directory (where this file is located)
PROJECT_ROOT = Path(__file__).parent

# ==================== FLASK CONFIGURATION ====================
SECRET_KEY = 'canada$God7972#'
DEBUG = True
TESTING = False

# ==================== FIREBASE CONFIGURATION ====================
# Path to Firebase keyfile (relative to project root)
FIREBASE_KEYFILE = PROJECT_ROOT / 'keyfile.json'
FIREBASE_DB_URL = 'https://smartparkingsystem-58ec8-default-rtdb.firebaseio.com/'
FIREBASE_COLLECTION = 'BookMySlot'

# ==================== ML MODEL CONFIGURATION ====================
# Path to the trained Naive Bayes model
ML_MODEL_PATH = PROJECT_ROOT / 'finalized_model.sav'
# Path to training data (for retraining if needed)
TRAINING_DATA_PATH = PROJECT_ROOT / 'data.csv'

# ==================== PARKING SLOTS CONFIGURATION ====================
# Define parking slots with coordinates and pricing
PARKING_SLOTS = {
    'A': {'x': 50, 'y': 0, 'price': 15, 'num': 1},
    'B': {'x': 0, 'y': 50, 'price': 20, 'num': 2},
    'C': {'x': 50, 'y': 100, 'price': 25, 'num': 3},
    'D': {'x': 100, 'y': 50, 'price': 30, 'num': 4}
}

# ==================== THINGSPEAK CONFIGURATION ====================
# ThingSpeak API credentials for each parking space
THINGSPEAK_CONFIG = {
    'A': {
        'channel_id': 1208300,
        'api_key': '7LHBQ6TZCKKWAYND',
        'field': 1,
        'json_file': PROJECT_ROOT / 'slot1.json'
    },
    'B': {
        'channel_id': 1208301,
        'api_key': 'YBW96SSU1G299SSS',
        'field': 1,
        'json_file': PROJECT_ROOT / 'slot2.json'
    },
    'C': {
        'channel_id': 1208302,
        'api_key': 'TOXRGRVZA1I28SIP',
        'field': 1,
        'json_file': PROJECT_ROOT / 'slot3.json'
    },
    'D': {
        'channel_id': 1208303,
        'api_key': 'I2L87XB3VT8P7L8V',
        'field': 1,
        'json_file': PROJECT_ROOT / 'slot4.json'
    }
}

# ==================== LOGGING CONFIGURATION ====================
LOG_LEVEL = 'INFO'
LOG_FILE = PROJECT_ROOT / 'logs' / 'app.log'

# Create logs directory if it doesn't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# ==================== HELPER FUNCTIONS ====================
def get_thingspeak_api_key(parking_space):
    """Get ThingSpeak API key for a specific parking space"""
    return THINGSPEAK_CONFIG.get(parking_space, {}).get('api_key')

def get_slot_json_path(parking_space):
    """Get the path to the slot JSON file for a parking space"""
    return THINGSPEAK_CONFIG.get(parking_space, {}).get('json_file')

def get_parking_slot_info(parking_space):
    """Get full information for a parking slot"""
    return PARKING_SLOTS.get(parking_space)
