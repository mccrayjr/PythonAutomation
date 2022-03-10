import random

print('hey there, what\'s your name?')
name = input()

print('Well,' + name + ', I am thinking of a number between 1 and 20')
secretNum = random.randint(1, 20)

for guesses in range (1, 7):
  print("Take a guess!")
  guess = int(input())

  if guess < secretNum:
    print("Your guess is too low")
  elif guess > secretNum:
    print("Your guess is too high")
  else:
    break # this is for correct guesses

if guess == secretNum:
  print('Nice work, ' + name + "! You guessed my number in " + str(guesses) + "!")
else:
  print('Sorry, ' + name + ' the number I was thinking of was ' + str(secretNum))

