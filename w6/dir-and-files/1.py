#Write a Python program to list only directories, files and all directories, files in a specified path.

# import OS module
import os
 
# Get the list of all files and directories
path = "C://Users//admin//OneDrive//Рабочий стол//work"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

