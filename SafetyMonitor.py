# Alex Feeley
# December 6, 2020
# This class aims to monitor the safety of the complete controller by ensuring that
# two aircraft never collide and that the aircraft never enter each other's danger
# zones.


class SafetyMonitor:
    def __init__(self):
        # True if danger zone ever encountered or planes crash
        self.danger = False

    # Enters danger state if planes enter danger zone or crash
    def error(self, plane1, plane2):
        # Current position of planes puts them in each others danger zones
        if abs(plane1.getXPos() - plane2.getXPos()) < 0.5 and abs(plane1.getYPos() - plane2.getYPos()) < 0.5:
            self.danger = True
        # Check if plane's positions overlapped in x-direction (aka they crashed!)
        elif plane1.getXPos() == plane2.xLast and plane1.getYPos() == plane2.getYPos() and \
                plane1.xLast == plane2.getXPos():
            self.danger = True
        # Check if plane's positions overlapped in y-direction (aka they crashed!)
        elif plane1.getYPos() == plane2.yLast and plane1.yLast == plane2.getYPos() and \
                plane1.getXPos() == plane2.getXPos():
            self.danger = True

        return self.danger

    # The controller is safe if danger == False
    def safety(self):
        return not self.danger
