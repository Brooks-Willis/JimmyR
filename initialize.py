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
    rsPitch = Robotis_Servo(dyn, 1, 'MX')
    lsPitch = Robotis_Servo(dyn, 2, 'MX')
    rsRoll = Robotis_Servo(dyn, 3, 'MX')
    lsRoll = Robotis_Servo(dyn, 4, 'MX')
    reExt = Robotis_Servo(dyn, 5, 'MX')
    leExt = Robotis_Servo(dyn, 6, 'MX')
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
    neck1 = Robotis_Servo(dyn, 19, 'MX')
    neck2 = Robotis_Servo(dyn, 20, 'MX')
    reRoll = Robotis_Servo(dyn, 21, 'MX')
    leRoll = Robotis_Servo(dyn, 22, 'MX')
    neckRot = Robotis_Servo(dyn, 27, 'MX')

    
    return (dyn, rsPitch, lsPitch, rsRoll, lsRoll, reExt, leExt, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt, neck1, neck2, reRoll, leRoll, neckRot)

def main():
    dyn, rsPitch, lsPitch, rsRoll, lsRoll, reExt, leExt, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt, neck1, neck2, reRoll, leRoll, neckRot = setup()
    motors = [rsPitch, lsPitch, rsRoll, lsRoll, reExt, leExt, rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt, neck1, neck2, reRoll, leRoll, neckRot]
    legmotors = [rhTwist, lhTwist, rhTilt, lhTilt, rhSwing, lhSwing, rkExt, lkExt, raExt, laExt, raTilt, laTilt]
    torsomotors = [rsPitch, lsPitch, rsRoll, lsRoll, reExt, leExt, neck1, neck2, reRoll, leRoll, neckRot]
    legposition = [1,1,1,1,1,1,1,1,1,1,1,1]
    torsoposition = [1,1,1,1,1,1,1,1,1,1,1]
    maxSpeed = radians(100)
    command = raw_input('Next Command? ')
    while command != 'end':
        if command == 'stand':
            target = [0,0,0,0,0,0,0,0,0,0,0,0]
            legposition = move_legs(legmotors, target, legposition, maxSpeed)

        elif command == 'crouch':
            target = [0,0,0,0,radians(20),radians(-20),radians(-40),radians(-40),radians(-20),radians(-20),0,0]
            legposition = move_legs(legmotors, target, legposition, maxSpeed)

        elif command == 'balance':
            #Stand Up
            target = [0,0,0,0,0,0,0,0,0,0,0,0]
            legposition = move_legs(legmotors, target, legposition, maxSpeed)
            #Shift Arms and Head
            command = raw_input('step (hit enter to proceed)')
            target = [radians(39.8), radians(1.6), radians(13.98), radians(35.87), radians(-70.2), radians(-6.8), radians(-5.3), radians(17.7), radians(156.3), radians(-83.9), radians(6.3)]
            torsoposition = move_torso(torsomotors,target, torsoposition, maxSpeed/2)
            #Shift onto Left Foot
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(13),radians(5),0,0,0,0,0,0,radians(-13),radians(-15)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed/2)
            #Lift Right Leg
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(13),radians(5),radians(20),0,radians(-40),0,radians(-20),0,radians(-13),radians(-15)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed) 
            #Right Leg Forward
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(13),radians(5),radians(15),0,0,0,radians(15),0,radians(-13),radians(-15)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed)
            #Body Forward
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(13),radians(5),radians(10),radians(10),0,0,radians(10),radians(-10),radians(-13),radians(-13)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed/3)
            #Shift Weight Right
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(-5),radians(-13),radians(10),radians(10),0,0,radians(10),radians(-10),radians(15),radians(13)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed/4)
            #Move Forward
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(-5),radians(-13),radians(0),radians(0),0,0,radians(0),radians(0),radians(15),radians(13)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed/4)
            #Lift Left Leg
            command = raw_input('step (hit enter to proceed)')
            target = [0,0,radians(-5),radians(-13),0,radians(-20),0,radians(-40),0,radians(-20),radians(15),radians(13)]
            legposition = move_legs(legmotors, target, legposition, maxSpeed)
            

        elif command == 'shuffle':
            while True:
                target = [0,0,radians(13),radians(13),0,0,0,0,0,0,radians(-13),radians(-13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed/3) #Shift Left
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break
                target = [0,0,radians(13),radians(13),radians(20),0,radians(-40),0,radians(-20),0,radians(-13),radians(-13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed) #Lift Right Leg
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break
                target = [0,0,radians(13),radians(13),0,0,0,0,0,0,radians(-13),radians(-13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed) #lower Right Leg
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break

                target = [0,0,radians(-13),radians(-13),0,0,0,0,0,0,radians(13),radians(13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed/3) #Shift Right
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break
                target = [0,0,radians(-13),radians(-13),0,radians(-20),0,radians(-40),0,radians(-20),radians(13),radians(13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed) #Lift Left Leg
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break
                target = [0,0,radians(-13),radians(-13),0,0,0,0,0,0,radians(13),radians(13)]
                legposition = move_legs(legmotors, target, legposition, maxSpeed) #Lower Left Leg
                command = raw_input('step (hit enter to proceed)')
                if command != '':
                    break

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

        elif command == 'alarm':
            for motor in motors:
                print motor.read_alarm()


        else:
            print 'Invalid Command'   
        command = raw_input('Next Command? ')     
    
def setSpeed(motors, position, target, maxSpeed):
    change = []
    speeds = []
    print len(position), len(target), len(motors)
    for i in range(len(motors)):
        change.append(abs(position[i] - target[i]))

    maxChange = max(change)
    for change in change:
        speeds.append(maxSpeed * (change/maxChange)) 

    return speeds

def move_torso(motors, target, position, maxSpeed):
    speeds = setSpeed(motors, position, target, maxSpeed)
    rsPitch, lsPitch, rsRoll, lsRoll, reExt, leExt, neck1, neck2, reRoll, leRoll, neckRot = motors
    rsPitch.move_angle(target[0], angvel = speeds[0], blocking = False)
    lsPitch.move_angle(target[1], angvel = speeds[1], blocking = False)
    rsRoll.move_angle(target[2], angvel = speeds[2],blocking = False)
    lsRoll.move_angle(target[3], angvel = speeds[3], blocking = False)
    reExt.move_angle(target[4], angvel = speeds[4], blocking = False)
    leExt.move_angle(target[5], angvel = speeds[5], blocking = False)
    neck1.move_angle(target[6], angvel = speeds[6], blocking = False)
    neck2.move_angle(target[7], angvel = speeds[7], blocking = False) 
    reRoll.move_angle(target[8], angvel = speeds[8], blocking = False)
    leRoll.move_angle(target[9], angvel = speeds[9], blocking = False)
    neckRot.move_angle(target[10], angvel = speeds[10], blocking = True) #Wait for commands to excecute before proceeding
    
    return target

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
    torsoposition = [39.8, 1.6, 13.98, 35.87, -70.2, -6.8, -5.3, 17.7, 156.3, -83.9, 6.3]
    [39.8, 1.6, 13.98, 35.87, -70.2, -6.8, 3.3, 8.5, -10.3, -17.4, -1.9, -0.4, 4.7, -0.7, 3.8, 0.1, 4.7, 11.3, -5.3, 17.7, 156.3, -83.9, 6.3]