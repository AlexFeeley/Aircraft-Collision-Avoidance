

class SafetyMonitor:
    def __init__(self):
        # True if danger zone ever encountered or planes crash
        self.danger = False

    def error(self, plane1, plane2):
        # Current position of planes puts them in each others danger zones
        if plane1.getXPos() - plane2.getXPos() < 0.5 and plane1.getYPos - plane2.getYPos() < 0.5:
            self.danger = True
        # Next position of planes puts them in each others danger zones
        elif plane1.nextX() - plane2.nextX() < 0.5 and plane1.nextY() - plane2.nextY() < 0.5:
            self.danger = True
        # Planes collide in the x-direction
        elif plane1.getYPos() == plane2.getYPos() and plane1.getXPos() == plane2.nextX() and \
                plane1.nextX() == plane2.getXPos():
            self.danger = True
        # Planes collide in the y-direction
        elif plane1.getXPos() == plane2.getXPos() and plane1.getYPos() == plane2.nextY() and \
                plane1.nextY() == plane2.getYPos():
            self.danger = True

        return self.danger

    def safety(self):
        if self.danger:
            print("The aircraft either collided or came into the other's danger zone.")
        else:
            print("The aircraft never collided or came into the other's danger zone. ")