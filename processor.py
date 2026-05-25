# Report Processor
# ❌ 1. Unused Imports
import os
import sys
import datetime

def calc(a, b, c):
    # ❌ 2. Spaghetti Code / High Cognitive Complexity
    # ❌ 3. Cryptic naming and duplicate code blocks
    if a > 10:
        if b < 5:
            for i in range(c):
                if i % 2 == 0:
                    print("Even index process")
                    temp_x = a * b + i
                    res_val = temp_x / 2
                else:
                    print("Odd index process")
                    temp_x = a * b + i
                    res_val = temp_x / 2
        else:
            for i in range(c):
                if i % 2 == 0:
                    print("Even index process")
                    temp_y = a * b - i
                    res_val = temp_y / 2
                else:
                    print("Odd index process")
                    temp_y = a * b - i
                    res_val = temp_y / 2
    return res_val
