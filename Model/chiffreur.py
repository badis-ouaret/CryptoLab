from abc import ABC,abstractmethod
from exceptions import *
import string
from calculMatriciel import * 

class Chiffreur(ABC):
    
    @abstractmethod
    
    def verifyKey(self):
        pass
    
    @abstractmethod
    def setKey(self):
        pass
    
    @abstractmethod
    def getKey(self):
        pass
    
    @abstractmethod
    def chiffrer(self,message):
        pass
    
    @abstractmethod
    def dechiffrer(self,message):
        pass
    @staticmethod
    def permuter(A,B):
        temp = A
        A = B
        B = temp
        
    def textToStringsArray(self,text):
        strings = []
        mot = ""
        
        for char in text: 
                       
            if char.isalpha() :
                mot +=char
            else:
                if len(mot)>0 :
                    strings.append(mot)
                mot = ""
        if len(mot)>0:
          strings.append(mot)
        return strings
    
    def textToStringsArray2(self,text):
        strings = []
        mot = ""
        
        for char in text: 
                       
            if char.isnumeric() :
                mot +=char
            else:
                if len(mot)>0 :
                    strings.append(mot)
                mot = ""
        if len(mot) :
            strings.append(mot)
        return strings
    def stringArrayToText(self,strings):
        textF = ""
        for string in strings:
            textF +=string+" "
        return textF
              
    
    @staticmethod
    def supprime_accents_nombres(messages):
        chaine = ""
        for char in messages:
            if char.isalpha() and char.isascii():
                chaine += char
            elif char.isalpha():
                
                if ord(char) in range(192,198) or ord(char) in range (224,230):
                    chaine +="A" if char.isupper() else "a"
                elif ord(char) == 199 or ord(char) == 231:
                    chaine +="C"  if char.isupper() else "c"
                elif ord(char) in range(232,236) or ord(char) in range(200,204):
                    chaine +="E"  if char.isupper() else "e"
                elif ord(char) in range(204,208) or ord(char) in range(236,240):
                    chaine +="I"  if char.isupper() else "i"
                elif ord(char) == 208 or ord(char) == 240:
                    chaine +="D"  if char.isupper() else "d"
                elif ord(char) == 209 or ord(char) == 241:
                    chaine +="N"  if char.isupper() else "n"
                elif ord(char) in range(210,215) or ord(char) in range(242,47):
                    chaine +="O"  if char.isupper() else "o"
                elif ord(char) in range(217,221) or ord(char) in range(249,253):
                    chaine +="U"  if char.isupper() else "u"
                elif ord(char) in range(253,256) or ord(char) == 221 :
                    chaine +="Y"  if char.isupper() else "y"
            elif char.isnumeric():
                chaine +=""
            else:
                chaine +=" "               
            
                
        return chaine
    @staticmethod
    def supprime_accents(messages):
        chaine = ""
        for char in messages:
            if char.isalpha() and char.isascii():
                chaine += char
            elif char.isalpha():
                
                if ord(char) in range(192,198) or ord(char) in range (224,230):
                    chaine +="A" if char.isupper() else "a"
                elif ord(char) == 199 or ord(char) == 231:
                    chaine +="C"  if char.isupper() else "c"
                elif ord(char) in range(232,236) or ord(char) in range(200,204):
                    chaine +="E"  if char.isupper() else "e"
                elif ord(char) in range(204,208) or ord(char) in range(236,240):
                    chaine +="I"  if char.isupper() else "i"
                elif ord(char) == 208 or ord(char) == 240:
                    chaine +="D"  if char.isupper() else "d"
                elif ord(char) == 209 or ord(char) == 241:
                    chaine +="N"  if char.isupper() else "n"
                elif ord(char) in range(210,215) or ord(char) in range(242,47):
                    chaine +="O"  if char.isupper() else "o"
                elif ord(char) in range(217,221) or ord(char) in range(249,253):
                    chaine +="U"  if char.isupper() else "u"
                elif ord(char) in range(253,256) or ord(char) == 221 :
                    chaine +="Y"  if char.isupper() else "y"
            
            else:
                chaine +=char               
            
                
        return chaine
    
class DecalageChiffreur(ABC):
        
    
    def chiffrerLettreDecalage(self,lettre,decalage):
        base = ord('A') if lettre.isupper() else  ord('a')
        return chr((ord(lettre) - base + decalage +1) % 26 + base)
        
    
    def dechiffrerLettreDecalage(self,lettre,decalage):
        base = ord('A') if lettre.isupper() else  ord('a')
        return chr((ord(lettre) - base - decalage -1) % 26 + base)

    


    


class CesarChiffreur(Chiffreur,DecalageChiffreur):
    def __init__(self):
        super().__init__()
        self.key = 3
    
    def initialiser(self):
        self.key = 3

    def setKey(self,key=3):
        if isinstance(key,int):
            self.key = key
        else:
            raise WrongKeyException()
        
    def getKey(self):
        return self.key

    def verifyKey(self,key):
        if(isinstance(key, int)):
            return True
        else:
            return False
    
    def chiffrer(self,message):
        if self.verifyKey(self.key) :
            resultat = ""
            message = Chiffreur.supprime_accents(message)
            for caractere in message:
                if caractere.isalpha() and caractere.isascii():
                    
                    resultat += self.chiffrerLettreDecalage(caractere,self.key-1)
                else:
                    resultat += caractere
            return resultat
        else:
            raise WrongKeyException()
    
    def dechiffrer(self,message):
        if self.verifyKey(self.key) :
            resultat = ""
            message = Chiffreur.supprime_accents(message)
            for caractere in message:
                if caractere.isalpha():
                    resultat += self.dechiffrerLettreDecalage(caractere,self.key-1)
                else:
                    resultat += caractere
            return resultat
        else:
            raise WrongKeyException()
class VigenereChiffreur(Chiffreur,DecalageChiffreur):

    def __init__(self):
        super().__init__()
        self.key = "Badis"
    
    def initialiser(self):
        self.key = "Badis"


    def setKey(self,key):
        if self.verifyKey(key):
            self.key = key
        else:
            raise WrongKeyException("La clé ne doit contenir que des caractères alphabétiques")
    def getKey(self):
        return self.key

    def verifyKey(self,key):
        if(key.isalpha() and key.isascii()):
            return True
        else:
            return False
    
    def chiffrer(self,message):
        if self.verifyKey(self.key) :
            message = Chiffreur.supprime_accents(message)
            self.key = self.key.upper()
            resultat = ""
            i = -1
            for caractere in message:
                if caractere.isalpha() and caractere.isascii():
                    i+=1
                    resultat += self.chiffrerLettreDecalage(caractere,ord(self.key[i% len(self.key)]) - ord('A') )
                   
                else:
                    resultat += caractere
            return resultat
        else:
            raise WrongKeyException("La clé ne doit contenir que des caractères alphabétiques")
     
    def dechiffrer(self,message):
        if self.verifyKey(self.key) :
            message = Chiffreur.supprime_accents(message)
            self.key = self.key.upper()
            resultat = ""
            i = -1
            for caractere in message:
                if caractere.isalpha() and caractere.isascii():
                    i+=1
                    resultat += self.dechiffrerLettreDecalage(caractere,(ord(self.key[i% len(self.key)]) - ord('A')) )
                else:
                    resultat += caractere
            return resultat
        else:
            raise WrongKeyException("La clé ne doit contenir que des caractères alphabétiques")
        
class AmelioredCesarChiffreur(Chiffreur):

    def __init__(self):
        super().__init__()
        self.dico = {} # la cle
        self.cleReady = False
    
    def initialiser(self):
        self.dico = {} # la cle
        self.cleReady = False
        

    def setKey(self,cle):
        if self.verifyKey(cle):
            self.dico  = cle
            self.cleReady = True
    
    def getKey(self):
        return self.dico
            

    
    def contient_toutes_les_lettres(self,key = {}):
        alphabet = set(string.ascii_lowercase)  # Ensemble des lettres de 'a' à 'z'
        cles_dico = {cle.lower() for cle in key.keys()}  # Ensemble des clés du dictionnaire
        return alphabet.issubset(cles_dico)  # Vérifier si toutes les lettres sont présentes

    
    def ajouter_si_absent(self,key,cle,valeur): # key -> dico cle -> lettreEtréeParLutilisateur valeur -> lettre proposée par linterface
        self.cleReady = False
        if not cle.isalpha() or not cle.isascii() :
            raise DicoWrogKeyFormatException()
        if cle not in key :
            key[cle.upper()] = valeur.upper()
            return True  # Ajout réussi
        else:
            raise DicoKeyAlradyExistException()  # Clé déjà existante

    
    def verifyKey(self,key={}):
        
        if self.contient_toutes_les_lettres(key) :           
            return True
        return self.cleReady
           
    
    def dechiffrer(self,message):
        if self.verifyKey(self.dico):
            chaine = ""
            message = Chiffreur.supprime_accents(message)
            for char in message:
                if char.isalpha() and char.isascii():
                    chaine += self.dico.get(char) if char.isupper() else self.dico.get(char.upper()).lower()
                else:
                    chaine += char
            return chaine
        else:
            raise WrongKeyException("Vous devez faire correspondre chaque lettre de l'alphabet à une autre lettre.")
    
    def chiffrer(self,message):
       
        if self.verifyKey(self.dico):
           
            chaine = ""
            message = Chiffreur.supprime_accents_nombres(message)
            
            for char in message:
                
                if char.isalpha() and char.isascii():
                    cle_trouvee = next((cle for cle, valeur in self.dico.items() if valeur == (char.upper() if not char.isupper() else char)), None)
                    if char.isupper():
                        chaine += cle_trouvee
                    else:
                        chaine += cle_trouvee.lower()
                else:
                    chaine += char
            return chaine
        else:
            raise WrongKeyException("Vous devez faire correspondre chaque lettre de l'alphabet à une autre lettre.")


class MatriceChiffreur(ABC):

    def __init__(self):
        self.LIGNES = 5
        self.COLONNES = 5
        self.matrice =[["A"] * self.COLONNES for _ in range(self.LIGNES)] 
        self.cleReady = False
        self.caracteresJumle = ["I","J"]
        self.motCle = "ABCDE"

    def initialiser(self):
        self.LIGNES = 5
        self.COLONNES = 5
        self.matrice =[["A"] * self.COLONNES for _ in range(self.LIGNES)] 
        self.cleReady = False
        self.caracteresJumle = ["I","J"]
        self.motCle = "ABCDE"

    def setMotCle(self,mot = "ABCDE"): 
        if not isinstance(mot,str):
            raise WrongKeyException()
        
        if len(mot)<1:
            mot = "A"     

        for char in mot:
            if not char.isalpha() or not char.isascii():
                raise WrongKeyException()

         
        self.motCle = mot.upper()
        
        
    def verifyKey(self):
        return True
    
    def setCaracteresJumle(self,carac = ["I","J"]):
               
        if not isinstance(carac[0],str) or not isinstance(carac[1],str) or not carac[0].isalpha() or not carac[1].isalpha():
            raise WrongFormatForCaractereJumleException()
        if len(carac[0]) != 1 and len(carac[1]) !=1:
            raise WrongFormatForCaractereJumleException()
        if carac[0] == carac[1]:
            raise PlayfairSameCaractereJumeException()
        carac[0] = carac[0].upper()
        carac[1] = carac[1].upper()
        
       
        if ord(carac[0])>ord(carac[1]):
            Chiffreur.permuter(carac[0],carac[1])


        self.caracteresJumle =carac


    def trouverCoordonéesLettre(self,cible):
        if self.verifyKey():
            return next(((i, j) for i, ligne in enumerate(self.matrice) for j, valeur in enumerate(ligne) if valeur == cible), None)
        else:
            return (-1,-1)

    


    def definirCle(self):            
         
        liste = []
        index = 0
        for char in self.motCle:  
            if char ==  self.caracteresJumle[1]:
                char = self.caracteresJumle[0]            
            if char not in liste:
                liste.append(char)           
                
        alphabet = ord("A")
        prisDansCle = 0
        for i in range(self.LIGNES):
            j=0
            while( j < self.COLONNES):
                if(prisDansCle < len(liste)):
                    self.matrice[i][j] = liste[prisDansCle]
                    prisDansCle +=1                            
                    j+=1
                elif chr(alphabet) not in liste and chr(alphabet) != self.caracteresJumle[1]:
                    self.matrice[i][j] = chr(alphabet)                        
                    j+=1
                    alphabet +=1
                else:                            
                    alphabet +=1
        self.cleReady = True  
        
        
     



class PlayfairChiffreur(Chiffreur,MatriceChiffreur):
    def __init__(self):
        super().__init__()         
        self.caracterAddi = "X"  

    def initialiser(self):
        super().initialiser()
        self.caracterAddi="X"     
       
    def setCaracterAddi(self,carac = "X"):
        if not isinstance(carac,str) or not carac.isalpha() :
            raise WrongFormatForCaractereAddiException()
        if len(carac) !=1:
            raise WrongFormatForCaractereAddiException()
        carac= carac.upper()
        self.caracterAddi = carac

    

    def definirCle(self):            
        if self.caracteresJumle[1]== self.caracterAddi :
            Chiffreur.permuter(self.caracteresJumle[0],self.caracteresJumle[1])       
        super().definirCle()  
        
    def setKey(self):
         self.definirCle()
    
    def getKey(self):
        if self.cleReady :
            return self.matrice          
        else:
            raise KeyNotReadyException()
                              

    def verifyKey(self):
        return self.cleReady
    
    
        
   
    
    def chiffrer(self,text):
        if self.verifyKey():
            
            
            mots = self.textToStringsArray(text)
            
            textF = ""
            for messageF in mots:
                
                message = messageF
                chaine=""
                message = Chiffreur.supprime_accents_nombres(message)
                messagetmp = ""
                for char in message:
                    if char == self.caracteresJumle[1].upper() or char == self.caracteresJumle[1].lower():
                        messagetmp+=self.caracteresJumle[0]
                    else:
                        messagetmp+=char
                message = messagetmp
                messagetmp = message[0]
                for i in range(len(message)-1):                    
                    if message[i] == message[i+1]:
                        messagetmp+=self.caracterAddi+message[i+1]
                    else:
                        messagetmp += message[i+1]
                message = messagetmp                
                if len(message) % 2 != 0:
                    message+=self.caracterAddi
               
                for i in range(0,len(message)-1,2):
                    
                    if message[i].isalpha() and message[i+1].isascii and message[i+1].isalpha() and message[i].isascii:
                        
                        cord1x,cord1y = self.trouverCoordonéesLettre(message[i].upper())
                        cord2x,cord2y = self.trouverCoordonéesLettre(message[i+1].upper())
                        
                        if cord1x == cord2x : 
                            chaine += self.matrice[cord1x][(cord1y+1)%5]+self.matrice[cord2x][(cord2y+1)%5]
                        elif cord1y == cord2y :
                            chaine += self.matrice[(cord1x+1)%5][cord1y]+self.matrice[(cord2x+1)%5][cord2y]
                        else:
                            chaine += self.matrice[cord1x][cord2y]+self.matrice[cord2x][cord1y]
                        
                textF += chaine+" "            
            return textF
                    

        else:
            raise KeyNotReadyException()
        

    def dechiffrer(self,text):
        if self.verifyKey():
            
            
            mots = self.textToStringsArray(text)
            
            textF = ""
            for messageF in mots:
                
                message = messageF
                chaine=""
                message = Chiffreur.supprime_accents_nombres(message)
                             
               
               
                for i in range(0,len(message)-1,2):
                    
                    if message[i].isalpha() and message[i+1].isascii and message[i+1].isalpha() and message[i].isascii:
                        
                        cord1x,cord1y = self.trouverCoordonéesLettre(message[i].upper())
                        cord2x,cord2y = self.trouverCoordonéesLettre(message[i+1].upper())
                        
                        if cord1x == cord2x : 
                            chaine += self.matrice[cord1x][(cord1y-1)%5]+self.matrice[cord2x][(cord2y-1)%5]
                        elif cord1y == cord2y :
                            chaine += self.matrice[(cord1x-1)%5][cord1y]+self.matrice[(cord2x-1)%5][cord2y]
                        else:
                            chaine += self.matrice[cord1x][cord2y]+self.matrice[cord2x][cord1y]
                        
                textF += chaine+" "    
                       
            return textF
                    

        else:
            raise KeyNotReadyException()
        
    


class PoybeChiffreur(Chiffreur,MatriceChiffreur):
    def __init__(self):
        super().__init__()
    
    

    def verifyKey(self):
        return self.cleReady 
    
    def setKey(self):
        super().definirCle()  
    
    def getKey(self):
        if self.cleReady :
            return self.matrice          
        else:
            raise KeyNotReadyException()


    def chiffrer(self, message):
        if self.verifyKey():
            chaine = ""
            message = Chiffreur.supprime_accents_nombres(message)
            
            for char in message:
                
                if char.isalpha() and char.isascii():
                    
                    if self.caracteresJumle[1].upper() == char.upper():
                        
                        cordx,cordy = self.trouverCoordonéesLettre(self.caracteresJumle[0].upper())
                    else:
                        cordx,cordy = self.trouverCoordonéesLettre(char.upper())
                                            
                    chaine  +=str(cordx)+str(cordy)
                    
                else:
                    chaine += " "
            return chaine
        else:
            raise KeyNotReadyException()
    
    def dechiffrer(self, texte):
        if self.verifyKey():
            strings = self.textToStringsArray2(texte)
            
            texteF = ""
            for messageF in strings:
                message = messageF
                if not message.isnumeric() or len(message)%2 != 0:
                    raise PolybeWrongTextException()
                chaine = "" 
                    
                for i in range(0,len(message)-1,2):    
                                    
                    chaine +=self.matrice[int(message[i])][int(message[i+1])]
                texteF +=chaine+" "
            return texteF
                
        else:
            raise KeyNotReadyException()
        
class TranspositionChiffreur(Chiffreur):
    def __init__(self):
        super().__init__()
        self.key = [3,1,4,5,2]
        self.COLLONES = 5
    
    def initialiser(self):
        self.key = [3,1,4,5,2]
        self.COLLONES = 5

        
    def verifyKey(self,key):
        return set(key).issubset(set([i for i in range(1, len(key) + 1)]))
    
    def setKey(self,key):
        if self.verifyKey(self.key):
            self.key= key
            self.COLLONES = len(key)
        else :
            raise WrongKeyException()
    def getKey(self):
        return self.key
    
    def recupererIndElementDansCle(self,cible):
        if self.verifyKey(self.key):
            return next((i for i, val in enumerate(self.key)  if val == cible), None)
        else:
            raise WrongKeyException()
    
    def chiffrer(self, message):
        if self.verifyKey(self.key):
            while(len(message)%self.COLLONES !=0 ):
                message +="x"
            chaine = ""
            matrice =[["X"] * self.COLLONES for _ in range(int(len(message)/self.COLLONES))]
            index = 0
            for i in range(int(len(message)/self.COLLONES)):
                for j in range(self.COLLONES):
                    matrice[i][j] = message[index]  
                    index +=1     
            for i in range(self.COLLONES):
                for j in range(int(len(message)/self.COLLONES)):
                    chaine += matrice[j][self.key[i]-1]
            
            return chaine
        else:
            raise WrongKeyException()
    
    

    
    def dechiffrer(self, message):
        if self.verifyKey(self.key):
            if len(message)%self.COLLONES !=0 :
                raise WrongTranspoCiferException()
            
            chaine = ""
            matrice =[["X"] * self.COLLONES for _ in range(int(len(message)/self.COLLONES))]
            index = 0
            for i in range(self.COLLONES):
                for j in range(int(len(message)/self.COLLONES)):
                    matrice[j][i] = message[index] 
                    index +=1      
            for i in range(int(len(message)/self.COLLONES)):
                j = 1
                while(j <=self.COLLONES):            
                    index = self.recupererIndElementDansCle(j)
                    chaine += matrice[i][index]
                    j +=1
            
            return chaine
        else:
            raise WrongKeyException()
        


class HillChiffreur(Chiffreur):
    def __init__(self):
        super().__init__()
        self.key = [[3,3], [2,5]]# autre possiblité [2,4,5], [9,2, 1],[3,17,7]
        self.keyLin = 2
        self.keyCol = 2
        self.keyDet = 9
        self.keyInversMod26 = [[15,17],[20,9]]
        
    def initialiser(self):
        self.key = [[3,3], [2,5]]# autre possiblité [2,4,5], [9,2, 1],[3,17,7]
        self.keyLin = 2
        self.keyCol = 2
        self.keyDet = 9
        self.keyInversMod26 = [[15,17],[20,9]]

           
    def setKey(self,cle=[[3,3], [2,5]]):        
        if self.verifyKey(cle):           
            self.key= cle 
            self.keyLin,self.keyCol = CalculMatriciel.dimentionsMat(self.key)            
            self.keyDet = CalculMatriciel.detMat(self.key)
            self.keyInversMod26 = CalculMatriciel.calculMatInversModNum(self.key,26)
        else:
            raise WrongKeyException()
    
    def getKey(self):
        return self.key   
                  
    
    def verifyKey(self,cle):
        yes = True
        if not CalculMatriciel.matIsCarree(cle) and CalculMatriciel.dimentionColMat(cle) >=2 and CalculMatriciel.dimentionLinMat(cle)>=2:
            yes = False
            raise WrongMatFormatException("La clé doit etre une matrice carrée d'ordre superieur ou egal à 2")   
        
        if not CalculMatriciel.matIsInversibleModNum(cle,26):  
            yes =False        
            raise WrongMatFormatException("La matrice clé doit être inversible modulo 26") 
        
        return yes
    
    def motsMultipleCleCol(self,strings):
        strings2=[]
        for string in strings:
            chaineTemp = string.upper()
            while len(chaineTemp) % self.keyCol != 0:
                chaineTemp +="X"
            strings2.append(chaineTemp)
        return strings2
    
    def motsToStringOfOrdChar(self,strings2):
        strings = []
        for string in strings2:
            chaineTemp=""             
            for char in string:
                numChar = ord(char.upper()) - ord("A")
                if numChar in range(0,10):
                    chaineTemp +="0"+str(numChar)
                else:
                    chaineTemp +=str(numChar)
            strings.append(chaineTemp)
        return strings
    
    def stringOfOrdCharListToStringOfCharListWithEncrypt(self,strings):#coeur du chiffrement
        mat = CalculMatriciel.initialiseMat(self.keyCol,1)       
        strings2=[]
        for string in strings: 
            index = 0
            chaineTemp =""
            while index < (len(string)-1):           
                for i in range(self.keyCol):
                                     
                    mat[i][0] = int(string[index]+string[index+1])                  
                    index +=2
                matchif = CalculMatriciel.produitMatriciel(self.key,mat)
                matchif = CalculMatriciel.modMatNum(matchif,26)
                
                matchif = CalculMatriciel.addValToMat(matchif,ord("A"))                               
                for i in range(self.keyCol):                    
                    chaineTemp +=chr(int(matchif[i][0]))
            strings2.append(chaineTemp)
        return strings2
    
    def stringOfOrdCharListToStringOfCharListWithDecrypt(self,strings):#coeur du dechiffrement
        
        
        mat = CalculMatriciel.initialiseMat(self.keyCol,1)                       
        strings2=[]
        for string in strings: 
            index = 0
            chaineTemp =""
            
            while index < (len(string)-1): 
                         
                for i in range(self.keyCol):                    
                    mat[i][0] = int(string[index]+string[index+1])                    
                    index +=2
                matchif = CalculMatriciel.produitMatriciel(self.keyInversMod26,mat)
                matchif = CalculMatriciel.modMatNum(matchif,26)
                matchif = CalculMatriciel.addValToMat(matchif,ord("A"))
                for i in range(self.keyCol):                    
                    chaineTemp +=chr(int(matchif[i][0]))
            strings2.append(chaineTemp)
        return strings2
                

    def chiffrer(self, message):        
        message = Chiffreur.supprime_accents_nombres(message)
        strings = self.textToStringsArray(message)    
        strings = self.motsMultipleCleCol(strings)        
        strings = self.motsToStringOfOrdChar(strings)                  
        strings = self.stringOfOrdCharListToStringOfCharListWithEncrypt(strings)            
        return self.stringArrayToText(strings)
    
    
    def dechiffrer(self, message):
        
        message = Chiffreur.supprime_accents_nombres(message)
        strings = self.textToStringsArray(message)        
        strings = self.motsMultipleCleCol(strings)        
        strings = self.motsToStringOfOrdChar(strings)  
        strings = self.stringOfOrdCharListToStringOfCharListWithDecrypt(strings)            
        return self.stringArrayToText(strings)
 
class AffineChiffreur(Chiffreur):
    def __init__(self):
        super().__init__()
        self.key = [5,8]
        self.cleInvMod26 = CalculMatriciel.numInversModNum(self.key[0],26)
    
    def initialiser(self):
        self.key = [5,8]
        self.cleInvMod26 = CalculMatriciel.numInversModNum(self.key[0],26)

        
    def verifyKey(self,cle):
        if CalculMatriciel.numInversibleModNum(cle[0],26) and isinstance(cle[1],int)and isinstance(cle[0],int):
            return True
        else:
            raise WrongKeyException("La clé doit avoir deux entier (clé,décalage) tel que clé est inversible mod 26 !")
        
    def setKey(self,cleInvMod26 = 5,decalage= 8):
        if self.verifyKey([cleInvMod26,decalage]):
            self.key = [cleInvMod26,decalage]
            self.cleInvMod26 = CalculMatriciel.numInversModNum(self.key[0],26)
            
    def getKey(self):
        return self.key
    
    def chiffrerLettre(self,lettre):
        base = ord('A') if lettre.isupper() else ord('a')
        
        return chr((self.key[0]*(ord(lettre)-base) + self.key[1])%26 + base)
        
        
        
    def dechiffrerLettre(self,lettre):
        base = ord('A') if lettre.isupper() else ord('a')        
        return chr((self.cleInvMod26*((ord(lettre)-base) - self.key[1]))%26 + base)
    
    def chiffrer(self, message):
        message = self.supprime_accents(message)
        textF =""        
        for char in message:
            if char.isalpha()and char.isascii():
                
                textF += self.chiffrerLettre(char)
                
            else:
                textF+=char
        return textF
            
        
    def dechiffrer(self, message):
        message = self.supprime_accents(message)
        textF =""        
        for char in message:
            if char.isalpha()and char.isascii():
                textF += self.dechiffrerLettre(char)
            else:
                textF+=char
        return textF
    
    

class DesChiffreur(Chiffreur):
    

    def __init__(self):
        super().__init__()
        self.key = "0000000000000000000000000000000000000000000000000000000000000000"
        self.tabKeys = []

    def initialiser(self):
        self.key = "0000000000000000000000000000000000000000000000000000000000000000"
        self.tabKeys = []
        
    def verifyKey(self,cle):
        if isinstance(cle,str) and len(cle) ==64 and cle.isdigit() and cle.isascii():
            return True
        else:
            raise WrongKeyException("La clé doit être en binaire et avoir 64 bits")
        
    def tabKeysReady(self):
        if len(self.tabKeys) == 16:
            return True
        return False
            
    def setKey(self,cle):
        if self.verifyKey(cle):
            self.key = cle
            cle =self.pC_1(cle)#fonction permuted choice 1
            for i in range(16):
                cle = self.shiftLeft(i,cle)
                self.tabKeys.append(self.pC_2(cle))
            
    def getKey(self):
        return self.key
    def getTabKeys(self):
        if self.tabKeysReady():
            return self.tabKeys
        else:
            raise KeyNotReadyException("Les clés ne sont pas prêtes")
        
    def pC_1(self,cle):
        # Permutation de la clé selon le tableau PC-1
        permuted_key = ""
        pc1 = [57, 49, 41, 33, 25, 17, 9, 1,
               58, 50, 42, 34, 26, 18, 10, 2,
               59, 51, 43, 35, 27, 19, 11, 3,
               60, 52, 44, 36, 63, 55, 47, 39,
               31, 23, 15, 7, 62, 54, 46, 38,
               30, 22, 14, 6, 61, 53,45 ,37,
               29 ,21 ,13 ,5 ,28 ,20 ,12 ,4]
        for i in pc1:
            permuted_key += cle[i-1]
        return permuted_key
    def pC_2(self,cle):
        # Permutation de la clé selon le tableau PC-2
        permuted_key = ""
        pc2 = [14, 17, 11, 24, 1,  5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]
       
        for i in pc2:
            permuted_key += cle[i-1]
        return permuted_key
    
    def shiftLeft(self,index,cle):
        # Décalage à gauche de la clé
        right = cle[28:]
        left = cle[0:28]
        if index == 0 or index == 1 or index == 8 or index == 15:
            left = left[1:] + left[0]
            right = right[1:] + right[0]
        else:
            left = left[2:] + left[0:2]
            right = right[2:] + right[0:2]
        return left + right
    
    def iP(self,message):
        # Permutation initiale
        permuted_message = ""
        ip = [
                58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17,  9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7
            ]

        for i in ip:
            permuted_message += message[i-1]
        return permuted_message
    
    def iIP(self,message):
        # Permutation inverse initiale
        permuted_message = ""
        ip = [
                40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25
        ]
        for i in ip:
            permuted_message += message[i-1]
        return permuted_message
    
    def swap32(self,message):
        # Échange des 32 premiers bits avec les 32 derniers bits
        return message[32:] + message[:32]

    def round(self,message,key):
        # Fonction de round
        left = message[:32]
        right = message[32:]
        right_expanded = self.eExpansion(right)
        right_expanded = self.xor(right_expanded, key)
        right_expanded = self.sBox(right_expanded)
        right_expanded = self.pBox(right_expanded)
        xor_result2 = self.xor(left, right_expanded)
        return right + xor_result2
    
    def eExpansion(self, message):
        # Expansion de la moitié droite
        expanded_message = ""
        e = [
               32, 1, 2, 3, 4, 5,
                4, 5, 6, 7, 8, 9,
                8, 9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32, 1
            ]
        for i in e:
            expanded_message += message[i-1]
        return expanded_message
    
    def sBox(self,message):

        # S1
        s1 =[
            [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
        ]
        # S2
        s2 = [
            [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
        ]
        # S3
        s3 = [
            [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
        ]
        # S4
        s4 = [
            [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
        ]
        # S5
        s5 = [
            [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        ]
        # S6
        s6 = [
            [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
            [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
        ]
        # S7
        s7 = [
            [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
        ]
        # S8
        s8 = [
            [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
        ]
        s_boxes = [s1, s2, s3, s4, s5, s6, s7, s8]

        nombres6bitsStr = [message[i:i+6] for i in range(0, len(message), 6)]
        lines = [int(n[0] + n[5], 2) for n in nombres6bitsStr]
        columns = [int(n[1:5], 2) for n in nombres6bitsStr]
        return "".join(bin(s_boxes[i][l][c])[2:].zfill(4) for i, (l, c) in enumerate(zip(lines, columns)))

        
    def pBox(self,message):
        # Permutation selon le tableau P
        permuted_message = ""
        p = [
                16, 7, 20, 21,
                29, 12, 28, 17,
                1, 15, 23, 26,
                5, 18, 31, 10,
                2, 8, 24, 14,
                32, 27, 3, 9,
                19, 13, 30, 6,
                22, 11, 4, 25
            ]
        for i in p:
            permuted_message += message[i-1]
        return permuted_message

    def xor(self,message1, message2):
        # Convertir les chaînes binaires en entiers
        num1 = int(message1, 2)
        num2 = int(message2, 2)
        
        # Appliquer le XOR
        result = num1 ^ num2
        
        # Convertir le résultat en binaire et supprimer le préfixe "0b"
        return bin(result)[2:].zfill(len(message1))  # zfill pour maintenir la longueur d'origine

    

    def chiffrer(self,message=''):
        if self.tabKeysReady():
            try :
                if self.verifyKey(message):
                    message = self.iP(message)
                    index = 0
                    for index in range(16):
                        message = self.round(message,self.tabKeys[index])
                    
            except WrongKeyException:
                raise WrongKeyException("Le message doit être en binaire et avoir 64 bits")
            message = self.swap32(message)
            message = self.iIP(message)
            return message
    
    def dechiffrer(self,message=''):
        if self.tabKeysReady():
            try :
                if self.verifyKey(message):
                    message = self.iP(message)
                
                    for index in range(15 ,-1,-1):
                        message = self.round(message,self.tabKeys[index])                    
            except WrongKeyException:
                raise WrongKeyException("Le message doit être en binaire et avoir 64 bits")
            
            message = self.swap32(message)
            message = self.iIP(message)
            return message

        
    
    
        
        
   
    
    

