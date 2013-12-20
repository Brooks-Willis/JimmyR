from lib_robotis import *
from math import radians

def setup():
    dyn = USB2Dynamixel_Device()
    hip = Robotis_Servo(dyn, 2)
    ankle = Robotis_Servo(dyn, 1)
    return (dyn, hip, ankle)


def main():
    dyn, hip, ankle = setup()
    command = 'start'
    while command != 10:
        command = raw_input('Next Command? ')

        if command == "step":
            hip.move_angle(-2.4)
            ankle.move_angle(radians(25))
            hip.move_angle(-1)
            ankle.move_angle(0)
            hip.move_angle(radians(-90))
        elif command == "hip":
            command = raw_input('Hip Position? ') #0 - -145
            while command != "break":
                command = float(command)
                hip.move_angle(radians(command))
                command = raw_input('hip Position? ')
        elif command == "ankle":
            command = raw_input('Ankle Position? ') #25 to -60
            while command != "break":
                command = float(command)
                ankle.move_angle(radians(command))
                command = raw_input('Ankle Position? ')




if __name__ == '__main__':
    main()