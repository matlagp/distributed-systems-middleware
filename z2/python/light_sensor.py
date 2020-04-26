import Ice
import Home
import random

class LightSensorI(Home.LightSensor):
    def __init__(self):
        self.active = False
        self.readings = []
        for i in range(10):
            self.readings.append(random.random())

    def getLastReading(self, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Supplying last light reading")
        return self.readings[-1]

    def getReadings(self, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Supplying light readings")
        return self.readings

    def on(self, current=None):
        if self.active:
            raise Home.AlreadyOnException

        print("Light sensr activating")
        self.active = True

    def off(self, current=None):
        if self.active == False:
            raise Home.AlreadyOffException

        print("Light sensr deactivating")
        self.active = False