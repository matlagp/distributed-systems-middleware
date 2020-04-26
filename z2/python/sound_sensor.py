import Ice
import Home
import random

class SoundSensorI(Home.SoundSensor):
    def __init__(self):
        self.active = False
        self.readings = []
        for i in range(10):
            self.readings.append(random.random() * 10)

    def getLastReading(self, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Supplying last sound reading")
        return self.readings[-1]

    def getReadings(self, current=None):
        if self.active == False:
            raise Home.InvalidOperationException

        print("Supplying sound readings")
        return self.reading

    def on(self, current=None):
        if self.active:
            raise Home.AlreadyOnException

        print("Sound sensor activating")
        self.active = True

    def off(self, current=None):
        if self.active == False:
            raise Home.AlreadyOffException

        print("Sound sensor deactivating")
        self.active = False