
## Présentation du Projet : Automatisation et Contrôle Yanshee

Ce dépôt centralise une série de scripts Python conçus pour le développement et le contrôle du robot Yanshee. L'objectif de cette collection est de permettre une gestion complète du robot, allant de la validation matérielle (servomoteurs) à l'implémentation de fonctionnalités avancées telles que la vision par ordinateur, la télémétrie de performance et l'interaction multimédia.

Ces outils ont été développés pour faciliter les phases de test, de débogage et d'exploitation autonome du robot dans des environnements académiques ou expérimentaux.


### Organisation des fonctionnalités

Les scripts sont classés par domaine d'application afin de faciliter leur maintenance et leur utilisation :

* **Test et Validation Matérielle (`Act_servo_moteurs.py`)** : Outil de diagnostic permettant de vérifier individuellement ou collectivement l'intégrité et le mouvement des 17 servomoteurs du robot.


* **Vision et Streaming (`Cam_seul.py`)** : Interface de vision par ordinateur permettant de diffuser le flux caméra en direct sur un serveur web local (port 5000) tout en exécutant des séquences de mouvement.


* **Contrôle Opérationnel et Télémétrie (`MOVE.py`)** : Module de pilotage complet offrant des mouvements pré-programmés. Il intègre une journalisation automatique des données (CSV) incluant le niveau de batterie, la luminosité ambiante et l'horodatage pour le suivi des performances.


* **Gestion Multimédia (`Music.py`)** : Interface de contrôle pour la lecture de fichiers audio au format `.mp3` stockés sur le système, facilitant l'ajout d'effets sonores aux interactions du robot.



Réalisé par Elhadj Ibrahima Diallo
Etudiant en Ingénierie informatique 
