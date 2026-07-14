#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import YanAPI
import lib_yanshee
import time
import os
import sys
import csv
import cv2
from datetime import datetime

# --- Configuration ---
CSV_FILE = "Data_move.csv"

# --- Fonctions utilitaires ---
def get_safe_battery():
    try:
        return YanAPI.get_robot_battery_value()
    except Exception:
        try:
            info = YanAPI.get_robot_battery_info()
            return info.get('level', info.get('value', 'N/A'))
        except:
            return "N/A"

def get_light_level():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_light = cv2.mean(gray)[0]
        cap.release()
        return round(avg_light, 2)
    cap.release()
    return 0.0

def log_to_csv(action_nom, index, resultat, code_erreur, attente, batt_avant, batt_apres):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "action_nom", "lumiere", "batt_avant", "batt_apres", "index", "resultat", "code_erreur", "attente"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            action_nom,
            get_light_level(),
            batt_avant,
            batt_apres,
            index,
            resultat,
            code_erreur,
            "{:.3f}".format(attente)
        ])

# --- Fonctions de mouvement ---
def move_reset(): YanAPI.sync_play_motion(name="reset")
def move_raise(): YanAPI.sync_play_motion(name="raise", direction="both")
def move_crouch(): YanAPI.sync_play_motion(name="crouch")
def move_come_on(): YanAPI.sync_play_motion(name="come on", direction="both")
def move_stretch(): YanAPI.sync_play_motion(name="stretch", direction="both")
def move_wave(): YanAPI.sync_play_motion(name="wave", direction="both")
def move_turn(): YanAPI.sync_play_motion(name="turn around", direction="left")

def move_walk_forward(): YanAPI.sync_play_motion(name="walk", direction="forward", speed="normal", repeat=4)
def move_walk_backward(): YanAPI.sync_play_motion(name="walk", direction="backward", speed="normal", repeat=4)
def move_turn_left(): YanAPI.sync_play_motion(name="OneStepTurnLeft", direction="left", speed="normal", repeat=5)
def move_turn_right(): YanAPI.sync_play_motion(name="OneStepTurnRight", direction="right", speed="normal", repeat=5)
def move_raise_left(): YanAPI.sync_play_motion(name="raise", direction="left", speed="normal", repeat=1)
def move_raise_right(): YanAPI.sync_play_motion(name="raise", direction="right", speed="normal", repeat=1)
def move_raise_both(): YanAPI.sync_play_motion(name="raise", direction="both", speed="normal", repeat=1)
def move_stop(): YanAPI.sync_play_motion(name="stop", speed="normal", repeat=1)
def move_wave_right(): YanAPI.sync_play_motion(name="wave", direction="right", speed="normal", repeat=1)
def move_wave_left(): YanAPI.sync_play_motion(name="wave", direction="left", speed="normal", repeat=1)
def move_bow(): YanAPI.sync_play_motion(name="bow", speed="normal", repeat=1)

# ---- Fonction à l'aide des servo moteurs -----

def bras_d_lat(): YanAPI.set_servos_angles({"RightShoulderRoll": 90, "RightShoulderFlex": 90, "RightElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_d_arr(): YanAPI.set_servos_angles({"RightShoulderRoll": 0, "RightShoulderFlex": 0, "RightElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_d_av(): YanAPI.set_servos_angles({"RightShoulderRoll": 180, "RightShoulderFlex": 0, "RightElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_d_poi(): YanAPI.set_servos_angles({"RightShoulderRoll": 180, "RightShoulderFlex": 0, "RightElbowFlex": 20}, runtime=800); time.sleep(1)
def bras_g_lat(): YanAPI.set_servos_angles({"LeftShoulderRoll": 90, "LeftShoulderFlex": 90, "LeftElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_g_arr(): YanAPI.set_servos_angles({"LeftShoulderRoll": 0, "LeftShoulderFlex": 0, "LeftElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_g_av(): YanAPI.set_servos_angles({"LeftShoulderRoll": 180, "LeftShoulderFlex": 0, "LeftElbowFlex": 90}, runtime=800); time.sleep(1)
def bras_g_poi(): YanAPI.set_servos_angles({"LeftShoulderRoll": 180, "LeftShoulderFlex": 0, "LeftElbowFlex": 20}, runtime=800); time.sleep(1)
def bras_tete(): YanAPI.set_servos_angles({"RightShoulderRoll": 90, "RightShoulderFlex": 0, "RightElbowFlex": 20, "LeftShoulderRoll": 90, "LeftShoulderFlex": 180, "LeftElbowFlex": 150}, runtime=800); time.sleep(1)
def bras_drt_tete(): YanAPI.set_servos_angles({"RightShoulderRoll": 90, "RightShoulderFlex": 0, "RightElbowFlex": 20}, runtime=800); time.sleep(1)
def bras_gch_tete(): YanAPI.set_servos_angles({"LeftShoulderRoll": 90, "LeftShoulderFlex": 180, "LeftElbowFlex": 150}, runtime=800); time.sleep(1)
def bras_poi_tot(): YanAPI.set_servos_angles({"RightShoulderRoll": 180, "RightShoulderFlex": 0, "RightElbowFlex": 20, "LeftShoulderRoll": 180, "LeftShoulderFlex": 0, "LeftElbowFlex": 20}, runtime=800); time.sleep(1)

# --- Programme principal ---
def main():
    if os.geteuid() != 0:
        print("ERREUR: Ce script doit être lancé avec sudo.")
        sys.exit(1)

    YanAPI.yan_api_init("127.0.0.1")
    lib_yanshee.reset_robot()

    actions = [
        ("Reset", move_reset), ("Raise", move_raise), ("Crouch", move_crouch),
        ("Come On", move_come_on), ("Stretch", move_stretch), ("Wave", move_wave),
        ("Turn Around", move_turn),
        ("Walk Fwd", move_walk_forward), ("Walk Back", move_walk_backward),
        ("Turn Left", move_turn_left), ("Turn Right", move_turn_right),
        ("Raise Left", move_raise_left), ("Raise Right", move_raise_right),
        ("Raise Both", move_raise_both), ("Stop", move_stop),
        ("Wave Right", move_wave_right), ("Wave Left", move_wave_left), ("Bow", move_bow),
        ("Bras Droit Lateral", bras_d_lat), ("Bras Droit Arriere", bras_d_arr),
        ("Bras Droit Avant", bras_d_av), ("Bras Droit Poitrine", bras_d_poi),
        ("Bras Gauche Lateral", bras_g_lat), ("Bras Gauche Arriere", bras_g_arr),
        ("Bras Gauche Avant", bras_g_av), ("Bras Gauche Poitrine", bras_g_poi),
        ("Bras Tete", bras_tete), ("Bras Droit Tete", bras_drt_tete),
        ("Bras Gauche Tete", bras_gch_tete), ("Bras Poitrine Total", bras_poi_tot)
    ]

    while True:
        print("\n--- MENU DE CONTROLE YANSHEE ---")
        for i, act in enumerate(actions):
            print("{:02d}. {}".format(i + 1, act[0]))
        print("Q. Quitter")

        start_time = time.time()
        choix = input("\nEntrez votre choix : ").strip().upper()
        attente = time.time() - start_time

        if choix == 'Q':
            break
        elif choix.isdigit():
            idx = int(choix) - 1
            if 0 <= idx < len(actions):
                act_nom, act_func = actions[idx]
                batt_avant = get_safe_battery()
                print("Execution de : {} (Batterie : {}%)".format(act_nom, batt_avant))
                try:
                    act_func()
                    batt_apres = get_safe_battery()
                    log_to_csv(act_nom, idx + 1, "Succes", 0, attente, batt_avant, batt_apres)
                except Exception as e:
                    log_to_csv(act_nom, idx + 1, "Echec", str(e), attente, batt_avant, get_safe_battery())
            else:
                print("Erreur: Numero invalide.")

    lib_yanshee.reset_robot()
    print("Robot reinitialise.")

if __name__ == "__main__":
    main()