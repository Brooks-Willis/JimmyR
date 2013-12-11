from lib_robotis import *

def setup():
	dyn = USB2Dynamixel_Device()
	hip = Robotis_Servo(2, dyn, 'AX')
	ankle = Robotis_Servo(1, dyn, 'AX')


def main():
	setup()

if __name__ == '__main__':
	main()