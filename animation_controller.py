import time
import curve_animation as CA
import Tkinter
import thread

class SingleAnimation:
    def __init__(self):
        master = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(master, width=400, height=400)
        animation = CA.BezierAnimation(self.canvas)


        self.canvas.pack()


        curve = CA.BezierAnimation(self.canvas,
                                pointA=[5, 5],
                                pointB=[5, 395],
                                   pointC=[395, 395],
                                   steps=30)
        
        thread.start_new(self.animateloop,(curve, 2))
        
        self.canvas.mainloop()

    def animateloop(self, curve, seconds):
        stepcount = 1/curve.stepsize

        for i in range(int(stepcount)):
            curve.step = i
            curve.drawcurve(fill='green')
            curve.drawedgepoints()
            curve.drawoutline()
            curve.drawcurveline()
            curve.drawcurvepoint()
        
            time.sleep(seconds/stepcount)

        thread.start_new(self.animateloop,(curve, 2))
        self.canvas.delete("all")

if __name__ == '__main__':
    s_anim = SingleAnimation()
