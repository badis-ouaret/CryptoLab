class WrongKeyException(Exception):
    def __init__(self, message = "Erreur dans le format de la clé"):
        super().__init__(message)

class DicoKeyAlradyExistException(Exception):
    def __init__(self):
        super().__init__("Chaque lettre ne doit correspondre qu'à une seule autre lettre !")

class DicoWrogKeyFormatException(Exception):
    def __init__(self):
        super().__init__("Le charactère doit être alphabetique et non accentué !")

class PlayfairCaractereJumleInCleException(Exception):
     def __init__(self):
        super().__init__("Les lettres jumlées ne doivent pas se trouver dans la clé")

class PlayfairCleTooShortException(Exception):
    def __init__(self):
        super().__init__("La cle doit avoir au moins 1 lettre ")


class PlayfairSameCaractereJumeException(Exception):
    def __init__(self):
        super().__init__("Les caracteres jumlés doivent être differents!")

class WrongFormatForCaractereJumleException(Exception):
    def __init__(self):
        super().__init__("Les caracteres jumlés doivent être des caractères alphabetiques differents (un seul caractère)")

class PolybeWrongTextException(Exception):
     def __init__(self):
        super().__init__("Le texte à déchifrer ne doit contenir que des chiffres(au nombres pair)")

class WrongTranspoCiferException(Exception):
    def __init__(self):
        super().__init__("Le texte fourni ne peut pas être déchiffré")

class WrongFormatForCaractereAddiException(Exception):
    def __init__(self):
        super().__init__("Le caractère de correction doit être un seul caracter alphabetique")


class WrongMatFormatException(Exception):
    def __init__(self,message = "Il y a un probleme avec les matrices"):
        super().__init__(message)
        
class ProduitMatImpossibleException(Exception):
    def __init__(self, message="Impossible d'effectuer le produit matriciel"):
        super().__init__(message)

class NumNonInversibleModNumException(Exception):
    def __init__(self, message = "Numero1 non inversible mod numero 2"):
        super().__init__(message)

class MatNonInversibleModNumException(Exception):
    def __init__(self, message = "La matrice n'est pas inversible mod numero"):
        super().__init__(message)

class KeyNotReadyException(Exception):
    def __init__(self, message = "La clé n'a pas encore été definie."):
        super().__init__(message)