#! /usr/bin/env python3


#this is basically how to 'throw' an error is JS
#raise Exception("Error Message here")

def boxPrint(symbol, width, height):
  if len(symbol) != 1:
    raise Exception('"symbol" needs to be astring lenght of 1.')

  print(symbol * width)

  for i in range(height- 2):
    print(symbol + (' ' * (width - 2)) + symbol)
  print(symbol * width)

boxPrint('x', 15, 5)
