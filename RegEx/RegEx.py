#! /usr/bin/env python3

import re

#regex are great for specifying text patterns

def isPhone(text):
  if len(text) != 12:
    return False # not phone number siced

message = "My number 571-867-5309,b ut my hope is for 540-882-9705"

#this will have to be a raw string as regex includes a lot of backslashes
#it's instructions to look for the pattern \d as digit and \d- as the digit and dash between the numbers
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumRegex.search(message) #invokes search method on the matchObject and reutns the first one
print(matchObject.group()) #.group() returns the result of the search

matchObjectTwo = phoneNumRegex.findall(message) #returns all instances of the search as a list
print(matchObjectTwo) #no need to group

#Regex groups and the Pipe Character

#if we wanted a specific part of the phone number we could use groups
#grousp use parentheses

phoneNumRegexTwo = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#separates the results into groups, area code and the rest of the num
#if the number used and parentheses two separate the
mo = phoneNumRegexTwo.search(message)
print(mo.group(1)) #prints the first group, the area code
print(mo.group(2)) #prints the las part

phoneNumRegexTwo = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d') #using esacpe characters to find phone numbers as (540) 704-3309


batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #use pipe to find string that match batmobile/batcopter/batman etc
mo = batRegex.search("Batman caught joker with the Batmobile")
print(mo.group())

#Repetition in regex Patterns | greedy/Nongreedy matching

#the ? indicates that (wo) can exist in the search 0 or 1 times
#searches for Batman or Batwoman
# a star * means it could except 0 or more so Batwowowowowoman would work
# + means atleast 1 time so Batman would not work
#you can escape patterns (\) to escape *, ?, or +
batRegex = re.compile(r'Bat(wo) ?man')

mo = batRegex.search("Batman")
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d-) ?\d\d\d-\d\d\d\d') #to make area codes optional

haReg = (r'(Ha) {3}') #searched for HaHaHa
haReg = (r'(Ha) {3,7}') #search for 3-7 Ha's
haReg = (r'(Ha) {3,}') #search for at least 3 Ha's

digitReg = re.compile(r'(\d) {3,7}') #search for digits w/ len 3 - 7
digitReg.searcch('123456789') #will return through 7 as regex is greedy
digitReg = re.compile(r'(\d) {3,7}?') #adding ? make it non greedy to return through3

#Regex Character Classes and the Findall Mehod
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall() #returns list of strings that match the pattern
#if the regex has more than one group it will return tuples of results (tuples can have more than two items inside)


xmas = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids Milking. 7 Swans Swimming, 6 Geese Laying, 5 golden rings, 4 turtle doves, 3 french hens, 2 turtle doves, 1 Partridge in Pear tree"

xmasReg= re.compile(r'\d+\s\w+') #looking for atleast 1 digit then a space and then atleast one character

#make you own character class []
vowelRx = re.compile(r'[aeiou]') #which is the same as (a|e|i|o|u)
doubleVowelRx = re.compile(r'[aeiou]{2}') #looking for atleset two vals next to each other oo ae etc
negativevowelRx = re.compile(r'^[aeiou]') #everything but vowels including punctuation and white space
rangeRx = re.compile(r'[a-zA-F]') #all lowercase letters but Uppercase A-F

#Regex Dot-Star and the Caeret/Dallar Chars

beginsWithRx = re.compile(r'^Hello') #has to be at the very beginning of the string
endsWithRx = re.compile(r'world!$') #has to be at the very end

  #wildcard dot .

atRegex =re.compile(r'.at')
atRegex.findall("The fat cat sat around the flat") #  should return all words with single char in front of at

  #.* any character accept for new line
nameRx = re.compile(r'First Name: (.*) Last Name: (.*)') #return zero or more of whatever character exists here
nameRx.findall('First Name: Will Last Name: Smith') #return a tuple [(Will, Smith)]

#.* is greedy, you would have to use .*? for non greedy

dootStarAll = re.compile('.*', re.DOTALL) #to inclide line breaks
vowelRx = re.compile(r'[aeiou]', re.I) #to ignore case and match lower & upper case

#Regex sub() Method and Verbose Mode
#you can use regex to find/replace

codeNameRx = re.compile(r'Agent \w+')
codeNameRx.findall('Agent Bourne handed off the file to Agent Bond') # return [Agent Bourne, Agent Bond]
codeNameRx.sub('REDACTED', 'Agent Bourne handed off the file to Agent Bond')
#returns 'REDACTED handed off the file to REDACTED'
codeNameRx = re.compile(r'Agent (\w)\w*') #return first letter of each agent
codeNameRx.sub('Agent \1****', 'Agent Bourne handed off the file to Agent Sandiego') #replace agent name with Agent 1st letter group (\1)
#returns 'Agent B**** handed off the file to Agent S****'

#Verbose Mode - allows us to use white space/ line breaks in our regex
newVariable = re.compile(r'''
\d\d\d  #I can even put in comments
-
\d\d\d
-
\d\d\d\d
  ''', re.VERBOSE) # I can also pss multiple params as the second -> re.VERBOSE | re.DOTALL | re.IGNORECASE
