# Alex Feeley
# December 6, 2020
# This class creates a plot and adds points to it as aircraft
# complete their run using the simple or complete controller.

import matplotlib.pyplot as plt


class Graph:
    def __init__(self, plane1, plane2=None):
        # Plane1 positions
        self.x1 = [plane1.getXPos()]
        self.y1 = [plane1.getYPos()]

        # Plane2 positions
        if plane2 is not None:
            self.x2 = [plane2.getXPos()]
            self.y2 = [plane2.getYPos()]

    def addPoint(self, x, y):
        self.x1.append(x)
        self.y1.append(y)

    def addPoints(self, x1, y1, x2, y2):
        self.x1.append(x1)
        self.y1.append(y1)

        self.x2.append(x2)
        self.y2.append(y2)

    def createSimplePlot(self):
        # Create plot and sub-plot
        fig = plt.figure()
        plt.title('Route of Aircraft')

        # Add data to plot
        plt.plot(self.x1, self.y1, c='b', marker='o', label='Plane 1')
        plt.legend(loc='upper left')

        # Show plot
        plt.show()

    def createCompletePlot(self):
        # Create plot and sub-plot
        fig = plt.figure()
        plt.title('Route of Aircraft')

        # Add data to plot
        plt.plot(self.x1, self.y1, c='b', marker='o', label='Plane 1')
        plt.plot(self.x2, self.y2, c='r', marker='s', label='Plane 2')
        plt.legend(loc='upper left')

        # Show plot
        plt.show()