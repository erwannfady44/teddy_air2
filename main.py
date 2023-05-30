from arm import Arm
import time
try:
    arm = Arm(23)  # Utilisation du port GPIO 23 pour le moteur

    # Demarre la rotation continue du moteur
    arm.start()

    a=Arm(5)
    a.start()
    # Laisse le moteur tourner pendant 5 secondes
    time.sleep(5)

    # Arrete la rotation
    arm.stop()
    time
except KeyboardInterrupt:
    arm.cleanup()
