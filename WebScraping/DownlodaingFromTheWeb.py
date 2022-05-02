#! /usr/bin/env python3
import requests # allows you to downlod files from an adress

res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # download romeo and juliet from the web

#res = the response object from the requested address

res.status_code #should be 200 if everything wen ok
res.raise_for_status() #raises an expection if we got a bad download
playFile = open("RomeoYJuliet.txt",'wb') #we need to open it in "write-binary" to maintain unicode enocding of the text

for chunk in res.iter_content(100000): # we can download by chunks (breaking up the download) in the response object
  playFile.write(chunk) #returns the number of byte written

playFile.close()
#requests may not be best if you need to login/access the download selenium or beautiful soup may be more appropriate

