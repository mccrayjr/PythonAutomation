#! /usr/bin/env python3
import pyautogui

#we need to let our program "see", refer to chapter 17 of the book for more info

pyautogui.screenshot('path/to/save/document.png') #returns a pillow image object
#to do image resognition we can crop an image of a button or something we want to click on or otherwise manipulate and find it w/ vvvv
pyautogui.locateOnScreen('filename.png')#returns x/y coords of that image and widht/height of region
pyautogui.locateCenterOnScreen('filename.png') #returns the center
#we could then pass info to to .click

#Note: the location function is computationally expenisve (up to a second), and also needs to be a pixel perfect match, refer to docs on how to optimize or find close/closest match

#view a sample of automating gameplay with gui here https://github.com/asweigart/sushigoroundbot
