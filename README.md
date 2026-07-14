
## Présentation du Projet : Automatisation et Contrôle Yanshee

Ce dépôt centralise une série de scripts Python conçus pour le développement et le contrôle du robot Yanshee. L'objectif de cette collection est de permettre une gestion complète du robot, allant de la validation matérielle (servomoteurs) à l'implémentation de fonctionnalités avancées telles que la vision par ordinateur, la télémétrie de performance et l'interaction multimédia.

Ces outils ont été développés pour faciliter les phases de test, de débogage et d'exploitation autonome du robot dans des environnements académiques ou expérimentaux.


### Organisation des fonctionnalités

Les scripts sont classés par domaine d'application afin de faciliter leur maintenance et leur utilisation :

* **Test et Validation Matérielle (`Act_servo_moteurs.py`)** : Outil de diagnostic permettant de vérifier individuellement ou collectivement l'intégrité et le mouvement des 17 servomoteurs du robot.


* **Vision et Streaming (`Cam_seul.py`)** : Interface de vision par ordinateur permettant de diffuser le flux caméra en direct sur un serveur web local (port 5000) tout en exécutant des séquences de mouvement.


* **Contrôle Opérationnel et Télémétrie (`MOVE.py`)** : Module de pilotage complet offrant des mouvements pré-programmés. Il intègre une journalisation automatique des données (CSV) incluant le niveau de batterie, la luminosité ambiante et l'horodatage pour le suivi des performances.


* **Gestion Multimédia (`Music.py`)** : Interface de contrôle pour la lecture de fichiers audio au format `.mp3` stockés sur le système, facilitant l'ajout d'effets sonores aux interactions du robot.


Ce fichier `donnees.xlsx` est essentiel pour l'analyse de vos expérimentations. Voici comment l'intégrer dans la présentation de votre dépôt :

---

### Analyse de Données et Historique (`donnees.xlsx`)

Ce fichier constitue la base de données consolidée des performances du robot. Il centralise les logs générés par le script `MOVE.py` pour permettre une analyse approfondie des interactions robotiques.

* **Structure des données** : Il contient un historique détaillé des exécutions, incluant :
* **Horodatage (`timestamp`)** : Date et heure précises de chaque action.
* **Indicateurs d'environnement** : Mesures de la luminosité ambiante (`lumiere`) lors de l'exécution.
* **Performance énergétique** : Suivi de l'état de la batterie avant (`batt_avant`) et après (`batt_apres`) chaque séquence de mouvement.
  
* **Diagnostic** : Statut de réussite (`resultat`) et codes d'erreur associés, ainsi que le temps de latence utilisateur (`attente`).


* **Rôle** : Ce fichier est indispensable pour évaluer l'efficacité énergétique du robot, corréler les succès d'actions aux conditions lumineuses, et auditer les temps de réponse système au fil de vos tests.

---


Vous pouvez ajouter cette section à la suite de la liste des scripts pour montrer que votre projet gère non seulement l'action, mais aussi le **suivi analytique** des performances.

* **Analyse de Données et Historique (donnees.xlsx)**
Ce fichier constitue la base de données consolidée des performances du robot. Il centralise les logs générés par le script MOVE.py pour permettre une analyse approfondie des interactions robotiques.

* **Structure des données** : Il contient un historique détaillé des exécutions, incluant :

*Horodatage (timestamp)* : Date et heure précises de chaque action.

**Indicateurs d'environnement**: Mesures de la luminosité ambiante (lumiere) lors de l'exécution.

**Performance énergétique** : Suivi de l'état de la batterie avant (batt_avant) et après (batt_apres) chaque séquence de mouvement.

**Diagnostic** : Statut de réussite (resultat) et codes d'erreur associés, ainsi que le temps de latence utilisateur (attente).

* **Rôle** : Ce fichier est indispensable pour évaluer l'efficacité énergétique du robot, corréler les succès d'actions aux conditions lumineuses, et auditer les temps de réponse système au fil de vos tests.



Réalisé par Elhadj Ibrahima Diallo
Etudiant en Ingénierie informatique 
