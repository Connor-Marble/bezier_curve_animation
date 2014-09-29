
class 4PointCurve():
    def init(self, pointA, pointB, PointC, pointD):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.pointD = pointD

    def lerp(a, b, t):

        if not len(a) == len(b):
            raise error('Mismatched point dimensions')

        result = []

        for i in a:
            result.append(a[i] + (b[i]-a[i])*t)

        return result

    def getcurvepoint(self, t):
        ABpoint = lerp(self.pointA, self.pointC, t)
        CDpoint = lerp(self.PointC, self.pointD, t)
        curvepoint = lerp(ABpoint, CDpoint, t)

        return curvepoint
        

class 3PointCurve():

    def init(self, pointA, pointB, pointC):
        self.curve = 4PointCurve(pointA, pointB, pointB, pointC)

    def getcurvepoint(self, t):
        return self.curve.getcurvepoint(t)
