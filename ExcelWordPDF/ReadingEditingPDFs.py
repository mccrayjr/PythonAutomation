#! /usr/bin/env python3
import PyPDF2 #PDF's are tough to read but this one has been the best - Text Only
import os

os.chdir('path/to/file')
pdfFile = open('example.pdf', 'rb') #needs to be in read binary
reader = PyPDF2.PdfFileReader(pdfFile)
page = reader.getPage(0)
page.extractText()

for pageNum in range (reader.numPages):
  print(reader.getPage(pageNum).extractText) #get all of the text from every page
