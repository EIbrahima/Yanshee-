import os

DOSS_SYSTEME = "/opt/yanshee/lib/move/.hts_zh/"

def lister_et_jouer():
    if not os.path.exists(DOSS_SYSTEME):
        print("Erreur : Le dossier est introuvable.")
        return

    fichiers = [f for f in os.listdir(DOSS_SYSTEME) if f.lower().endswith(".mp3")]

    if not fichiers:
        print("Aucun fichier.mp3 trouve.")
        return

    print("\n--- Liste des musiques disponibles ---")
    for index, nom in enumerate(fichiers):
        print("{0} : {1}".format(index + 1, nom))

    try:
        saisie = input("\nEntrez le numero de la musique a lire : ")
        choix = int(saisie) - 1

        if 0 <= choix < len(fichiers):
            chemin_complet = os.path.join(DOSS_SYSTEME, fichiers[choix])
            print("Lecture en cours : " + fichiers[choix])

            # Utilisation de os.system à la place de subprocess
            os.system("sudo mpg123 " + chemin_complet)
        else:
            print("Numero invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    lister_et_jouer(