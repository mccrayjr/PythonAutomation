def dum(dideby):
  try:
    return 42 / dideby
  except ZeroDivisionError:
    print("you tried to deivide by zero")

print(dum(84))
print(dum(0))
