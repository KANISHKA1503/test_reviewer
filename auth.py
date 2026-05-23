# Authentication & System Diagnostic Module
import subprocess
import sqlite3

# ❌ 1. Hardcoded Secret / Sensitive Key
API_SECRET_KEY = "sk_live_" + "51NzY8H2jKlm9Pqw8JsdF982hKasd812"

def verify_user(username, password):
    # ❌ 2. SQL Injection Vulnerability in Raw Query
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def run_system_diagnostic(user_input):
    # ❌ 3. Shell Injection (subprocess with shell=True)
    # If user_input is "test; rm -rf /", this will execute arbitrary shell commands
    cmd = f"ping -c 1 {user_input}"
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return result.communicate()[0]

def execute_dynamic_calculation(formula):
    # ❌ 4. Remote Code Execution (eval on user input)
    return eval(formula)
