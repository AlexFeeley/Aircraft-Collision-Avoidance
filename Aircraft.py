# Alex Feeley
# December 3, 2020
# This class creates an aircraft that moves exactly 1 km / minute and may only move in
# the directions north, east, south, and west.

import math

class Aircraft:
    VELOCITY = 1 # Velocity is constant at 1km/min

    def __init__(self, x = 0, y = 0, xFinal = 0, yFinal = 0):
        # Initial Position
        self.xPos = x
        self.yPos = y

        # Right (0), Up (90), Left (180), Down (270)
        self.angle = None

        # Final Position
        self.xF = xFinal
        self.yF = yFinal

    # Set direction of aircraft
    def setAngle(self, angle):
        if not (angle == 0 or angle == 90 or angle == 180 or angle == 270):
            raise IndexError('Direction must be between 0 and 3.')
        elif self.angle is not None and abs(self.angle - angle) == 180:
            raise Exception('Aircraft can not turn around.')
        self.angle = angle

    # Get current angle of movement for the aircraft
    def getDirection(self):
        return self.angle

    # Get current x-position of aircraft
    def getXPos(self):
        return self.xPos

    # Get current y-position of aircraft
    def getYPos(self):
        return self.yPos

    # Final x-position of aircraft
    def getXFinal(self):
        return self.xF

    # Final y-position of aircraft
    def getYFinal(self):
        return self.yF

    # Distance between current and final x-positions
    def xDistance(self):
        return abs(self.xPos - self.xF)

    # Distance between current and final y-positions
    def yDistance(self):
        return abs(self.yPos - self.yF)

    # Total distance left to destination
    def distance(self):
        return self.xDistance() + self.yDistance()

    # Advance aircraft one step in current direction
    def advance(self):
        self.xPos += (self.VELOCITY * math.cos(math.radians(self.angle)))
        self.yPos += (self.VELOCITY * math.sin(math.radians(self.angle)))

    # Returns an (x, y) representation of the plane
    def __repr__(self):
        return "(" + str(self.xPos) + ", " + str(self.yPos) + ")"
