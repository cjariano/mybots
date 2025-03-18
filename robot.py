import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.robotID = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")

        pyrosim.Prepare_To_Simulate(self.robotID)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("del brain"+str(self.solutionID)+".nndf")

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotID)
                    
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID,0)
        print(stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        with open("fitness"+str(self.solutionID)+".txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))