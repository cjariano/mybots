import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np

class MOTOR:
    
    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE_BACKLEG
        self.frequency = c.FREQUENCY_BACKLEG
        self.offset = c.PHASEOFFSET_BACKLEG

        if self.jointName == "torse_frontLeg":
            self.frequency *= 0.5

        self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(0, 2*np.pi, 1000) + self.offset)

    def Set_Value(self, t, robotID):
        targetLocation = self.motorValues[t]
        pyrosim.Set_Motor_For_Joint(
                bodyIndex=robotID,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=targetLocation,
                maxForce=25)
        
    def Save_Values(self):
        np.save("data/motorControls1.npy", self.motorValues[0])
        np.save("data/motorControls2.npy", self.motorValues[1])
        np.save("data/motorControls3.npy", self.motorValues[2])