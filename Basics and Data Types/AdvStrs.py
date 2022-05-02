import pyperclip
#usings apostrphes

#i you use single quotes and apostrpehs python throws and error
#str = 'It's the best day ever'
#^sad python noises, however double qoutes lets you

myStr = "It's the best day ever" #pyth dgaf about that apostrophe

#you can use and escape character to allow thing \' (apostrophe) \" (double quote) \t (tab) \n (newline) \\(backslash)

sndStr = 'It\'s the \"best\" day\\week \n \t ever'
print(sndStr)


#raw string: if you have a string that has many newlines or escape characters

rawStr = r'It\'s the \"best\" day\\week \n \t ever'

#Triple quotes are away to print everything in the string treating all characters are part of the string

romeoyJulieta = """insert entire play here"""

#list methods slice, in, and not in are viable

#string methods
#.upper, .lower, title -> sanitizes whole string to upper/lower
#islower & .isupper boolean check if the whole string is upper or lower

#isalpha - letters only
#isalnum - letters and numbers only
#isdecimal - numbers only
#isspace - whitespace only
#is title - titlecase only

#startswith("string") & enswith(string) returns bool

# 'str'.join(list) joins strings with sepereator on front

pets = ['cat', 'dog', 'bird', 'rat']

print(', '.join(pets))

#split returns a list of the "words" in the strings seperated by whitespace or a defined separator
print(myStr.split())
print(myStr.split('t'))

#ljust(amount of padding, character to pad with) and rjust(amount of padding, character to pad with) can add padding to a string .Center works the same
#rstrip(), lstrip(), strip() undoes the above or you can provide characters to remoce

#replace(target, string to replace wiht)

#STRING INTERPOLATION

print('You can put variables with an %s and where there is a %s the varible you define on the other side of %s will show' % (pets, myStr, sndStr))
