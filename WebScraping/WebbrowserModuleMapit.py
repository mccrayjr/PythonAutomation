#! /usr/bin/env python3

#opens a new browsers to specific url
import webbrowser, sys, pyperclip
#webbrowser.open(https://automatetheboringstuff.com)

sys.argv #checkingfor command line args

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])#slice to the end of the arr
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/
webbrowser.open('https://www.google.com/maps/place/'+ address)
