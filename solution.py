import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:
    
    def __init__(self):
        self.weights = np.random.rand(3,2)

        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python simulate.py {directOrGUI}")
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg",
                           type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg",
                           type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="backLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "frontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "torso_backLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "torso_frontLeg")
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -5.0 )
        pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = -5.0 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -3.0)
        pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -4.0)
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 2.0)
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = np.random.randint(0,2)
        randomColumn = np.random.randint(0,1)
        self.weights[randomRow, randomColumn] = np.random.random() * 2 - 1
