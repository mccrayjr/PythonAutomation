#! /usr/bin/env python3
import docx

def getText(filename): #return all of the text in a document
  doc = docx.Document(filename)
  fullText = []
  for para in doc.paragraphs:
    fullText.append(para.text)
    '\n'.join(fullText) #form string w/ all of the text from all paragraphs

print(getText('path/to/file.docx'))
