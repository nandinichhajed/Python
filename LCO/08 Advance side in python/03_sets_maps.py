superhero = (1, 2, 3, 4)

print(superhero)

def getSquare(num):
    return num * num

result = map(getSquare, superhero)

resultTwo = set(result)

print(resultTwo)