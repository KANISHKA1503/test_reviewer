"""
Auto-Detection Test Module

This module tests automatic change detection by the agentic AI system.
It contains intentional code issues for the AI to identify.
"""

def process_user_input(user_data):
    """Process user input - missing validation."""
    # No input validation - potential security issue
    name = user_data["name"]
    age = user_data["age"]
    email = user_data["email"]
    
    return f"User: {name}, Age: {age}, Email: {email}"


def calculate_discount(price, discount_percent):
    """Calculate discounted price - missing error handling."""
    discounted = price * (1 - discount_percent / 100)
    return discounted  # Could be negative if discount > 100


def fetch_data_from_api(url):
    """Fetch data with hardcoded credentials."""
    import requests
    
    # ❌ HARDCODED CREDENTIALS - Security risk!
    api_key = "sk-1234567890abcdef"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(url, headers=headers)
    return response.json()


def parse_database_url(connection_string):
    """Parse database URL - SQL injection vulnerable."""
    # ❌ Vulnerable to SQL injection
    parts = connection_string.split(";")
    config = {}
    
    for part in parts:
        key, value = part.split("=")
        config[key] = value
    
    return config


class UserProcessor:
    """Process user data - design issues."""
    
    def __init__(self):
        self.users = []
        self.cache = {}
    
    def add_user(self, user):
        """Add user to list - no duplicate checking."""
        self.users.append(user)
        self.cache = {}  # Clear cache on every add - inefficient
    
    def get_user(self, user_id):
        """Get user - inefficient lookup."""
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
    
    def get_all_users(self):
        """Return all users - memory leak potential."""
        # ❌ Returns reference to internal list - can be modified externally
        return self.users
