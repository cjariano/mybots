from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time



class SIMULATION:

    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8, physicsClient)
        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range (1000):
            print(i)
            p.stepSimulation()
            self.robot.Sense()
            
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName=b'torso_backLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=motorControl_backleg[i],
            #     maxForce=5)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotID,
            #     jointName=b'torso_frontLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=motorControl_frontleg[i],
            #     maxForce=5)

            time.sleep(1/60)