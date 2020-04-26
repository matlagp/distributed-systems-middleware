import sys, Ice
import Home
from home_servant_locator import HomeServantLocator

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("HomeAdapter", "default -p 10000")
    
    adapter.addServantLocator(HomeServantLocator(communicator), "home")

    adapter.activate()
    communicator.waitForShutdown()