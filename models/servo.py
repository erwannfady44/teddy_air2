import RPi.GPIO as GPIO

class Servo:
    def __init__(self, servo_pin):
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)

    def set_angle(self, angle):
        duty_cycle = angle / 18 + 2
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(duty_cycle)


    def disconnect(self):
        self.pwm.stop()
        GPIO.cleanup()

