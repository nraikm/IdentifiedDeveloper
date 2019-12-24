import os

directory_name = input("Please enter the directory that contains the files you want to unblock: ")
for path_name in os.listdir(directory_name):
    os.system("xattr -d com.apple.quarantine \"" + str(directory_name + "/" + path_name) + "\"")
