from flask import Flask, request
from flask_cors import CORS
from models.arm import Arm
from models.servo import Servo
from models.motor import Motor

app = Flask(__name__)
CORS(app)

speed = 0
direction = 0
sens = 0

motor = Motor(2)
arm = Arm(5)
servo = Servo(4)
@app.route('/drive', methods=['POST'])
def drive():
    #Récupération des données envoyées
    data = request.get_json()
    #Si on doit Reculer
    if int(data.get('sens')) == -1:
        #Fait reculer à la bonne vitesse
        motor.backward(data.get('speed'))
    #Si on doit avancer
    elif int(data.get('sens')) == 1:
        #Fait avancer à la bonne vitesse
        motor.backward(data.get('speed'))
    #Sinon
    else:
        #Arrêt du moteur
        motor.stop()

    #Si on ne va pas tout droit
    if int(data.get('direction')) != 90:
        #Fait tourner le servo moteur au bon angle
        Servo.set_angle(data.get('direction'))

    return "drive"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    arm.start()