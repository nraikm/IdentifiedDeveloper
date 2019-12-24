import os

path_name = input("Please enter the path of the file you want to unblock: ")

os.system("xattr -d com.apple.quarantine \"" + str(path_name) + "\"")
