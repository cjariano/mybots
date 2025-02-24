import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = np.zeros(1000)

    def Get_Value(self):
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)