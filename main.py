from CompleteController import *

plane1 = Aircraft(0, 5, 0, 10)
plane2 = Aircraft(5, 5, 5, 10)

complete = CompleteController(plane1, plane2)
while not complete.finalDestinations():
    complete.run()

print('This was a success: ', complete.finalDestinations())
print('This was safe: ', complete.checkSafety())
complete.showPlot()
