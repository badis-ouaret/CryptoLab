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
    
    
