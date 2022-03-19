#! /usr/bin/env python3

import os

#this function giveus acces to all of the files inside of a root folder
#it can be used in for loops to access all of the dirs in a root dir
#os.walk("root folder")

# FolderName = string name of the folder it's loooking at in this iteration
#subfolders = a list of allthe folders in that foler
# filenames = list of all the files in a folder
for folderName, subfolders, filenames in os.walk('/Users/johnmccray/other/PythonStuff'):
  print('the folder is ' + folderName)
  print('the subfolders in ' + folderName + ' are' + str(subfolders))
  print('the filenames in ' + folderName + ' are' + str(filenames))
  print()
