from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:

    def __init__(self):

        self.motors = {}
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):
        for sensor in self.sensors.values():
            sensor.GetValue() 