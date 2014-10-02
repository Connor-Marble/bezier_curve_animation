from Tkinter import *
from bcurves import ThreePointCurve, FourPointCurve


class BezierAnimation:
    def __init__(self, canvas, **kwargs):
        self.pointA = kwargs.get('pointA', [0, 0])
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

        if pointD is None:
            self.canvas.create_line(self.pointB[0],
                                    self.pointB[1],
                                    self.pointC[0],
                                    self.pointC[1])

        else:
            self.canvas.create_line(self.pointC[0],
                                    self.pointC[1],
                                    self.pointD[0],
                                    self.pointD[1])

master = Tk()

canvas = Canvas(master, width=200, height=200)

canvas.pack()


curve = BezierAnimation(canvas)
curve.step = 30

curve.drawcurve()
canvas.mainloop()
