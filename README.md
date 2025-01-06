# README - Fonctionnement de l'application

## Description
Ce projet comprend plusieurs composants qui interagissent pour simuler la création de tickets, les enregistrer dans une base de données Firestore, et tester le système avec un simulateur.

### Composants principaux :
1. **hookServer** : Le serveur qui reçoit les webhooks et les traite.
2. **petzi_simulator** : Simulateur pour envoyer des données à l'API du serveur.
3. **dashboard** : Frontend pour visualiser les données traitées.

## Prérequis

### 1. Installer les dépendances

#### Pour le backend (hookServer) :
Le projet utilise **Python** et les bibliothèques suivantes :

```bash
pip install flask firebase-admin
```

#### Pour le frontend (dashboard) :
Le projet utilise **Node.js** et **npm**. Pour installer les dépendances nécessaires, exécutez la commande suivante :

```bash
npm install
```

### Configuration Firebase

Pour configurer Firebase et permettre au serveur de se connecter à Firestore, suivez ces étapes :

1. Connectez-vous à [Firebase Console](https://console.firebase.google.com).
2. Sélectionnez le projet associé à votre application (par exemple : `urbanisation-c5b41`).
3. Accédez à **Paramètres du projet > Comptes de service**.
4. Cliquez sur **Générer une nouvelle clé privée** et téléchargez le fichier JSON.
5. Renommez le fichier téléchargé en : `urbanisation-c5b41-firebase-adminsdk-5d7y6-f6163c31f2.json`.
6. Placez ce fichier dans le répertoire : `hookServer\`.

Assurez-vous que le fichier n'est **pas committé** dans le dépôt en ajoutant cette ligne dans le fichier `.gitignore` :

```
hookServer/urbanisation-c5b41-firebase-adminsdk-5d7y6-f6163c31f2.json
```

Le serveur utilise ce fichier pour initialiser Firebase Admin SDK.

Exemple de code pour charger la clé dans `hookServer.py` :

```python
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('hookServer/urbanisation-c5b41-firebase-adminsdk-5d7y6-f6163c31f2.json')
firebase_admin.initialize_app(cred)
```

## 1. Hook Server

Le **hook server** est un serveur Flask qui reçoit les webhooks envoyés par le simulateur Petzi et les enregistre dans Firestore.

### Commande pour lancer le serveur :
```bash
python 'hookServer/hookServer.py'
```

### Fonctionnement :
- Le serveur écoute les requêtes POST sur `/webhook`.
- Il vérifie la signature HMAC envoyée dans l'en-tête `Petzi-Signature` pour valider la requête.
- Si la signature est correcte, il extrait les informations du webhook (création de ticket) et les enregistre dans Firestore sous la collection `tickets`.

### Détails techniques :
- Firebase est initialisé avec une clé de service JSON.
- Le serveur écoute sur le port 5000 avec Flask.
- L'événement traité est `ticket_created`.



## 2. Petzi Simulator

Le **petzi simulator** permet de simuler l'envoi de webhooks au serveur en générant des tickets avec des informations aléatoires.

### Commande pour lancer le simulateur :
```bash
python 'hookServer/petzi_simulator.py' "http://127.0.0.1:5000/webhook" "AEeyJhbGciOiJIUzUxMiIsImlzcyI6"
```

### Fonctionnement :
- Le simulateur génère des tickets avec des données aléatoires et les envoie au serveur.
- Il génère des dates de tickets selon une courbe exponentielle d'augmentation des ventes avant l'événement.
- La signature HMAC est incluse pour vérifier l'intégrité des données.

### Détails techniques :
- Les tickets contiennent des informations sur l'événement, la catégorie, le prix et l'acheteur.
- L'URL du webhook et le secret partagé sont passés en argument.

## 3. Dashboard

Le **dashboard** est l'interface frontend pour visualiser les tickets et les informations extraites par le serveur.

### Commande pour lancer le dashboard :
```bash
npm run dev
```

### Fonctionnement :
- Le frontend est développé avec Vue.js et Vite pour le développement.
- Il permet de visualiser les tickets enregistrés dans Firestore via des API.
- L'interface utilisateur est dynamique et affiche les données en temps réel.

### Détails techniques :
- Le backend Firestore est intégré pour récupérer et afficher les tickets dans le dashboard.

## Configuration requise :
- Python 3.x pour le serveur.
- Node.js et npm pour le dashboard.
- Firebase configuré avec les clés d'authentification.

## Conclusion :
Ce projet met en place un système complet pour traiter des tickets via un webhook, simuler des événements et visualiser les données dans un tableau de bord interactif.
