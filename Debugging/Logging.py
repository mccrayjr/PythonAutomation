#! /usr/bin/env python3

import logging
#set of code for logging in python
logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
#you can also log to a file by passing a filename param
#logging.basicConfig(filename='myLogdile.txt', level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)#Turns off logging for the propram at the critical level or lower (debug, info, warning, error, critical)



def factorial(n):
  logging.debug('Starting factorial %s' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i issi %s, total is %s' % (i, total))
  logging.debug('Return value is %s' % (total))
  return total

factorial(5)
