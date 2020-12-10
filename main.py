from CompleteController import *

startX = 0
startY = 5
endX = -4
endY = 0
plane1 = Aircraft(startX, startY, endX, endY)
plane2 = Aircraft(0, 1, 3, 3)

complete = CompleteController(plane1, plane2)
while not complete.finalDestinations():
    complete.run()

print('This was a success: ', complete.finalDestinations())
complete.showPlot()
