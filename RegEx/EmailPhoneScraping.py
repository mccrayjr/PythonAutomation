#! /usr/bin/env python3

import pyperclip
import re

#TODO: Create regex obj for phone numbers

phoneRx = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext. 12345, x12345

  (((\d\d\d) | (\(\d\d\d\)))? #area code (optional) is either 3 digits or 3 digits inside parentheses.
  (\s|-)            #first separator
  \d\d\d            #first 3 digits
  -                 #separator
  \d\d\d\d          #last 4 digits
  (((ext(\.)?\s) | x)#extension (optional)
  (\d{2,5})) ?  )     #numbers after extension and the whole group (extendsion and numbers are wrapped in parens to make optional)
''', re.VERBOSE)

#TODO: Create regex obj for emails
emailRx = re.compile(r'''
[a-zA-Z0-9_.+]+ #name part, created a custom character class of all of the characters that can be used in an email
@               #@ symbaol
[a-zA-Z0-9_.+]+ #domain name part
''', re.VERBOSE)
#TODO: get text off clipboard
text = pyperclip.paste()
#TODO: extract email/phone from text
extractedPhone = phoneRx.findall(text) #returns tuple of all groups so we have to wrap the whole regex as a group
extractedEmail = emailRx.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
  allPhoneNumbers.append(phoneNumber[0])

#print(allPhoneNumbers)
#print(extractedEmail)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail) # take the elems from each array and join them on a line break
print(results)
pyperclip.copy(results)


