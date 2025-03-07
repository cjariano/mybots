import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np

class MOTOR:
    
    def __init__(self, jointName):

        self.jointName = jointName


    def Set_Value(self, desiredAngle, robotID):
        targetLocation = float(desiredAngle) #self.motorValues[desiredAngle]
        pyrosim.Set_Motor_For_Joint(
                bodyIndex=robotID,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=targetLocation,
                maxForce=50)
