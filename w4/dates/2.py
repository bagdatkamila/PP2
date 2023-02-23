"""
Write a Python program to print yesterday, today, tomorrow.
"""
from datetime import *

yest = date.today() - timedelta(days = 1)
today = date.today()
tmr = date.today() + timedelta(days = 1)

print(yest, today, tmr)