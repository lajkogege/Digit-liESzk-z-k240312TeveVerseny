from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok
def hattra(self):
        self.ev3.speaker.set_volume(1000)
        self.robot.settings(straight_speed=1000)
        self.robot.straight(-1500)
        wait(300)
        self.robot.turn(100)
        wait(300)
        self.robot.straight(-1200)
        wait(300)
        self.robot.turn(100)
        wait(300)
        self.robot.straight(-1600)
        wait(300)
        self.robot.turn(100)
        wait(300)
        self.robot.straight(-1300)
        wait(300)
        self.robot.turn(100)
        wait(300)
        self.robot.straight(-600)
        wait(300)
        self.robot.turn(360)
        wait(300)
        sel.robot.turn(-360)
        wait(300)
        self.robot.stop(STOP_BREAKE)