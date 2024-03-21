import os
import shutil

path = "test.txt"

try:
    os.remove(path)
    #os.rmdir(path)   # to delete empty folder
    #shutil.rmtree(path) # delete folder and it's files
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You do not have permission to delete")
except OSError:
    print("You can't remove this using that function")
else:
    print(path+" was deleted")