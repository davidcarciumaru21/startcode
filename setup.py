# ************ IMPORTS ************
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread
from errors import *

# ************ ROBOT CLASS ************
class Robot:
    def __init__(self, wheel_diameter: float, axle_track: float) -> None:
        # Initialize robot parameters
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.ev3 = EV3Brick()

        # Initialize motors
        self.left_motor = self._init_motor(Port.B, "Left motor", Direction.COUNTERCLOCKWISE)
        self.right_motor = self._init_motor(Port.C, "Right motor", Direction.COUNTERCLOCKWISE)
        self.left_arm_motor = self._init_motor(Port.A, "Left arm motor")
        self.right_arm_motor = self._init_motor(Port.D, "Right arm motor")

        # Initialize sensors
        self.touch_sensor = self._init_sensor(TouchSensor, Port.S4, "Touch sensor")
        self.gyro_sensor = self._init_sensor(GyroSensor, Port.S1, "Gyro sensor")

        # Initialize drive base
        self.drive_base = DriveBase(self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track)

        # Thread control locks
        self.lock0 = _thread.allocate_lock()
        self.lock1 = _thread.allocate_lock()
        self.lock2 = _thread.allocate_lock()
        self.lock3 = _thread.allocate_lock()
        self.thread_stop_flag = False

        # List of motors for easy access
        self.motor_list = [self.left_motor, self.right_motor, self.left_arm_motor, self.right_arm_motor]

    # ************ INITIALIZATION METHODS ************
    def _init_motor(self, port: Port, name: str, direction=Direction.CLOCKWISE) -> Motor:
        """Initialize a motor and handle errors if it fails."""
        try:
            return Motor(port, direction)
        except Exception as e:
            raise UnableToFindMotor(f"{name}: {str(e)}")

    def _init_sensor(self, sensor_class: object, port: Port, name: str) -> object:
        """Initialize a sensor and handle errors if it fails."""
        try:
            return sensor_class(port)
        except Exception as e:
            raise UnableToFindSensor(f"{name}: {str(e)}")

    # ************ MOVEMENT CONTROL ************
    def stop_robot(self) -> None:
        """Stop all motors."""
        for motor in self.motor_list:
            motor.stop()

    def hold_robot(self) -> None:
        """Hold all motors in place."""
        for motor in self.motor_list:
            motor.hold()

    # ************ THREAD CONTROL ************
    def start_threads(self) -> None:
        """Allow threads to run."""
        self.thread_stop_flag = False

    def stop_threads(self) -> None:
        """Stop all threads."""
        self.thread_stop_flag = True

    # ************ THREADED MOVEMENTS ************
    def _run_thread(self, function: callable, args: tuple) -> None:
        """Start a new thread if threads are not stopped."""
        if not self.thread_stop_flag:
            _thread.start_new_thread(function, args)

    def straight_threaded(self, distance: int, lock: object) -> None:
        """Move the robot straight in a threaded manner."""
        with lock:
            self.drive_base.straight(distance)

    def run_motor_by_time_threaded(self, speed: int, duration: int, motor: Motor, lock: object) -> None:
        """Run a motor for a specific duration in a threaded manner."""
        with lock:
            motor.run_time(speed, duration)

    def run_motor_by_angle_threaded(self, speed: int, angle: int, motor: Motor, lock: object) -> None:
        """Run a motor to a specific angle in a threaded manner."""
        with lock:
            motor.run_angle(speed, angle)

    # ************ GYRO-ASSISTED MOVEMENT ************
    def gyro_goto(self, target_angle: int, speed: int, timeout: int = 4000, spin_direction: int = 1) -> None:
        """Turn the robot to a target angle using the gyro sensor."""
        self.drive_base.stop()
        timer = StopWatch()

        while timer.time() < timeout:
            current_angle = self.gyro_sensor.angle()
            if abs(target_angle - current_angle) <= 10:
                break

            direction = 1 if current_angle < target_angle else -1
            self.left_motor.run(direction * speed)
            self.right_motor.run(-direction * speed)

            if timer.time() >= timeout:
                print("Abandoning due to timeout")
                self.hold_robot()
                return

        self.hold_robot()
        self.drive_base.turn(target_angle - self.gyro_sensor.angle())