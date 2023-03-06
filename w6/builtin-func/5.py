#Write a Python program with builtin function that returns True if all elements of the tuple are true.
"""
x = ()

y = list(x)

n = int(input())

for i in range(n):
    i = input()
    y.append(i)

x = tuple(y)

a = all(x)

print(a)

"""
x = (True, False, True)
a = all(x)
print(a)