import random

life = 500
score = -1

while life>0:
    print('__________')
    print('your score is ' + str(life))
    score+=1
    print('opur score so far: ' + str(score))

    ascii = random.randint(32, 126)
    charachter = chr(ascii)

    guess = int(input('What is ASCII code for this charchter: ' + charachter))


if guess == ascii:
    print('Correct! Your life score is back at 500.')
    life = 500
else:
    print('Incorrect. The answer was ' + str(ascii))
    difference = abs(guess-ascii)
    print('you lose' + 'life points.')
    life = life - difference

print('Game Over')
print('your score:' + str(score))
