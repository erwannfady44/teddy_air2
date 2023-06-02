import RPi.GPIO as GPIO

class Motor:
    def __init__(self, l_en, r_en):
        self.l_en = l_en
        self.r_en = r_en
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.l_en, GPIO.OUT)
        GPIO.setup(self.r_en, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.r_en, 100)
        self.pwm_backward = GPIO.PWM(self.l_en, 100)

        self.pwm_forward.start(0)
        self.pwm_backward.start(0)

    def forward(self, speed):
        self.pwm_forward.ChangeDutyCycle(speed)
        self.pwm_backward.ChangeDutyCycle(0)

    def backward(self, speed):
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm_forward.stop()
        self.pwm_backward.stop()
        GPIO.cleanup()
