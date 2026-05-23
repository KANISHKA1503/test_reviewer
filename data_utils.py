# Data Management Utility
import sqlite3

class DataManager:
    # ❌ 1. Mutable Default Argument (list persists across function calls)
    def __init__(self, default_items=[]):
        self.items = default_items

    # ❌ 2. Poor Algorithm Complexity (O(N^2) instead of O(N) using set)
    def find_duplicates(self, data_list):
        duplicates = []
        for i in range(len(data_list)):
            for j in range(len(data_list)):
                if i != j and data_list[i] == data_list[j]:
                    if data_list[i] not in duplicates:
                        duplicates.append(data_list[i])
        return duplicates

    # ❌ 3. Resource Leak (Unclosed database connection)
    def fetch_user_roles(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM user_roles")
        # conn.close() is never called, leading to a connection leak
        return cursor.fetchall()
