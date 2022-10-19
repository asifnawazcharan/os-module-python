# list of files inside the current directory and directories inside it

import os

list = os.listdir(".")
print(f"Total files and directories in current directory: {len(list)}")
for i in list:
    if os.path.isdir(i):
        print("")
        print(f"Directory: {i}")
        print("")
        list_individual = os.listdir(path=f"{i}")
        print("Files inside this directory:")
        print(list_individual)
    else:
        print("")
        print(f"File: {i}")
