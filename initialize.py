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
    position = [1,1,1,1,1,1,1,1,1,1,1,1]
    maxSpeed = radians(100)
    command = raw_input('Next Command? ')
    while command != 'end':
        if command == 'stand':
            target = [0,0,0,0,0,0,0,0,0,0,0,0]
            position = move_legs(motors, target, position, maxSpeed)

        elif command == 'crouch':
            target = [0,0,0,0,radians(20),radians(-20),radians(-40),radians(-40),radians(-20),radians(-20),0,0]
            position = move_legs(motors, target, position, maxSpeed)

        elif command == 'shuffle':
            while command != 'break':
                target = [0,0,radians(13),radians(13),0,0,0,0,0,0,radians(-13),radians(-13)]
                position = move_legs(motors, target, position, maxSpeed/3) #Shift Left
                command = raw_input('step (hit enter to proceed)')
                target = [0,0,radians(13),radians(13),radians(20),0,radians(-40),0,radians(-20),0,radians(-13),radians(-13)]
                position = move_legs(motors, target, position, maxSpeed) #Lift Right Leg
                command = raw_input('step (hit enter to proceed)')
                target = [0,0,radians(13),radians(13),0,0,0,0,0,0,radians(-13),radians(-13)]
                position = move_legs(motors, target, position, maxSpeed) #lower Right Leg
                command = raw_input('step (hit enter to proceed)')

                target = [0,0,radians(-13),radians(-13),0,0,0,0,0,0,radians(13),radians(13)]
                position = move_legs(motors, target, position, maxSpeed/3) #Shift Right
                command = raw_input('step (hit enter to proceed)')
                target = [0,0,radians(-13),radians(-13),0,radians(-20),0,radians(-40),0,radians(-20),radians(13),radians(13)]
                position = move_legs(motors, target, position, maxSpeed) #Lift Left Leg
                command = raw_input('step (hit enter to proceed)')
                target = [0,0,radians(-13),radians(-13),0,0,0,0,0,0,radians(13),radians(13)]
                position = move_legs(motors, target, position, maxSpeed) #Lower Left Leg
                command = raw_input('step (hit enter to proceed)')

        elif command == 'makesetpoint':
            for motor in motors:
                motor.disable_torque()
            command = raw_input('Ready to read angles? ')
            if command == 'yes':
                angles = []
                for i in range(len(motors)):
                    angles.append(degrees(motors[i].read_angle()))
                print angles

        elif command == 'readpos':
            angles = []
            for i in range(len(motors)):
                angles.append(degrees(motors[i].read_angle()))
            print angles


        else:
            print 'Invalid Command'
            """command = float(command)
            lhSwing.move_angle(radians(command))"""   
        command = raw_input('Next Command? ')     
    
def setSpeed(motors, position, target, maxSpeed):
    change = []
    speeds = []
    for i in range(len(motors)):
        change.append(abs(position[i] - target[i]))

    maxChange = max(change)
    for change in change:
        speeds.append(maxSpeed * (change/maxChange)) 

    return speeds

def move_legs(motors, target, position, maxSpeed):
    speeds = setSpeed(motors, position, target, maxSpeed)
    rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt = motors
    rhTwist.move_angle(target[0], angvel = speeds[0], blocking = False)
    lhTwist.move_angle(target[1], angvel = speeds[1], blocking = False)
    rhTilt.move_angle(target[2], angvel = speeds[2],blocking = False)
    lhTilt.move_angle(target[3], angvel = speeds[3], blocking = False)
    rhSwing.move_angle(target[4], angvel = speeds[4], blocking = False)
    lhSwing.move_angle(target[5], angvel = speeds[5], blocking = False)
    rkExt.move_angle(target[6], angvel = speeds[6], blocking = False)
    lkExt.move_angle(target[7], angvel = speeds[7], blocking = False)
    raExt.move_angle(target[8], angvel = speeds[8], blocking = False)
    laExt.move_angle(target[9], angvel = speeds[9], blocking = False) 
    raTilt.move_angle(target[10], angvel = speeds[10], blocking = False)
    laTilt.move_angle(target[11], angvel = speeds[11], blocking = True) #Wait for commands to excecute before proceeding
    
    return target

if __name__ == '__main__':
    main()