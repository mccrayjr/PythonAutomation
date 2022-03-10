#! /usr/bin/python3

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


xmas = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids Milking. 7 Swans Swimming, 6 Geese Laying, 5 golden rings, 4 turtle doves, 3 french hens, 2 turtle doves, 1 Partridge in Pear tree "
