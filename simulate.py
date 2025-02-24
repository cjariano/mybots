import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()

# amplitude_frontleg = c.AMPLITUDE_FRONTLEG
# frequency_frontleg = c.FREQUENCY_FRONTLEG
# phaseOffset_frontleg = c.PHASEOFFSET_FRONTLEG

# amplitude_backleg = c.AMPLITUDE_BACKLEG
# frequency_backleg = c.FREQUENCY_BACKLEG
# phaseOffset_backleg = c.PHASEOFFSET_BACKLEG


# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)

# motorControl_frontleg = np.zeros(1000)
# motorControl_backleg = np.zeros(1000)

# #targetAngles_frontleg = np.sin(np.linspace(-1. ,1. , 1000))
# targetAngles_frontleg = np.linspace(0, 2 * np.pi, 1000)
# targetAngles_frontleg = targetAngles_frontleg * (np.pi / 4)

# #targetAngles_backleg = np.sin(np.linspace(-1. ,1. , 1000))
# targetAngles_backleg = np.linspace(0, 2 * np.pi, 1000)
# targetAngles_backleg = targetAngles_backleg * (np.pi / 4)

# for i in range (1000):
#     motorControl_frontleg[i] = amplitude_frontleg * np.sin(frequency_frontleg * targetAngles_frontleg[i] + phaseOffset_frontleg)
#     motorControl_backleg[i] = amplitude_backleg * np.sin(frequency_backleg * targetAngles_backleg[i] + phaseOffset_backleg)


# #np.save("data/motorControlfront.npy", motorControl_frontleg)
# #np.save("data/motorControlback.npy", motorControl_backleg)


# #exit()

# for i in range (1000):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontLeg")

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotID,
#         jointName=b'torso_backLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=motorControl_backleg[i],
#         maxForce=5)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotID,
#         jointName=b'torso_frontLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=motorControl_frontleg[i],
#         maxForce=5)

#     time.sleep(1/60)


# p.disconnect()
# np.save("data/back_leg_sensor_values.npy", backLegSensorValues)
# np.save("data/front_leg_sensor_values.npy", frontLegSensorValues)