from Tkinter import *
from bcurves import ThreePointCurve


class bezieranimation:
    def __init__(self, **kwargs):
        self.pointA = kwargs.get('pointA', [0, 0])
        self.pointB = kwargs.get('pointB', [100, 0])
        self.pointC = kwargs.get('pointC', [100, 100])
        self.pointD = kwargs.get('pointD', [0, 100])

        self.setpsize = kwargs.get('stepsize', 0.04)
        self.step = 0

master = Tk()

canvas = Canvas(master, width=200, height=200)

canvas.pack()

canvas.create_line(0, 0, 512, 512)

curve = ThreePointCurve([0, 0], [200, 0], [200, 200])

points = []

for i in range(10):
    points.append(curve.getcurvepoint(float(i)/10))

for i in range(len(points)-1):
    canvas.create_line(
        points[i][0], points[i][1], points[i+1][0], points[i+1][1])

canvas.mainloop()
