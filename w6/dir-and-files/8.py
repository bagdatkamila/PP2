#Write a Python program to delete file by specified path. 
#Before deleting check for access and whether a given path exists or not.

import os

#print('Exist:', os.access("C://Users//admin//OneDrive//Рабочий стол//pp2//w6//dir-and-files//deleted.txt", os.F_OK))

if os.path.exists("deleted.txt"):
  os.remove("deleted.txt")
else:
  print("The file does not exist")