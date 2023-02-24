"""Implement a generator that returns all numbers from (n) down to 0."""

def fromnto0():
    n = int(input())
    decr = (int(i) for i in range (n, 0, -1))
    for i in range(n):
        print(next(decr))
fromnto0()