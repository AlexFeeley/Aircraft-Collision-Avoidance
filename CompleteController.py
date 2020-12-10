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

        self.last1X = True # Plane1 last moved in the x-direction
        self.last2X = True # Plane2 last moved in the x-direction

    # Main algorithm
    def run(self):
        # Aircraft in communication zone
        if self.communicationZone():
            # Neither plane's final destination is in other's communication zone
            if not self.plane1Check() and not self.plane2Check():
                if self.plane1.xDistance() != 0 and self.plane2.yDistance() != 0:
                    self.setXAngle1()
                    self.setYAngle2()
                elif self.plane1.yDistance() != 0 and self.plane2.xDistance() != 0:
                    self.setYAngle1()
                    self.setXAngle2()
                elif self.plane1.yDistance() != 0 and self.plane2.yDistance() != 0: # Head-on, y-direction
                    self.setXAngle2() # Plane 2 moves out of the way
                elif self.plane1.xDistance() != 0 and self.plane2.xDistance() != 0: # Head on, x-direction
                    self.setYAngle2() # Plane 2 moves out of the way
                self.plane1.advance()
                self.plane2.advance()
            # Plane2's final destination is in plane1's communication zone
            elif not self.plane1Check() and self.plane2Check():
                if self.plane2.angle == 0 or self.plane2.angle == 180: # X-direction
                    self.setYAngle1()
                else: # Y-direction
                    self.setXAngle1()
                self.runPlane2()  # Plane2 continues, plane1 moves
                self.plane1.advance()
            # Plane1's final destination is in plane2's communication zone
            elif self.plane1Check() and not self.plane2Check():
                if self.plane1.angle == 0 or self.plane1.angle == 180: # X-direction
                    self.setYAngle2()
                else: # Y-direction
                    self.setXAngle2()
                self.runPlane1() # Plane1, continues, plane2 moves
                self.plane2.advance()

        # Aircraft cannot communicate, run normally
        else:
            if self.plane1.xDistance() != 0 or self.plane1.yDistance() != 0:
                self.runPlane1()
            if self.plane2.xDistance() != 0 or self.plane2.yDistance() != 0:
                self.runPlane2()
        self.graph.addPoints(self.plane1.getXPos(), self.plane1.getYPos(), self.plane2.getXPos(), self.plane2.getYPos())
        self.showPlot()

    # Set angle in x-direction for plane1
    def setXAngle1(self):
        if self.plane1.getXPos() - self.plane1.getXFinal() > 0 or self.plane1.angle == 180:
            self.plane1.setAngle(180)  # Left
        else:
            self.plane1.setAngle(0)  # Right

    # Sets angle in y-direction for plane1
    def setYAngle1(self):
        if self.plane1.getYPos() - self.plane1.getYFinal() > 0 or self.plane1.angle == 270:
            self.plane1.setAngle(270)  # Down
        else:
            self.plane1.setAngle(90)  # Up

    # Sets angle in x-direction for plane2
    def setXAngle2(self):
        if self.plane2.getXPos() - self.plane2.getXFinal() > 0 or self.plane2.angle == 180:
            self.plane2.setAngle(180)  # Left
        else:
            self.plane2.setAngle(0)  # Right

    # Sets angle in y-direction for plane2
    def setYAngle2(self):
        if self.plane2.getYPos() - self.plane2.getYFinal() > 0 or self.plane2.angle == 270:
            self.plane2.setAngle(270)  # Down
        else:
            self.plane2.setAngle(90)  # Up

    # Runs plane1 normally
    def runPlane1(self):
        if self.plane1.xDistance() != 0:
            self.setXAngle1()
            if not self.last1X or self.plane1.yDistance() == 0:
                self.plane1.advance() # Move in x-direction
                self.last1X = not self.last1X

        if self.plane1.yDistance() != 0:
            self.setYAngle1()
            if self.last1X or self.plane1.xDistance() == 0:
                self.plane1.advance() # Move in y-direction

    # Runs plane2 normally
    def runPlane2(self):
        if self.plane2.xDistance() != 0:
            self.setXAngle2()
            if not self.last2X or self.plane2.yDistance() == 0:
                self.plane2.advance() # Move in x-direction

        if self.plane2.yDistance() != 0:
            self.setYAngle2()
            if self.last2X or self.plane2.xDistance() == 0:
                self.plane2.advance() # Move in y-direction
                self.last2X = not self.last2X

    # Determines if one plane is at its final destination
    def finalDestinations(self):
        return (self.plane1.xDistance() == 0 and self.plane1.yDistance() == 0) and \
               (self.plane2.xDistance() == 0 and self.plane2.yDistance() == 0)

    # Check if planes are within a 2km square of each other
    def communicationZone(self):
        return abs(self.plane1.getXPos() - self.plane2.getXPos()) <= 2 and abs(self.plane1.getYPos() - self.plane2.getYPos()) <= 2

    # Check if plane1's final position is within plane2's communication zone
    def plane1Check(self):
        return abs(self.plane1.getXFinal() - self.plane2.getXPos()) <= 2 and abs(self.plane1.getYFinal() - self.plane2.getYPos()) <= 2

    # Check if plane2's final position is within plane1's communication zone
    def plane2Check(self):
        return abs(self.plane2.getXFinal() - self.plane1.getXPos()) <= 2 and abs(self.plane2.getYFinal() - self.plane1.getYPos()) <= 2

    # Show plot of run
    def showPlot(self):
        self.graph.createCompletePlot()

    # def checkSafety(self):
    #     return self.safetyMonitor.safety()
