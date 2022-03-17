#! /usr/bin/env python3
import shelve # -a special tool we'll need later ;)

#three things

practiceFile = open('/Users/johnmccray/Notes/Practice.txt') #save as afile object

practiceFile.read() #reads the content of the txt file
practiceFile.close() #closes the file

practiceFile = open('/Users/johnmccray/Notes/Practice.txt') #after closing the file you have to open it again in order to read it
content = practiceFile.read() #so we're just going to store the contents in a variable
practiceFile.close()

practiceFile = open('/Users/johnmccray/Notes/Practice.txt')
linesofContent = practiceFile.readlines()
practiceFile.close()
print(content)
print(linesofContent)

#write ('w')lets you overwrite whats in an existing file, while append ('a') letts you add on that file
practiceFile = open('/Users/johnmccray/Notes/Practice2.txt', 'w') #if this file does not exist it will create it
practiceFile.write('Woah buddy we\'re writing in a new file!') #it'll add text (overwrite), but we would have to manually add line breaks \n
practiceFile.write(' So much writing, its pretty great') #We can keep writing as lonmg as we don't close the file

#Shelves - let you pass on variables and information to other files


