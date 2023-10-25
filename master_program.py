from base_robot import *

# Import missions
import jonas_missions
import sadie_test
import giovanni_missions
import rj_cleve_mission
import cad_car_mission
import zack_mission

br = BaseRobot()

pressed = []
col = br.colorSensor.color()

while True:
    while True:
        col = br.colorSensor.color()
        # The first thing this program does is it detects what color is
        # being help up to the robot color sensor.
        # If no color is detected, then it will display a sad face
        if col == Color.SENSOR_NONE:
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:  #  If a color is detected, then it will display a happy face
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])

        wait(50)
        pressed = br.hub.buttons.pressed()
        #  When the left button is pressed, it will break out of the loop
        if Button.LEFT in pressed:
            break
        if Button.BLUETOOTH in pressed:
            # If the Bluetooth button is pressed, it will run the motors fast for
            # cleaning
            if br.leftDriveMotor.speed() == 0:
                br.leftDriveMotor.run(5000)
                br.rightDriveMotor.run(5000)
            else:
                br.leftDriveMotor.run(0)
                br.rightDriveMotor.run(0)

    # It will now launch the mission coresponding to the color
    # If detected color is Red, then run RJ's mission
    if col == Color.SENSOR_RED:
        rj_cleve_mission.Run(br)
        # If detected color is Orange, then run Jonas' mission
    if col == Color.SENSOR_ORANGE:
        jonas_missions.Run(br)
        # If detected color is White, then run Sadie's mission
    if col == Color.SENSOR_WHITE:
        sadie_test.Run(br)
        # If detected color is Magenta, then run Cadence's & Carter's mission
    if col == Color.SENSOR_MAGENTA:
        cad_car_mission.Run(br)
        # If detected color is Dark Gray, then run Zack's mission
    if col == Color.SENSOR_DARKGRAY:
        zack_mission.Run(br)
    # If detected color is Yellow, then run Giovanni's mission
    if col == Color.SENSOR_YELLOW:
        giovanni_missions.Run(br)
