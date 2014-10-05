import time
import curve_animation as CA
import Tkinter
import thread

class SingleAnimation:
    def __init__(self, **kwargs):
        master = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(master, width=400, height=400)

        self.canvas.pack()


        curve = CA.BezierAnimation(self.canvas,
                                pointA=[200, 5],
                                pointB=[200, 395],
                                pointC=[5, 200],
                                pointD=[395, 200],
                                   steps=60,
                                   thickness=2)

        thread.start_new(self.animateloop,(curve, 2, kwargs))
        
        self.canvas.mainloop()

    def animateloop(self, curve, seconds, kwargs):
        stepcount = 1/curve.stepsize

        for i in range(int(stepcount)):
            curve.step = i
            curve.drawcurve(fill='green')
            curve.drawedgepoints()
            curve.drawoutline()
            curve.drawcurveline()
            curve.drawcurvepoint()
        
            time.sleep(seconds/stepcount)

            if kwargs.get('persist',False) is False:
                self.canvas.delete("all")

        self.canvas.delete("all")
        thread.start_new(self.animateloop,(curve, 2, kwargs))

        thread.start_new(self.animateloop,(curve, 2))
        self.canvas.delete("all")

if __name__ == '__main__':
    s_anim = SingleAnimation(persist=False)


