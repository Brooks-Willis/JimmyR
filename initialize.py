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
    rhTwist = Robotis_Servo(dyn, 7, 'MX')
    lhTwist = Robotis_Servo(dyn, 8, 'MX')
    rhTilt = Robotis_Servo(dyn, 9, 'MX')
    lhTilt = Robotis_Servo(dyn, 10, 'MX')
    rhSwing = Robotis_Servo(dyn, 11, 'MX')
    lhSwing = Robotis_Servo(dyn, 12, 'MX')
    rkExt = Robotis_Servo(dyn, 13, 'MX')
    lkExt = Robotis_Servo(dyn, 14, 'MX')
    raExt = Robotis_Servo(dyn, 15, 'MX')
    laExt = Robotis_Servo(dyn, 16, 'MX')
    raTilt = Robotis_Servo(dyn, 17, 'MX')
    laTilt = Robotis_Servo(dyn, 18, 'MX')

    
    return (dyn, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt)

def main():
    dyn, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt  = setup()
    command = raw_input('Next Command? ')
    while command != 'end':
        if command == 'stand':
            rhTwist.move_angle(0)
            lhTwist.move_angle(0)
            rhTilt.move_angle(0)
            lhTilt.move_angle(0)
            rhSwing.move_angle(0)
            lhSwing.move_angle(0)
            rkExt.move_angle(0)
            lkExt.move_angle(0)
            raExt.move_angle(0)
            laExt.move_angle(0)
            raTilt.move_angle(0)
            laTilt.move_angle(0)
        else:
            command = float(command)
            lhSwing.move_angle(radians(command))   
        command = raw_input('Next Command? ')     
     
if __name__ == '__main__':
    main()