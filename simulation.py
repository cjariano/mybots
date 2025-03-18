from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time



class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            physicsClient = p.connect(p.DIRECT)
        else:
            physicsClient = p.connect(p.GUI)

        self.directOrGUI = directOrGUI
        solutionID

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8, physicsClient)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range (1000):
            # print(t)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI":
                time.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()