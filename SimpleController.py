# Alex Feeley
# December 4, 2020
# This class creates a simple controller which navigates an aircraft from
# its original location to its final destination.

from Aircraft import *

class SimpleController:
    def __init__(self, plane):
        self.plane = Aircraft(plane.getXPos(), plane.getYPos(), plane.getXFinal(), plane.getYFinal())

    def run(self, output = False):
        if self.plane.getXFinal() - self.plane.getXPos() > 0:
            self.plane.setAngle(0)
        elif self.plane.getXFinal() - self.plane.getXPos() < 0:
            self.plane.setAngle(180)

        while not self.plane.xDestination():
            self.plane.advance()

        if self.plane.getYFinal() - self.plane.getYPos() > 0:
            self.plane.setAngle(90)
        elif self.plane.getXFinal() - self.plane.getYFinal() < 0:
            self.plane.setAngle(270)

        while not self.plane.yDestination():
            self.plane.advance()

    def success(self):
        return self.plane.xDestination() and self.plane.yDestination()