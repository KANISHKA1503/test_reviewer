"""
Webhook Security Test Module
This file contains intentional code issues for agent analysis
"""

import os
import requests
from flask import Flask, request

app = Flask(__name__)

# SECURITY ISSUE: Hardcoded API key
API_KEY = "sk_live_abc123xyz789_NEVER_DO_THIS"
DATABASE_PASSWORD = "admin123"

def fetch_user_data(user_id):
    """DESIGN ISSUE: N+1 Query Pattern"""
    users = []
    for i in range(100):
        # This makes 100 separate requests instead of one bulk query
        response = requests.get(f"https://api.example.com/user/{user_id}/data/{i}")
        users.append(response.json())
    return users

@app.route('/process', methods=['POST'])
def process_webhook():
    """BEST PRACTICE ISSUE: No input validation"""
    data = request.json
    # Directly using user input without validation
    command = data['command']
    os.system(command)  # SQL Injection / Command Injection vulnerability
    return {'status': 'processed'}

def calculate_score(values):
    """PERFORMANCE ISSUE: Inefficient algorithm"""
    # O(n²) algorithm when O(n) exists
    result = []
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i] == values[j]:
                result.append(values[i])
    return list(set(result))

# CODE STYLE ISSUE: Inconsistent naming
def FetchData():  # PascalCase instead of snake_case
    x=10  # No spaces around operator
    y=20
    z=x+y  # Poor variable naming
    return z

class DataProcessor:
    """DESIGN ISSUE: Missing error handling"""
    def __init__(self):
        self.db = None
    
    def connect(self, connection_string):
        # No try-except, will crash on connection failure
        self.db = self.connect_database(connection_string)
    
    def connect_database(self, cs):
        """MAINTAINABILITY ISSUE: Unused parameter"""
        return "connection_object"

# MEMORY LEAK: Unbounded cache
cache = {}
def cache_result(key, value):
    cache[key] = value  # Never cleared, grows indefinitely
