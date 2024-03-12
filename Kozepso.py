#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Kozep():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)
def kozepso(self):
     self.ev3.speaker.set_volume(1000)
        self.robot.settings(straight_speed=1000)
        self.robot.straight(-1700)
        wait(300)
        self.robot.turn(-90)
        wait(300)
        self.robot.straight(-1400)
        wait(300)
        self.robot.turn(-70)
        wait(300)
        self.robot.straight(-3000)
        wait(300)
        self.robot.turn(-90)
        wait(300)
        self.robot.straight(-1200)
        wait(300)
        self.robot.turn(-90)
        wait(300)
        self.robot.straight(-500)
        wait(300)
        self.robot.turn(340)
        wait(300)
        self.robot.turn(-720)
        wait(300)
        self.robot.stop(STOP_BREAKE)
        self.ev3.speaker("teve.wav")