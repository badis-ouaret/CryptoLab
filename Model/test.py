import unittest
from exceptions import WrongMatFormatException
from chiffreur import *





def test_transposition_chiffreur():
     print("=== Test de TranspositionChiffreur ===")
     try:
         # Création de l'instance du chiffreur par transposition
         transpo = TranspositionChiffreur()
        
         # Message à chiffrer (ici, on choisit un message dont la longueur est un multiple de 5,
        # sinon la méthode ajoute des 'X' pour le compléter)
         message = "Je vous parle d'un temps que les moins De ê%"  # 10 caractères => 2 lignes de 5 colonnes
         transpo.setKey([2,8,1,7,4,5,3,6,9])
         print("Message original :", message)
        
         # Chiffrement du message
         encrypted = transpo.chiffrer(message)
         print("Message chiffré  :", encrypted)
        
         # Déchiffrement du message chiffré
         decrypted = transpo.dechiffrer(encrypted)
         print("Message déchiffré :", decrypted)
       
     except Exception as e:
         print("Erreur dans TranspositionChiffreur :", e)
        
def test_ameliored_cesar():
     print("=== Test de AmelioredCesarChiffreur ===")
     try:
         # Création de l'instance
         ac = AmelioredCesarChiffreur()
         # Définir une clé de substitution valide (doit contenir toutes les lettres de A à Z)
         key_mapping = {
             "A": "D", "B": "E", "C": "F", "D": "G", "E": "H", "F": "I",
             "G": "J", "H": "K", "I": "L", "J": "M", "K": "N", "L": "O",
             "M": "P", "N": "Q", "O": "R", "P": "S", "Q": "T", "R": "U",
             "S": "V", "T": "W", "U": "X", "V": "Y", "W": "Z", "X": "A",
             "Y": "B", "Z": "C"
         }
         # Affecter la clé à l'instance (attention : dans votre code, c'est self.key utilisé, donc on l'assigne ici)
         ac.setKey(key_mapping)
         # Message à tester
         message = "HELLO WORLD"        
         encrypted = ac.chiffrer(message)        
         decrypted = ac.dechiffrer(encrypted)
         print("Message original :", message)
         print("Message chiffré  :", encrypted)
         print("Message déchiffré :", decrypted)
     except Exception as e:
         print("Erreur dans AmelioredCesarChiffreur :", e)
         
def main():
    # Instanciation de l'objet AffineChiffreur
    affine = AffineChiffreur()
    
    # Affichage de la clé par défaut
    print("Clé par défaut :", affine.getKey())
    print("Clé inverse mod 26 :", affine.cleInvMod26)
    
    # Définir une nouvelle clé (optionnel)
    try:
        affine.setKey(7, 3)  # Par exemple, clé=7 (doit être inversible modulo 26) et décalage=3
        print("\nNouvelle clé définie :", affine.getKey())
        print("Nouvelle clé inverse mod 26 :", affine.cleInvMod26)
    except Exception as e:
        print("Erreur lors de la définition de la nouvelle clé :", e)
    
    # Message à chiffrer/déchiffrer
    message_original = "Bonjour à tous aujourd'hui C'est le ramadan 2025 ê"
    print("\nMessage original :", message_original)
    
    # Chiffrement
    message_chiffre = affine.chiffrer(message_original)
    print("Message chiffré :", message_chiffre)
    
    # Déchiffrement
    message_dechiffre = affine.dechiffrer(message_chiffre)
    print("Message déchiffré :", message_dechiffre)
    # Instanciation de l'objet HillChiffreur avec la clé par défaut [[3,3],[2,5]]
    hill = HillChiffreur()
    
    # Optionnel : on peut redéfinir la clé (doit être une matrice carrée d'ordre >=2 et inversible)
    try:
        #nouvelle_cle = [[2,4,5], [9,2, 1],[3,17,7]]
        nouvelle_cle =[[3, 3], [2, 5]]
        hill.setKey(nouvelle_cle)
        # Clé attendue : [[3, 3], [2, 5]] (matrice 2x2)
        print("Clé définie avec succès :", hill.key)
    except Exception as e:
        print("Erreur lors de la définition de la clé :", e)
    
    # Message à chiffrer
    message_original = "Bejaia"
    # Message original attendu (sans accents et sans nombres) : "HELLO WORLD"
    print("\nMessage original :", message_original)
    
    # Test du chiffrement
    try:
        message_chiffre = hill.chiffrer(message_original)
        # Affichage du message chiffré (résultat dépend de l'implémentation de textToStringsArray, etc.)
        print("Message chiffré :", message_chiffre)
    except Exception as e:
        print("Erreur lors du chiffrement :", e)
    
    # Test du déchiffrement
    try:
        message_dechiffre = hill.dechiffrer(message_chiffre)
        # Le message déchiffré devrait être identique (ou très proche) au message original
        print("Message déchiffré :", message_dechiffre)
    except Exception as e:
        print("Erreur lors du déchiffrement :", e)


    # Test du chiffreur Playfair (basé sur une matrice)
        print("=== Test de PlayfairChiffreur ===")
    try:
          playfair = PlayfairChiffreur()
          # Définir la clé (ici, on utilise "ABCDE" avec "I" et "J" comme caractères jumelés)
          playfair.setCaracteresJumle(["I","J"])
          playfair.setMotCle("")
          playfair.setKey()       
          message = "Demaincestlegrandjour"        
          encrypted = playfair.chiffrer(message)
          decrypted = playfair.dechiffrer(encrypted)
          print("Message original :", message)
          print("Message chiffré  :", encrypted)
          print("Message déchiffré :", decrypted)
    except Exception as e:
          print("Erreur dans PlayfairChiffreur :", e)


    message = "il était une fois ûn imbecile qui voulait être heureux%"

     
    
    print("=== Test de CesarChiffreur ===")
    try:
          cesar = CesarChiffreur()
          cesar.setKey(3)
          print("Message original:", message)
          encrypted = cesar.chiffrer(message)
          print("Chiffré:", encrypted)
          decrypted = cesar.dechiffrer(encrypted)
          print("Déchiffré:", decrypted)
    except Exception as e:
          print("Erreur dans CesarChiffreur:", e)
         
    print("\n=== Test de VigenereChiffreur ===")
    try:
          vigenere = VigenereChiffreur()
          vigenere.setKey("dack")
          print("Clé utilisée:", vigenere.getKey())
          print("Message original:", message)
          encrypted = vigenere.chiffrer(message)
          print("Chiffré:", encrypted)
          decrypted = vigenere.dechiffrer(encrypted)
          print("Déchiffré:", decrypted)
    except Exception as e:
          print("Erreur dans VigenereChiffreur:", e)
          

    print("\n=== Test de PoybeChiffreur ===")
    try:
          poybre = PoybeChiffreur()
          # On utilise la clé par défaut (tableau complet de l'alphabet)
          poybre.setCaracteresJumle(["I","J"])
          poybre.setMotCle("Gymnastique")
          poybre.setKey()  # suppose que la méthode utilise list(string.ascii_uppercase) par défaut
          message = "Demain c'est le grand jour"       
          encrypted = poybre.chiffrer(message)       
          decrypted = poybre.dechiffrer(encrypted)
       
          print("Message original :", message)
          print("Message chiffré  :", encrypted)
          print("Message déchiffré :", decrypted)
    except Exception as e:
          print("Erreur dans PoybreChiffreur :", e)
        
test_transposition_chiffreur()


if __name__ == "__main__":
     main()