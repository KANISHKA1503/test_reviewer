"""
Real-time Change Detection Test

This file tests automatic webhook detection from GitHub.
When this PR is opened, the webhook should automatically trigger the agentic AI.
"""

def optimize_database_query(query):
    """Database query - missing optimization."""
    # ❌ N+1 query problem - not using JOIN
    return query.split(";")


def validate_user_age(age):
    """Validate age - missing validation."""
    # ❌ No check for negative numbers
    return age >= 18
