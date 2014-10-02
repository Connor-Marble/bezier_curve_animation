from Tkinter import *
from bcurves import ThreePointCurve, FourPointCurve


class bezieranimation:
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
        curvepoints = []

        for i in range(self.step+1):
            curvepoints.append(self.curve.getcurvepoint(self.stepsize * i))

        for i in range(len(curvepoints)-1):
            self.canvas.create_line(
                curvepoints[i][0],
                curvepoints[i][1],
                curvepoints[i+1][0],
                curvepoints[i+1][1])

master = Tk()

canvas = Canvas(master, width=200, height=200)

canvas.pack()


curve = bezieranimation(canvas)
curve.step = 30

curve.drawcurve()
canvas.mainloop()
