from SimpleController import *

startX = -7
startY = -8
endX = -3
endY = -4
plane = Aircraft(startX, startY, endX, endY)

simple = SimpleController(plane)
while not simple.success():
    simple.run()
print('This was a success: ', simple.success())
