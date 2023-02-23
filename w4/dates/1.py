"""
Write a Python program to subtract five days from current date.
"""

import datetime

FiveDays = datetime.date.today() - datetime.timedelta(days = 5)
print(FiveDays)