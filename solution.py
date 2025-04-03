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

        # LeftLeg1
        pyrosim.Send_Cube(name="LeftLeg1", pos=[0.1, -0.5, 0], size=[0.2, 1, 0.2])

        # LeftLeg2
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.1, -0.5, 0], size=[0.2, 1, 0.2])
        
        # RightLeg1
        pyrosim.Send_Cube(name="RightLeg1", pos=[0.1, 0.5, 0], size=[0.2, 1, 0.2])

        # RightLeg2
        pyrosim.Send_Cube(name="RightLeg2", pos=[-0.1, 0.5, 0], size=[0.2, 1, 0.2])

        #FrontLeg
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        #BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        #LeftLowerLeg1
        pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #LeftLowerLeg2
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #RightLowerLeg1
        pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #RightLowerLeg2
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #FrontLowerLeg
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #BackLowerLeg
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Joints
        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[0.1, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[-0.1, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[0.1, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[-0.1, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name ="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="LeftLeg1_LeftLowerLeg1", parent="LeftLeg1", child="LeftLowerLeg1", type="revolute", position=[0.1, -1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[-0.1, -1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="RightLeg1_RightLowerLeg1", parent="RightLeg1", child="RightLowerLeg1", type="revolute", position=[0.1, 1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[-0.1, 1, 0], jointAxis ="1 0 0")
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis ="0 1 0")
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[1, 0, 0], jointAxis ="0 1 0")


        pyrosim.End()

    def Create_Brain(self):
        brainFileName = "brain" + str(self.myID) + ".nndf"  # NEW: Use unique filename
        pyrosim.Start_NeuralNetwork(brainFileName)
        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name="0", linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name="1", linkName="LeftLeg1")
        pyrosim.Send_Sensor_Neuron(name="2", linkName="LeftLeg2")
        pyrosim.Send_Sensor_Neuron(name="3", linkName="RightLeg1")
        pyrosim.Send_Sensor_Neuron(name="4", linkName="RightLeg2")
        pyrosim.Send_Sensor_Neuron(name="5", linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name="6", linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name="7", linkName="LeftLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name="8", linkName="LeftLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name="9", linkName="RightLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name="10", linkName="RightLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name="11", linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name="12", linkName="BackLowerLeg")  

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name="13", jointName="Torso_LeftLeg1")
        pyrosim.Send_Motor_Neuron(name="14", jointName="Torso_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name="15", jointName="Torso_RightLeg1")
        pyrosim.Send_Motor_Neuron(name="16", jointName="Torso_RightLeg2")
        pyrosim.Send_Motor_Neuron(name="17", jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name="18", jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name="19", jointName="LeftLeg1_LeftLowerLeg1")
        pyrosim.Send_Motor_Neuron(name="20", jointName="LeftLeg2_LeftLowerLeg2")
        pyrosim.Send_Motor_Neuron(name="21", jointName="RightLeg1_RightLowerLeg1")
        pyrosim.Send_Motor_Neuron(name="22", jointName="RightLeg2_RightLowerLeg2")
        pyrosim.Send_Motor_Neuron(name="23", jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name="24", jointName="BackLeg_BackLowerLeg")


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
