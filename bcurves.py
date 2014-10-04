
class FourPointCurve:
    def __init__(self, pointA, pointB, pointC, pointD):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.pointD = pointD

    def lerp(self, a, b, t):

        if not len(a) == len(b):
            raise error('Mismatched point dimensions')

        result = []

        for i in range(len(a)):
            result.append(a[i] + (b[i]-a[i])*t)

        return result

    def getcurvepoint(self, t):
        ABpoint = self.lerp(self.pointA, self.pointB, t)
        CDpoint = self.lerp(self.pointC, self.pointD, t)
        curvepoint = self.lerp(ABpoint, CDpoint, t)

        return curvepoint
        
    def getedgepoints(self, t):
        edgepoints = []
        
        firstpoint = self.lerp(self.pointA, self.pointB, t)
        secondpoint = self.lerp(self.pointC, self.pointD, t)

        edgepoints.append(firstpoint)
        edgepoints.append(secondpoint)

        return edgepoints

class ThreePointCurve:

    def __init__(self, pointA, pointB, pointC):
        self.curve = FourPointCurve(pointA, pointB, pointB, pointC)

    def getcurvepoint(self, t):
        return self.curve.getcurvepoint(t)

    def getedgepoints(self, t):
        return self.curve.getedgepoints(t)

