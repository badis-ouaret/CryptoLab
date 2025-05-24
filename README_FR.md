## README (français)

### 🛠️ Instructions d'exécution de l'application :

1. Ouvrez un terminal ou une invite de commande (**cmd**) dans le répertoire du projet.
2. Exécutez la commande suivante :

   ```bash
   python3 app.py
   ```

📌 **Remarque** : Assurez-vous d'avoir installé la bibliothèque **CustomTkinter**.

---

### 🛍️ Fonctionnement général de l’application :

#### 🔹 Fenêtre principale :

* Choisissez la **méthode de chiffrement** à gauche grâce aux boutons radio.
* Sélectionnez l'**action** à effectuer (chiffrer / déchiffrer) via les boutons radio en haut.
* Saisissez votre texte dans le champ de gauche.
* Cliquez sur le bouton **"Chiffrer"** ou **"Déchiffrer"** selon l’action sélectionnée.
* Une **clé par défaut** sera utilisée si aucune n’est définie manuellement (voir plus bas pour la définition des clés).
* Le **résultat** apparaîtra dans le champ de droite.

---

### 🔑 Fenêtres de définition des clés :

* **César** : accepte uniquement des entiers entre **0 et 27**.
* **Vigenère** : n'accepte que des **mots sans espaces** ni **caractères spéciaux**.
* **César Amélioré** :

  * Chaque case représente une lettre majuscule.
  * **Aucune lettre ne doit être répétée.**
* **Polybe / Playfair** :

  * Définissez les **caractères jumelés** en partant de la gauche.
  * Entrez votre clé : **lettres majuscules uniquement**, **sans doublons**.
  * La **seconde lettre des couples jumelés est interdite** dans la clé.
  * Cliquez sur **"Aperçu"** pour visualiser la matrice.
* **Hill** :

  * Définissez la **taille de la matrice**.
  * Entrez les valeurs de votre clé.
  * ⚠️ La matrice doit être **inversible modulo 26**.
* **Affine** :

  * Entrez la **clé** et le **décalage**.
  * ⚠️ La clé doit être **inversible modulo 26**.
* **DES** :

  * Entrez une **clé binaire** de taille inférieure ou égale à **64 bits**.
  * Elle sera automatiquement **complétée par des zéros à gauche** si nécessaire.

📌 **Remarques** :

* Le bouton **"Effacer"** vide uniquement les champs, **sans réinitialiser les clés**.
* Pour réinitialiser une clé : cliquez d'abord sur **"Effacer"**, puis sur **"Valider"**.