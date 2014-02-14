from lib_robotis import *

U2D = USB2Dynamixel_Device()
"""
s = shoulder
e = elbow
h = hip
k = knee
a = ankle
"""
rsPitch = Robotis_Servo(U2D,1)
lsPitch = Robotis_Servo(U2D,2)
rsRoll = Robotis_Servo(U2D,3)

