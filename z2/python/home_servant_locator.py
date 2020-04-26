import Ice
import Ice.ServantLocatorF_ice
import IcePy
import Home

from light_sensor import LightSensorI
from sound_sensor import SoundSensorI
from cctv import CCTVI

class HomeServantLocator(Ice.ServantLocator):
    def __init__(self, communicator):
        self.communicator = communicator

    def locate(self, curr):
        name = curr.id.name.lower()

        servant = None

        if name == "lightsensor":
            servant = LightSensorI()
            print("Created Light Sensor Servant")
        elif name == "soundsensor":
            servant = SoundSensorI()
            print("Created Sound Sensor Servant")
        elif name == "cctv":
            servant = CCTVI()
            print("Created CCTV Servant")

        if servant is not None:
            curr.adapter.add(servant, self.communicator.stringToIdentity("home/%s" % name))
            return (servant, "")

    def finished(self, curr, servant, cookie):
        pass

    def deactivate(self, category):
        pass

