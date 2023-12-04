from base_robot import *


def Run(br: BaseRobot):
    # ACCEL = 350
    # br.robot.settings(
    # straight_speed=400,
    # straight_acceleration=ACCEL,
    # turn_rate=150,
    # turn_acceleration=360,
    # )
    br.rightAttachmentMotor.run_time(-500, 1000, wait=False)
    br.GyroDrive(300, 977)
    br.Curve(radius=370, angle=-70, speed=977)
    br.GyroDrive(475, 750)
    br.GyroTurn(35)
    # br.WaitForMillis(10000)
    br.GyroDrive(-100, 700)
    br.GyroTurn(-50)
    br.GyroDrive(500, 977)
    br.GyroTurn(35)
    br.rightAttachmentMotor.run_time(500, 1000)
    br.GyroDrive(-300, 977)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(515, 977)  # drive 340 mm
    br.GyroDrive(-600, 977)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
