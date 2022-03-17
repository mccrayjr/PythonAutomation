#! /usr/bin/env python3


#mac vs pc use different file structure notation convention c:/user/path/to/file while mac user\user\path\to file
#in order to comply with naming convention in our code we can use a library to determine which os were writing for
import os

os.path.join('folder', 'folder1', 'folder3', 'pic.png')

os.getcwd() #pwd
os.chdir    #cd

os.path.abspath('file') #returns absolsulte file path
os.path.isabs('/Users/johnmccray/other/PythonStuff') #returns boolean on if the pathis an absolute path
os.path.relpath('/Users/johnmccray/other/PythonStuff', '/Users/johnmccray/other/FreeNDee') #return relative path from first parram to second
os.path.dirname('/Users/johnmccray/other/PythonStuff\\Files.py') #returns directors of the path to a file (abspath)
os.path.basename('/Users/johnmccray/other/PythonStuff\\Files.py') #returns the name of the file of the  end of the path (file.text)

os.path.exists('/Users/johnmccray/other/PythonStuff')#returns a boolean if a directory exists
os.path.isfile('/Users/johnmccray/other/PythonStuff\\Files.py') #returns a bool if file exists
os.path.getsize('/Users/johnmccray/other/PythonStuff\\Files.py') #return file size

os.listdir('/Users/johnmccray/other/PythonStuff')#ls - list all files in a directory

#func to get all of the file sizes in a directory

def dirSizer(file):
  totalSize = 0

  for filename in os.listdir('/Users/johnmccray/other/PythonStuff'):
    #handling to check if it's a file or directory
    if not os.path.isfile(os.path.join('/Users/johnmccray/other/PythonStuff', filename)):
      continue
    totalsize += os.path.getsize(os.path.join('/Users/johnmccray/other/PythonStuff', filename))

  return totalSize


os.makedirs('/Users/johnmccray/anotherdir/create/multiple/at/once')
