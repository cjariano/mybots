# solution.py
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):  # NEW: Accept a unique ID argument.
        self.myID = myID  # NEW:
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Set_ID(self, newID):  # NEW: Update the solution's unique ID.
        self.myID = newID

    def Start_Simulation(self, mode):  # NEW:
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # Build a command string that passes mode and this solution's unique ID to simulate.py.
        cmd = "start /B python simulate.py " + mode + " " + str(self.myID)  # NEW:
        # print("Command:", cmd)  # (Optional debug)
        os.system(cmd)

    def Wait_For_Simulation_To_End(self):  # NEW:
        fitnessFileName = "fitness" + str(self.myID) + ".txt"  # NEW:
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        with open(fitnessFileName, "r") as fitnessFile:
            fitnessStr = fitnessFile.read().strip()
        self.fitness = float(fitnessStr)
        print("Solution", self.myID, "fitness:", self.fitness)  # NEW: For verification
        os.system("del " + fitnessFileName)  # NEW: Clean up the fitness file

    def Evaluate(self, mode):  # (Optional convenience method – not used in PHC now)
        self.Start_Simulation(mode)
        self.Wait_For_Simulation_To_End()

    def Create_World(self):
        length, width, height = 1, 1, 1
        x, y, z = -3, 3, 0.5
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        length, width, height = 1, 1, 1
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])

        # LeftLeg
        pyrosim.Send_Cube(name="LeftLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        
        # RightLeg
        pyrosim.Send_Cube(name="RightLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        #FrontLeg1
        pyrosim.Send_Cube(name="FrontLeg1", pos=[-0.5, 0.1, 0], size=[1, 0.2, 0.2])

        #FrontLeg2
        pyrosim.Send_Cube(name="FrontLeg2", pos=[-0.5, -0.1, 0], size=[1, 0.2, 0.2])

        #BackLeg1
        pyrosim.Send_Cube(name="BackLeg1", pos=[0.5, 0.1, 0], size=[1, 0.2, 0.2])

        #BackLeg2
        pyrosim.Send_Cube(name="BackLeg2", pos=[0.5, -0.1, 0], size=[1, 0.2, 0.2])

        #LeftLowerLeg
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #RightLowerLeg
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #FrontLowerLeg1
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #FrontLowerLeg2
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #BackLowerLeg1
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #BackLowerLeg2
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Joints
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name ="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[-0.5, 0.1, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name ="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[-0.5, -0.1, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[0.5, 0.1, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[0.5, -0.1, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[0, -1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[0, 1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute", position=[-1, 0.1, 0], jointAxis ="0 1 0")
        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute", position=[-1, -0.1, 0], jointAxis ="0 1 0")
        pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute", position=[1, 0.1, 0], jointAxis ="0 1 0")
        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute", position=[1, -0.1, 0], jointAxis ="0 1 0")

        pyrosim.End()

    def Create_Brain(self):
        brainFileName = "brain" + str(self.myID) + ".nndf"  # NEW: Use unique filename
        pyrosim.Start_NeuralNetwork(brainFileName)
        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name="0", linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name="1", linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name="2", linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name="3", linkName="FrontLeg1")
        pyrosim.Send_Sensor_Neuron(name="4", linkName="FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name="5", linkName="BackLeg1")
        pyrosim.Send_Sensor_Neuron(name="6", linkName="BackLeg2")
        pyrosim.Send_Sensor_Neuron(name="7", linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name="8", linkName="RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name="9", linkName="FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name="10", linkName="FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name="11", linkName="BackLowerLeg1")  
        pyrosim.Send_Sensor_Neuron(name="12", linkName="BackLowerLeg2") 

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name="13", jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name="14", jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name="15", jointName="Torso_FrontLeg1")
        pyrosim.Send_Motor_Neuron(name="16", jointName="Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name="17", jointName="Torso_BackLeg1")
        pyrosim.Send_Motor_Neuron(name="18", jointName="Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron(name="19", jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name="20", jointName="RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name="21", jointName="FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron(name="22", jointName="FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name="23", jointName="BackLeg1_BackLowerLeg1")
        pyrosim.Send_Motor_Neuron(name="24", jointName="BackLeg2_BackLowerLeg2")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName=str(currentRow), targetNeuronName=str(currentColumn + c.numSensorNeurons), weight=weight)
        pyrosim.End()
        print(f"Brain file created: {brainFileName}")


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] += random.uniform(-0.1, 0.1)  # Small perturbation
        self.weights[randomRow, randomColumn] = np.clip(self.weights[randomRow, randomColumn], -1, 1)  # Keep within range
