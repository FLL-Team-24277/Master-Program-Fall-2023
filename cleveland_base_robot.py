from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color, Button, Icon
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


PI = 3.14159

TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

STRAIGHT_SPEED = 600  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2


class BaseRobot:
    """
    A collection of methods and Spike Prime objects for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> import base_robot
    >>> br = base_robot.BaseRobot()
    >>> br.Drive(400) #400mm
    >>> br.GyroTurn(90) #90 deg to the right
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self._version = "0.1 05/19/2023"
        self.leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.A)
        self.robot = GyroDriveBase(self.leftDriveMotor, self.rightDriveMotor, TIRE_DIAMETER, AXLE_TRACK )
        self.robot.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.D)

        self.colorSensor = ColorSensor(Port.F)

        self.myCustomColors = [
            Color(h=154, s=69, v=55), # 0, Green
            Color(h=350, s=78, v=84), # 1, Red
            Color(h=44, s=63, v=100), # 2, Yellow
            Color(h=216, s=84, v=79), # 3, Blue
            Color(h=336, s=77, v=72), # 4, Magenta
            Color(h=0, s=0, v=100), # 5, White
            Color(h=8, s=77, v=100), # 6, Orange
            Color(h=197, s=26, v=53), # 7, Gray
            Color(h=180, s=32, v=9), # 8, None
        ]

        self.myColor2DefaultColorDict = {
            self.myCustomColors[0] : Color.GREEN,
            self.myCustomColors[1] : Color.RED,
            self.myCustomColors[2] : Color.YELLOW,
            self.myCustomColors[3] : Color.BLUE,
            self.myCustomColors[4] : Color.MAGENTA,
            self.myCustomColors[5] : Color.WHITE,
            self.myCustomColors[6] : Color.ORANGE,
            self.myCustomColors[7] : Color.GRAY,
            self.myCustomColors[8] : Color.NONE
        }
        self.colorSensor.detectable_colors(self.myCustomColors)
    
    def GyroTurn(self, angle, then=Stop.HOLD, wait=True):
        self.robot.turn(angle, then, wait)

    def GyroDrive(self, distance, speed = STRAIGHT_SPEED, then=Stop.HOLD, wait=True):
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.robot.straight(distance, then, wait)

    def DriveTank(self, leftMotorSpeed, rightMotorSpeed, measurement, units="mm"):
        pass

    def WaitForMillis(self, millis):
        wait(millis)
