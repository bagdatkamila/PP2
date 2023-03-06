#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

s = list(input())

s1 = list(reversed(s))

if s == s1:
    print("It is palindrom")
else:
    print("It is not palindrom")

