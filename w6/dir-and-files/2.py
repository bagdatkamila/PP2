#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path

import os

print('Exist:', os.access('C://Users//admin//OneDrive//Рабочий стол//work', os.F_OK))
print('Readable:', os.access('C://Users//admin//OneDrive//Рабочий стол//work', os.R_OK))
print('Writable:', os.access('C://Users//admin//OneDrive//Рабочий стол//work', os.W_OK))
print('Executable:', os.access('C://Users//admin//OneDrive//Рабочий стол//work', os.X_OK))