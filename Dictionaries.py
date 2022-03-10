# Dictionaries (basically object)

cat = {'size' : "large", 'colour': 'black', 'dispo': 'honourable'}


#check to see if keys exist using in/not in

print(list(cat.keys())) #cat.keys itself returns an array like obj (list like obj)
for k in cat.keys():
  print(k)

print(list(cat.values()))
for k in cat.values():
  print(k)

print(list(cat.items()))#returns a list of touples that can be accessed through nmultiple assignment
for k, v in cat.items():
  print(k, v)

#get method so it doesn't matter if it does not exist
cat.get("age", 0) #will return zero

#cat['age'] #will throw an error

#setDefault - if there is not value on the key, set the value if so keep OG value
cat.setdefault('colour', 'grey') # because colour is already set to black nothing will happen

message = "On a dark desert highway, cool wind in my hair"

count = {}

for char in message.upper():
  count.setdefault(char, 0)
  count[char] = count[char] + 1
print(count)

#type() returns the type passed through the function
