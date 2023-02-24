"""
Create a generator that generates the squares of numbers up to some number N.
"""

def squares():
    n = int(input())
    sq = (int(i)**2 for i in range(0, n))
    for i in range(n):
        print(next(sq))
        
squares()