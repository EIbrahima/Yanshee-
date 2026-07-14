#!/usr/bin/env python3
import YanAPI
import time
import lib_yanshee


CONFIG_SERVOS = {
    1: "RightShoulderRoll", 2: "RightShoulderFlex", 3: "RightElbowFlex",
    4: "LeftShoulderRoll", 5: "LeftShoulderFlex", 6: "LeftElbowFlex",
    7: "RightHipLR", 8: "RightHipFB", 9: "RightKneeFlex",
    10: "RightAnkleFB", 11: "RightAnkleUD", 12: "LeftHipLR",
    13: "LeftHipFB", 14: "LeftKneeFlex", 15: "LeftAnkleFB",
    16: "LeftAnkleUD", 17: "NeckLR"
}

def tester_un_servo(id_servo):
    nom = CONFIG_SERVOS[id_servo]
    print("Mouvement du servo n°{:02d} : {}...".format(id_servo, nom))
    YanAPI.set_servos_angles({nom: 90}, runtime=500)
    time.sleep(1)
    YanAPI.set_servos_angles({nom: 45}, runtime=500)
    time.sleep(1)

def menu():
    print("\n--- MENU DE TEST ---")
    for i in range(1, 18):
        print("{:02d}. {}".format(i, CONFIG_SERVOS[i]))
    print("18. Action tous les servo_moteurs")
    print("19. Quitter")
    return input("\nEntrez votre choix : ")

if __name__ == "__main__":
    try:
        YanAPI.yan_api_init("127.0.0.1")

        while True:
            choix = menu()
            if choix.isdigit():
                valeur = int(choix)
                if 1 <= valeur <= 17:
                    tester_un_servo(valeur)
                elif valeur == 18:
                    print("Lancement du test complet...")
                    for i in range(1, 18):
                        tester_un_servo(i)
                elif valeur == 19:
                    print("Sortie...")
                    break
                else:
                    print("Erreur : Valeur hors plage.")
            else:
                print("Erreur : Entree invalide.")
    except KeyboardInterrupt:
        print("\nArret manuel detecte.")
    finally:
        print("Reinitialisation du robot...")
        lib_yanshee.reset_robot()
        print("Robot en position de sécurie.")