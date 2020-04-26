import Ice
import Home

class CCTVI(Home.CCTV):
    def __init__(self):
        self.active = False
        self.zoom = 0
        self.theta = 0

    def getStatus(self, current=None):
        return Home.CCTVStatus(zoom=self.zoom, theta=self.theta)

    def zoomIn(self, zoom, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Zooming in")
        self.zoom += zoom
        if self.zoom > 10:
            self.zoom = 10

    def zoomOut(self, zoom, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Zooming out")
        self.zoom -= zoom
        if self.zoom < 0:
            self.zoom = 0

    def tiltLeft(self, theta, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Tilting")
        self.theta += theta
        if self.theta >= 90:
            self.theta = 90

    def tiltRight(self, theta, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Tilting")
        self.theta -= theta
        if self.theta <= -90:
            self.theta = -90

    def on(self, current=None):
        if self.active == True:
            raise Home.AlreadyOnException

        print("Activating CCTV")
        self.active = True

    def off(self, current=None):
        if self.active == False:
            raise Home.AlreadyOffException

        print("Deactivating CCTV")
        self.active = False