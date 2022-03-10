pets = ['cat', 'dog', 'bird', 'rat']

#slice is up to but does not include las index

print(pets[1:3])

#however with a slice you can change multiple values of a list

pets[1:3] = ['lion', 'tiger', 'bear']

print(pets)
print(pets[:2]) #prints up to bu no including 2nd index
print(pets[1:]) #prints everything starting from the first index

del pets[4] #unassigns value from the list
print(pets)
print(len(pets)) # length of pets

#you can also just add or multiply arrays
print(pets * 2)
#or add/concat lists
owners =['john', 'katy', 'james']
print(pets + owners) # ['cat', 'lion', 'tiger', 'bear', 'john', 'katy', 'james']

#you can use list() to force values into list
print(list('John')) #['J', 'o', 'h', 'n']

# you can use in and not to see if a value is in a list
print('tiger' in pets) #true
print("John" in pets) #false
print('tiger' not in pets) #false

#loops, multiple assignment, and augmented operator

#note a range is different thna a list rang(4) is a list like array of ints
list(range(0, 100, 2)) # a list starting at zero upto but not including 100 counting by two
for i in range(len(pets)):
  print('index ' + str(i) + ' in pets is: ' + pets[i])

cat = ['fat', 'orange', 'grumpy']
size = cat[0] #single assignment
size, color, disposition = cat #multiple addignment, abit like destructuring objects
size, color, disposition = 'skinny', 'balck', 'grumpy' # ican create/ assing multiple vals at once

#additional you can swap vals pretty easily
a ='AAA'
b = "BBB"
a, b = b, a #you can swap the vals of those vars

#augments operators
count = 1
count = count + 1 #valid syntax
count += 1 # also valid -> -= or *= or /= or %=

#List Methods - index, append, insert, remove, sort

print(pets.index('lion')) #prints firts index of 'lion' or exception
pets.append('dragon') #adds to the end of an array
print(pets)
pets.insert(0, 'algernon')
print(pets)
#both append and insert return "none" values print(pets.append('dragon')) returns none
pets.remove('dragon') #rmoves this the first instance of this val no matter where it is in the list

#sort works on strings and ints alphabeticallly & numerically ***Uppercase letters always come first

pets.sort()
print(pets) # ['algernon', 'bear', 'cat', 'lion', 'tiger']

pets.sort(reverse=True)
print(pets) # ['tiger', 'lion', 'cat', 'bear', 'algernon']

# ***Uppercase letters always come first
pets.sort(key=str.lower) #applies the string method to every key while sorting to compensate for asci alphabetization
