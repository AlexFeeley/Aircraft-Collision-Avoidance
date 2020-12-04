from Aircraft import *

startX = 3
startY = 4
endX = 7
endY = 8
plane = Aircraft(startX, startY, endX, endY)

plane.setDirection(1)

while plane.xPos != endX:
    plane.advance()

plane.setDirection(0)

while plane.yPos != endY:
    plane.advance()

print('The plane has successfully reached its destination: ', plane.destination())