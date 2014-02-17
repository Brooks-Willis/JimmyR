from lib_robotis import *
from math import *
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
    dyn, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt = setup()
    motors = [rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt]
    command = raw_input('Next Command? ')
    while command != 'end':
        if command == 'stand':
            rhTwist.move_angle(0, blocking = False)
            lhTwist.move_angle(0, blocking = False)
            rhTilt.move_angle(0, blocking = False)
            lhTilt.move_angle(0, blocking = False)
            rhSwing.move_angle(0, blocking = False)
            lhSwing.move_angle(0, blocking = False)
            rkExt.move_angle(0, blocking = False)
            lkExt.move_angle(0, blocking = False)
            raExt.move_angle(0, blocking = False)
            laExt.move_angle(0, blocking = False)
            raTilt.move_angle(0, blocking = False)
            laTilt.move_angle(0, blocking = False)

        elif command == 'crouch':
            rhTwist.move_angle(0, blocking = False)
            lhTwist.move_angle(0, blocking = False)
            rhTilt.move_angle(0, blocking = False)
            lhTilt.move_angle(0, blocking = False)
            rhSwing.move_angle(radians(20), angvel = radians(50), blocking = False)
            lhSwing.move_angle(radians(-20), angvel = radians(50), blocking = False)
            rkExt.move_angle(radians(-40), blocking = False)
            lkExt.move_angle(radians(-40), blocking = False)
            raExt.move_angle(radians(-20), angvel = radians(50), blocking = False)
            laExt.move_angle(radians(-20), angvel = radians(50), blocking = False) 
            raTilt.move_angle(0, blocking = False)
            laTilt.move_angle(0, blocking = False)

            

        elif command == 'makesetpoint':
            for motor in motors:
                motor.disable_torque()
            command = raw_input('Ready to read angles? ')
            if command == 'yes':
                angles = []
                for i in range(len(motors)):
                    angles.append(degrees(motors[i].read_angle()))

            print angles


        else:
            command = float(command)
            lhSwing.move_angle(radians(command))   
        command = raw_input('Next Command? ')     
     
if __name__ == '__main__':
    main()