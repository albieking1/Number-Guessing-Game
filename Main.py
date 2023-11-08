import random
n = random.randrange(1,10)
guessednumber = int(input("Guess any number from 1 to 10: "))
while n != guessednumber:
  if guessednumber < n:
    print("Too low!")
    guessednumber = int(input("Guess again: "))
  elif guessednumber > n:
    print("Too high!")
    guessednumber = int(input("Guess again: "))
  else:
    break
print(f'Correct, the answer was {n}!')
