import random

numberOfStreaks = 0


for experimentNumber in range(10000):
    z = []
    for dsaf in range(100):

        x = random.randint(0,1)
        z.append(x)

    for i in range(100):
        if z[i] == z[i+1]:
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))