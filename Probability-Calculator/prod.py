listOfBalls = ("black=2", "red=1", "green=3")

newList = []
counter = 0
for ball in listOfBalls:
    ballColor = listOfBalls[counter].split('=')[0]
    ballCount = int(listOfBalls[counter].split('=')[1])
    while ballCount > 0:
        newList.append(ballColor)
        ballCount = ballCount - 1
    counter = counter + 1
        
print(newList)
print('test: "black", "black", "red", "green", "green", "green"') 