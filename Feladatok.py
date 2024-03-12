#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

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

    def elsoFeladat(self):
        #menjen előre arobot 30 cm
        self.robot.straight(300)

    def masodikFeladat(self):
        #forduljon jobbra 90°-ot
        self.robot.turn(90)

    def harmadikFeladat(self):
        ut = 100
        fordul = 90
        # menjen előre
        self.robot.straight(ut)
        # menjen hátra
        self.robot.straight(ut*(-1))
        # foruljon 90°-ot jobbra
        self.robot.turn(fordul)
        # forduljon 90°-ot balra
        self.robot.turn(-1*fordul)

    def negyedikFeladat(self):
        self.robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
        self.robot.drive(100, 0)
        wait(1000)
        self.robot.stop()
        self.robot.drive(0, 90)
        wait(1000)
        self.robot.stop()
        self.robot.drive(-100, 0)
        wait(1000)
        self.robot.stop()
        self.robot.drive(0, -90)
        wait(1000)
        self.robot.stop()

    def koszon(self):
        self.ev3.speaker.set_volume(100)
        
        
    def csipog(self):
        self.ev3.speaker.beep()

    def korbefordul1(self):
        # a két kerék különböző irányba mozog azonos sebeséggel
        while self.jm.angle() <= 995:
            self.jm.run(speed=100)
            self.bm.run(speed=(-100))
        self.jm.hold()
        self.bm.hold()

    def korbefordul2(self):
        # az egyik kerék áll, a másik kerék mozog adott sebességgel egy irányba
        self.bm.hold()
        while self.jm.angle() <= 1960:
            self.jm.run(speed=100)
        self.jm.hold()

    def korbefordul3(self):
        # mind a két kerék azonos sebeséggel mozog azonos irányba
        self.robot.settings(straight_speed=1, straight_acceleration=1, turn_rate=1)
        self.robot.drive(1, 360)
        wait(1380)
        self.robot.stop(Stop.COAST)
        pass

    def vonalkovet(self):
        self.ev3.speaker.set_volume(1000)
        self.robot.settings(straight_speed=1000)
        self.robot.straight(1500)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(1200)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(1600)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(1300)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(600)
        wait(300)
        self.robot.turn(360)
        wait(300)
        sel.robot.turn(-360)
        wait(300)
        self.robot.stop(STOP_BREAKE)
        

    def hattra(self):
        self.ev3.speaker.set_volume(1000)
        self.robot.settings(straight_speed=1000)
        self.robot.straight(-1500)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1200)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1600)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1000)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-300)
        wait(300)
        self.robot.turn(340)
        wait(300)
        sel.robot.turn(1080)
        wait(300)
        self.robot.stop(STOP_BREAKE)
        self.ev3.speaker("teve.wav")
        
    def kozepso(self):
        self.ev3.speaker.set_volume(1000)
        self.robot.settings(straight_speed=1000)
        self.robot.straight(-1700)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1400)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1400)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-1200)
        wait(300)
        self.robot.turn(-100)
        wait(300)
        self.robot.straight(-500)
        wait(300)
        self.robot.turn(340)
        wait(300)
        self.robot.turn(-720)
        wait(300)
        self.robot.stop(STOP_BREAKE)
        self.ev3.speaker("teve.wav")
       
        
        
