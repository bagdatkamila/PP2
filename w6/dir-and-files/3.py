#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os

path = r"C://Users//admin//OneDrive//Рабочий стол//work"

print(os.path.exists(path))
print(os.path.basename(path))
print(os.path.dirname(path))