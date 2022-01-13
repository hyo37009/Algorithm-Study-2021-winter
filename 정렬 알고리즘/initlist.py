import random

def listinitiation():
    n = random.randrange(5, 15)
    x = []
    for i in range(n):
        x.append(random.randrange(1, 25))

    return x