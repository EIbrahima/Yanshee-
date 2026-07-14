// dans ce script, on utilise la camera en direct seulement et le mouvement de la main droit . On peut avoir un visuel sur le web avec l'adresse ip:5000
import sys
# Remplacez le chemin ci-dessous par celui trouvé avec la commande 'find'
sys.path.append('/home/pi/.config/Yanshee')

import YanAPI
import time
import cv2
import threading
import logging
from flask import Flask, Response

# --- CONFIGURATION CAMÉRA ---
app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generer_video():
    while True:
        succes, frame = camera.read()
        if not succes:
            break
        else:
            # Encodage JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_data = buffer.tobytes()
            # Utilisation de bytes concaténés pour Python 3.5
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')

@app.route('/')
def index():
    return Response(generer_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

def lancer_serveur_video():
    # Désactivation des logs
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    # Host 0.0.0.0 accessible sur le réseau
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

# --- PROGRAMME PRINCIPAL ---
if __name__ == "__main__":
    # 1. Démarrage de la caméra en tâche de fond (Thread)
    # Remplacement des f-strings par .format()
    print("Démarrage de la caméra sur http://{}:5000".format("172.16.0.190"))

    thread_video = threading.Thread(target=lancer_serveur_video)
    thread_video.daemon = True
    thread_video.start()

    time.sleep(2)

    # 2. Initialisation du Robot
    print("Connexion au robot...")
    # Si le script tourne SUR le robot, 127.0.0.1 est correct.
    YanAPI.yan_api_init("127.0.0.1")

    # 3. Mouvement
    print("Action : Lever le bras droit...")
    # Vérifiez que les arguments correspondent exactement à votre version de l'API
    YanAPI.sync_play_motion(name="raise", direction="right", speed="normal", repeat=1)

    print("Le robot reste ainsi. Ouvrez votre navigateur pour voir le direct.")
    print("Appuyez sur Ctrl+C dans ce terminal pour quitter.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt en cours...")
        camera.release()