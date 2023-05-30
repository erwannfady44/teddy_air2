from servo import Servo
import time
import threading


class Arm:
    def __init__(self, servo_pin):
        self.servo = Servo(servo_pin)
        self.is_running = False
        self.thread = None

    def start(self):
        if self.is_running:
            return

        self.is_running = True
        self.thread = threading.Thread(target=self.move_arm, args=())
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()

    def move_arm(self):
        angle = 0
        while self.is_running:
            if angle == 180:
                direction = -1
            elif angle == 0:
                direction = 1

            angle += direction
            self.servo.set_angle(angle)
            time.sleep(0.015)

    def cleanup(self):
        self.stop()
        self.servo.disconnect()
