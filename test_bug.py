import os
import sqlite3

def fetch_user(username):
    # SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    
    # Command Injection vulnerability
    os.system(f"echo 'Fetching user: {username}'")
    
    # Code smell: Unused variable
    result_code = 123
    
    return cursor.fetchall()
