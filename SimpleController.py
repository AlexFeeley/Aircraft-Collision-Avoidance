# Alex Feeley
# December 4, 2020
# This class creates a simple controller which navigates an aircraft from
# its original location to its final destination.

from Aircraft import *
from Graph import *

class SimpleController:
    def __init__(self, plane):
        self.plane = Aircraft(plane.getXPos(), plane.getYPos(), plane.getXFinal(), plane.getYFinal())
        self.graph = Graph(plane) # Empty graph

    def run(self):
        # Move until x = xf
        if self.plane.xDistance() != 0:
            self.setX()
            self.plane.advance()
        # Move until y = yf
        elif self.plane.yDistance() != 0:
            self.setY()
            self.plane.advance()
        self.graph.addPoint(self.plane.getXPos(), self.plane.getYPos())

    # Set x-direction of plane
    def setX(self):
        if self.plane.getXFinal() - self.plane.getXPos() > 0:
            self.plane.setAngle(0)
        elif self.plane.getXFinal() - self.plane.getXPos() < 0:
            self.plane.setAngle(180)

    # Set y-direction of plane
    def setY(self):
        if self.plane.getYFinal() - self.plane.getYPos() > 0:
            self.plane.setAngle(90)
        elif self.plane.getYFinal() - self.plane.getYPos() < 0:
            self.plane.setAngle(270)

    # Return true if plane has reached destination
    def success(self):
        return self.plane.xDistance() == 0 and self.plane.yDistance() == 0

    # Show plot of run
    def showPlot(self):
        self.graph.createSimplePlot()
