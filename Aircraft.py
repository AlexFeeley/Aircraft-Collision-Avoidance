# Alex Feeley
# December 3, 2020
# This class creates an aircraft that moves exactly 1 km / minute and may only move in
# the directions north, east, south, and west.
class Aircraft:
    def __init__(self, x = 0, y = 0, xFinal = 0, yFinal = 0):
        # Initial Position
        self.xPos = x
        self.yPos = y

        # 0 = North (up), 1 = East (right), 2 = South (down), 3 = West (left)
        self.direction = 0

        # Final Position
        self.xF = xFinal
        self.yF = yFinal

    # Set direction of aircraft
    def setDirection(self, direction):
        if not 0 <= direction <= 3:
            raise IndexError('Direction must be between 0 and 3.')
        elif abs(self.direction - direction) == 2:
            raise Exception('Aircraft can not turn around.')
        self.direction = direction

    # Get current direction of aircraft
    def getDirection(self):
        return self.direction

    # Get current x-position of aircraft
    def getXPos(self):
        return self.xPos

    # Get current y-position of aircraft
    def getYPos(self):
        return self.yPos

    # Advance aircraft one step in current direction
    def advance(self):
        if self.direction == 0:
            self.yPos += 1
        elif self.direction == 2:
            self.yPos -= 1
        elif self.direction == 1:
            self.xPos += 1
        else:
            self.xPos -= 1

    # Returns true if destination has been reached
    def destination(self):
        return self.xPos == self.xF and self.yPos == self.yF

    # Returns true if position is in danger zone of aircraft
    def danger(self, x, y):
        return abs(self.xPos - x) < 1 and abs(self.yPos - y) < 1

    # Returns true if position is in communication zone of aircraft
    def communication(self, x, y):
        return abs(self.xPos - x) < 2 and abs(self.yPos - y) < 2

    # Returns an (x, y) representation of the plane
    def __repr__(self):
        return "(" + self.xPos + ", " + self.yPos + ")"
