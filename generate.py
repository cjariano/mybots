import pyrosim.pyrosim as pyrosim
import numpy as np

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name=f"Box_1", pos=[2, 2, 0.5], size=[1, 1, 1])

    pyrosim.End()

def Create_Robot():
    pass

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg",
                       type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg",
                       type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="backLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()

def Generate_Brain():
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
    for i in range(0,3):
        for j in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight = np.random.uniform(-1, 1))

    pyrosim.End()


def main():
    Create_World()
    Generate_Body()
    Generate_Brain()



if __name__ == "__main__":
    main()