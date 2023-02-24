"""
Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

"""

def evens():
    n = int(input())
    ev = (int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(ev), end = ", ")
    print(next(ev))

evens()