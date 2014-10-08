import time
import curve_animation as CA
import Tkinter
import thread
import math


class CurveDrawAnimation:
    def __init__(self, **kwargs):
        master = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(master, width=400, height=400)

        self.canvas.pack()

        curve = CA.BezierAnimation(self.canvas,
                                   pointA=[200, 5],
                                   pointB=[200, 395],
                                   pointC=[5, 200],
                                   pointD=[395, 200],
                                   steps=60)

        thread.start_new(self.animateloop, (curve, 2, kwargs))
        
        self.canvas.mainloop()

    def animateloop(self, curve, seconds, kwargs):
        stepcount = 1/curve.stepsize

        for i in range(int(stepcount)):
            curve.step = i
            curve.drawcurve()
            curve.drawedgepoints()
            curve.drawoutline()
            curve.drawcurveline()
            curve.drawcurvepoint()
        
            time.sleep(seconds/stepcount)

            if kwargs.get('persist', False) is False:
                self.canvas.delete("all")

        self.canvas.delete("all")
        thread.start_new(self.animateloop, (curve, 2, kwargs))


class CurveMoveAnimation:
    def __init__(self, **kwargs):
        master = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(master, width=400, height=400)

        self.canvas.pack()

        self.pointA = [200, 5]
        self.pointB = [200, 395]
        self.pointC = [5, 200]
        self.pointD = [395, 200]
        self.time = 0

        curve = CA.BezierAnimation(self.canvas,
                                   pointA=self.pointA,
                                   pointB=self.pointB,
                                   pointC=self.pointC,
                                   pointD=self.pointD,
                                   steps=60)

        thread.start_new(self.animateloop, (curve, 2, kwargs))
        
        self.canvas.mainloop()

    def animateloop(self, curve, speed, kwargs):
        stepcount = int(1/curve.stepsize)

        for i in range(stepcount):
            curve.step = 60
            curve.pointA[1] = math.sin(i/float(stepcount) *
                                       2 * math.pi)*200 + 200
            curve.pointB[0] = math.cos(i/float(stepcount + 0.1234) *
                                       2 * math.pi)*200 + 200
            curve.pointC[0] = math.cos(i/float(stepcount + 0.7897) *
                                       2 * math.pi)*200 + 200
            curve.pointA[1] = math.sin(i/float(stepcount + 0.22378) *
                                       2 * math.pi)*200 + 200

            curve.drawcurve()
            curve.drawoutline()
            time.sleep(curve.stepsize)
            print(i)

            if kwargs.get('persist', False) is False:
                self.canvas.delete("all")

        thread.start_new(self.animateloop, (curve, 2, kwargs))

if __name__ == '__main__':
    s_anim = CurveMoveAnimation(persist=False)
