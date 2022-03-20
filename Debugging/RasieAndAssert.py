#! /usr/bin/env python3

import traceback

#this is basically how to 'throw' an error is JS
#raise Exception("Error Message here")

def boxPrint(symbol, width, height):
  #gotta fail fast and early!
  if len(symbol) != 1:
    raise Exception('"symbol" needs to be astring lenght of 1.')
  if (width < 2) or (height < 2):
    raise Exception('"height" needs to be astring lenght of 1.')

  print(symbol * width)

  for i in range(height- 2):
    print(symbol + (' ' * (width - 2)) + symbol)
  print(symbol * width)

boxPrint('x', 15, 5)

#We could also write the traceback (callstack) to a file with traceback.format_exc())

errorfile= open('errorFile.txt', 'a')
errorfile.write(traceback.format_exc())
errorfile.close() #this block of code in the catch of try catch would just print the traceback to a file and you could still have the rest of your program run

#Assertions and assert statement - a sanity check to make sure your code isn;t doing something obviously worng
#a conditional that wil throw an exception

market_2nd = {'ns': 'green', 'ew': 'red' }
def changeLight(intersection):
  for key in intersection.keys():
    if intersection[key] == 'green':
      intersection[key] = 'yellow'
    elif intersection[key] == 'yellow':
      intersection[key] = 'red'
    elif intersection[key] == 'red':
      intersection[key] = 'green'

  assert 'red' in stoplight.values(), 'neither light is' + str(intersection)
  #basically we know before writing the func that atleast one should be red at all time so we can trow and exception if it's not

changeLight(market_2nd)
