from lib_robotis import *
from math import radians
#U2D = USB2Dynamixel_Device()
"""
s = shoulder
e = elbow
h = hip
k = knee
a = ankle
"""
#rsPitch = Robotis_Servo(U2D,1)
#lsPitch = Robotis_Servo(U2D,2)
#sRoll = Robotis_Servo(U2D,3)

#r = Robotis_Servo(U2D,1)

def setup():
    dyn = USB2Dynamixel_Device()
    r = Robotis_Servo(dyn, 1, 'MX')
    return (dyn, r)

def main():
    dyn, r = setup()
    command = 'start'
    while command != 10:
        command = raw_input('Next Command? ')
        command = float(command)
        r.move_angle(radians(command))    
     
if __name__ == '__main__':
    main()