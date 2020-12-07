# Alex Feeley
# December 6, 2020
# The complete controller moves two aircraft from their initial positions
# to their final destinations without colliding.

from Aircraft import *
from SafetyMonitor import *
from Graph import *


class CompleteController:
    def __init__(self, plane1, plane2):
        # Two aircraft
        self.plane1 = Aircraft(plane1.getXPos(), plane1.getYPos(), plane1.getXFinal(), plane1.getYFinal())
        self.plane2 = Aircraft(plane2.getXPos(), plane2.getYPos(), plane2.getXFinal(), plane2.getYFinal())

        self.safetyMonitor = SafetyMonitor() # External safety monitor
        self.checkSafety = SafetyMonitor() # Internal monitor for decision making
        self.graph = Graph(plane1, plane2) # Empty graph
        self.switch1 = True # True if moving in x-direction for plane1
        self.switch2 = True # True if moving in y-direction for plane2

    # Main algorithm
    def run(self):
        # Aircraft not in communication zone and not at final destination
        if not self.finalDestinations() and not self.communicationZone():
            self.freeRun()

        # Aircraft in communication zone but not at final destination
        elif not self.finalDestinations():
            # Next 'step' will not cause a collision
            if self.plane1.getDirection() is not None and self.plane2.getDirection() is not None and self.dangerZone():
                self.checkSafety.reset()  # Reset internal safety monitor
                self.changeDirection()  # Change direction as appropiate
            self.freeRun()

        # One plane has reached its destination, the other has not
        else:
            self.freeRun()

    def changeDirection(self):
        if self.switch1 == True and self.switch2 == True: # Both traveling in x-direction
            if self.plane1.yDistance() > self.plane2.yDistance():
                self.switch1 = False
            else:
                self.switch2 = False
        elif self.switch2 == False and self.switch2 == False: # Both traveling in y-direction
            if self.plane1.xDistance() > self.plane2.xDistance():
                self.switch1 = True
            else:
                self.switch2 = True
        elif self.switch1 == True and self.switch2 == False: # Plane1 in x, plane2 in y
            if self.plane1.yDistance() > self.plane2.xDistance():
                self.switch1 = False
            else:
                self.switch2 = True
        elif self.switch1 == False and self.switch2 == True: # Plane1 in y, plane2 in x
            if self.plane1.xDistance() > self.plane2.yDistance():
                self.switch1 = True
            else:
                self.switch2 = False

    # Aircraft are not in communication zone and not at final destination
    def freeRun(self):
        # self.safetyMonitor(self.plane1, self.plane2)
        # Determine next direction
        if self.switch1 and self.plane1.xDistance() != 0:
            self.setX1()
            self.plane1.advance()
            self.switch1 = False
            self.setY1()
        elif self.plane1.yDistance() != 0:
            self.setY1()
            self.plane1.advance()
            self.switch1 = True
            self.setX1()
        if self.switch2 and self.plane2.xDistance() != 0:
            self.setX2()
            self.plane2.advance()
            self.switch2 = False
            self.setY2()
        elif self.plane2.yDistance() != 0:
            self.setY2()
            self.plane2.advance()
            self.switch2 = True
            self.setX2()

        self.graph.addPoints(self.plane1.getXPos(), self.plane1.getYPos(), self.plane2.getXPos(), self.plane2.getYPos())

    # Determines if both planes are at their final destination
    def finalDestinations(self):
        return self.plane1.xDistance() == 0 and self.plane1.yDistance() == 0 and \
            self.plane2.xDistance() == 0 and self.plane2.yDistance() == 0

    # Check if planes are within a 1km square of each other or will collide
    # after 1 minute of moving
    def dangerZone(self):
        return self.checkSafety.error(self.plane1, self.plane2)

    # Check if planes are within a 2km square of each other
    def communicationZone(self):
        return abs(self.plane1.getXPos() - self.plane2.getXPos()) <= 2 and abs(self.plane1.getYPos() - self.plane2.getYPos()) <= 2

    # Set x-direction of plane1
    def setX1(self):
        if self.plane1.getXFinal() - self.plane1.getXPos() > 0:
            self.plane1.setAngle(0)
        elif self.plane1.getXFinal() - self.plane1.getXPos() < 0:
            self.plane1.setAngle(180)

    # Set y-direction of plane1
    def setY1(self):
        if self.plane1.getYFinal() - self.plane1.getYPos() > 0:
            self.plane1.setAngle(90)
        elif self.plane1.getYFinal() - self.plane1.getYPos() < 0:
            self.plane1.setAngle(270)

    # Set x-direction of plane2
    def setX2(self):
        if self.plane2.getXFinal() - self.plane2.getXPos() > 0:
            self.plane2.setAngle(0)
        elif self.plane2.getXFinal() - self.plane2.getXPos() < 0:
            self.plane2.setAngle(180)

    # Set y-direction of plane2
    def setY2(self):
        if self.plane2.getYFinal() - self.plane2.getYPos() > 0:
            self.plane2.setAngle(90)
        elif self.plane2.getYFinal() - self.plane2.getYPos() < 0:
            self.plane2.setAngle(270)

    # Show plot of run
    def showPlot(self):
        self.graph.createCompletePlot()

    def checkSafety(self):
        return self.safetyMonitor.safety()
