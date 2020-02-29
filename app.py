import random
x = random.randint(1, 20)
print(x)
while True:
  guess = input('what is the number\n')
  if int(guess) == x:
    print('you guessed successfully, your number is', guess,'and the random number is', x)
    break
  elif int(guess) > x:(
    print('your number is greater try again')
  elif int(guess) < x:
    print('your number is lower try again')