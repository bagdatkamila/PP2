"""
Write a Python program to drop microseconds from datetime.
"""

import datetime

today = datetime.datetime.now()
today = str(today)
woutmicro = today.split(".")
print(woutmicro[0])