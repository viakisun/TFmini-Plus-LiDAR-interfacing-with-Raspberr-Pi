from WindowHome import *
from WindowDistanceMode import *

class ManageWindow:

    windowHome = None
    windowDistance = None

    @classmethod
    def getWindows(cls):
        ManageWindow.windowHome = WindowHome()
        ManageWindow.windowDistance = WindowDistanceMode()