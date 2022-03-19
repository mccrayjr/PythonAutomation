#! /usr/bin/env python3

#import shell utills copy or move files
import shutil
#import os to delete files
import os
import send2trash

#rememb to use escape characters or raw strings when denoting paths
shutil.copy('absolute path of file', 'directory of where it needs to go\\second param to rename.txt')
shutil.copytree('abs. path of folder you\'d like to copy', 'name of what to call new copy')

shutil.move('abs. path of file you\'d like to copy', 'abs. path of where you want it moved')

#there is no 'rename' function so you have to use .move() name what you want to move it to
shutil.move('abs. path of file you\'d like to copy', 'abs. path of where you want it moved\\newName.file')

#to 'delete' a file use
os.unlink('file') #however check which one your deleting by using
os.getcwd()

#to delete a foler
#~~~~~~~*******-----IMPORTANT-----*******~~~~~~~
# these methods permanently delet files. Give them a dry run using print() before using them
os.rmdir('path\to\folder') #however folder has to be empty

shutil.rmtree('path\to\folder') #will delete everything inside of the folder


#ALTERNATIVELY use pip to install the send2trash to send to trash instead of permanently deleting
send2trash.send2trash('path\to\folder')
