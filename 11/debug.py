import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)
if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guesss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')