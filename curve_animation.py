from Tkinter import *
from bcurves import ThreePointCurve, FourPointCurve
import time

class BezierAnimation:
    def __init__(self, canvas, **kwargs):
        self.pointA = kwargs.get('pointA', [0, 50])
        self.pointB = kwargs.get('pointB', [100, 0])
        self.pointC = kwargs.get('pointC', [100, 100])
        self.pointD = kwargs.get('pointD', None)
        
        if self.pointD is not None:
            self.curve = FourPointCurve(
                self.pointA, self.pointB, self.pointC, self.pointD)
        else:
            self.curve = ThreePointCurve(
                self.pointA, self.pointB, self.pointC)

        self.stepsize = 1/float(kwargs.get('steps', 30))
        self.step = 0
        self.canvas = canvas

    def drawcurve(self):
        curve_points = []

        for i in range(self.step+1):
            curve_points.append(self.curve.getcurvepoint(self.stepsize * i))

        for i in range(len(curve_points)-1):
            self.canvas.create_line(
                curve_points[i][0],
                curve_points[i][1],
                curve_points[i+1][0],
                curve_points[i+1][1])

    def drawoutline(self):
        
        self.canvas.create_line(self.pointA[0],
                                self.pointA[1],
                                self.pointB[0],
                                self.pointB[1])

        if self.pointD is None:
            self.canvas.create_line(self.pointB[0],
                                    self.pointB[1],
                                    self.pointC[0],
                                    self.pointC[1])

        else:
            self.canvas.create_line(self.pointC[0],
                                    self.pointC[1],
                                    self.pointD[0],
                                    self.pointD[1])

    def drawedgepoints(self):
        edgepoints = self.curve.getedgepoints(self.step * self.stepsize)

        for point in edgepoints:
            self.canvas.create_rectangle(point[0]-5,
                                         point[1]-5,
                                         point[0]+5,
                                         point[1]+5,
                                         outline='blue')

    def drawcurveline(self):
        edgepoints = self.curve.getedgepoints(self.step * self.stepsize)
        
        self.canvas.create_line(edgepoints[0][0],
                                edgepoints[0][1],
                                edgepoints[1][0],
                                edgepoints[1][1],
                                fill = 'red')

    def drawcurvepoint(self):
        curvepoint = self.curve.getcurvepoint(self.step * self.stepsize)
        self.canvas .create_rectangle(curvepoint[0]-5,
                                      curvepoint[1]-5,
                                      curvepoint[0]+5,
                                      curvepoint[1]+5)



