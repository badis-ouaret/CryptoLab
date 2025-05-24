import View.Frames as fr
import Model.chiffreur as ch
# importation des controllers
import Controller.VigenereKeyFrameController as vigFrCont
import Controller.CesarKeyFrameController as cesFrCont
import Controller.PolybePlayfairKeyFrameController as polPlayFrCont
import Controller.AffineKeyFrameController as affinCont
import Controller.DESKeyFrameController as DesFrCont
import Controller.HillKeyFrameController as HillFrCont
import Controller.AmelioCesarKeyFrame as AmelioCesarFrCont
#========================================================================
class MainController():
    
    def __init__(self):

        self.frame = fr.Interface()#instanciation de la fenetre principale
        # instanciation des chiffreurs
        self.cesar = ch.CesarChiffreur()
        self.vigenere = ch.VigenereChiffreur()
        self.amelioCesar = ch.AmelioredCesarChiffreur()
        self.polybe=ch.PoybeChiffreur()
        self.playfair = ch.PlayfairChiffreur()
        self.affine = ch.AffineChiffreur()
        self.hill = ch.HillChiffreur()
        self.transpo = ch.TranspositionChiffreur()
        self.DES = ch.DesChiffreur()
        #======================================================
        self.keyFrame = None
        # importation des boutons principaux de l'interface pour gerer leurs fonctionnements.
        self.frame.keyDefButton.configure(command=self.keyDefButtonFunction)        
        self.frame.operationButton.configure(command=self.operationButtonFunction)
        self.frame.clearButton.configure(command=self.clearButtonAction2)



    
    
    def operationButtonFunction(self):# definie le role du bouton chiffrer/dechiffrer selon la methode de chiffrement et l'operation(chiffrer dechiffrer)
            method = self.frame.getMethodeDeChiffrement() # methode selectionnée
            operation = self.frame.getOperation()# operation choisie
        
            try:
                if method == "Cesar":
                    if operation == "Chiffrer" :
                        text = self.cesar.chiffrer(self.frame.getTextEntry().get("0.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.cesar.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)

                elif method == "Vigenere":
                    if operation == "Chiffrer" :
                        text = self.vigenere.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.vigenere.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    
                elif method == "Playfair":
                    if operation == "Chiffrer" :
                        text = self.playfair.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.playfair.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    
                elif method == "AmelioCesar":
                    if operation == "Chiffrer" :
                        text = self.amelioCesar.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.amelioCesar.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    
                elif method == "Polybe":
                    
                    if operation == "Chiffrer" :
                        text = self.polybe.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text) 
                    else:
                        text = self.frame.getTextEntry().get("1.0", "end")
                        if not all(c in "01234" or c.isspace() for c in text) :
                            raise Exception("Le message à déchiffrer doit être de taille divisible par 2 ne contient que des caractères numeriques entre 0 et 4 ou des éspaces")
                        text = self.polybe.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)               

                elif method == "Hill":
                    if operation == "Chiffrer" :
                        text = self.hill.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.hill.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                elif method == "Affine":
                    if operation == "Chiffrer" :
                        text = self.affine.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                    else:
                        text = self.affine.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                        self.frame.setResultEntryText(text)
                # elif method == "Transpo":
                #     if operation == "Chiffrer" :
                #         text = self.transpo.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                #         self.frame.setResultEntryText(text)
                #     else:
                #         text = self.transpo.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                #         self.frame.setResultEntryText(text)
                # il manque l'interface
                elif method == "DES":
                    textF =""
                    if operation == "Chiffrer" :                    
                        text = self.messageFormatDesChiffrement(self.frame.getTextEntry().get("1.0", "end"))#retourne une liste de chaines bin de len  64bits
                        for m in text:
                            textF += self.DES.chiffrer(m) 
                        self.frame.setResultEntryText(textF)
                    else:
                        text = self.messageFormatDesDechiffrement(self.frame.getTextEntry().get("1.0", "end"))
                        i = 0
                        for m in text:
                            if len(m)==64:                                             
                                decrypted_message = self.DES.dechiffrer(m)
                                textF += "".join(chr(int(decrypted_message[i:i+8], 2)) for i in range(0, len(decrypted_message), 8)) 
                        self.frame.setResultEntryText(textF)
            except Exception as e:
                    self.frame.messageAlerte(str(e),title="Erreur",buttonText="OK")

    def keyDefButtonFunction(self):# affiche l'iterface de definition de la clé selon la methode choisie(bouton definir cle)
        method = self.frame.getMethodeDeChiffrement()
        if self.keyFrame != None:
            self.keyFrame.destroyFrame()
        if method == "Cesar":
            self.keyFrame = cesFrCont.CesarKeyFrameController(self.cesar,str(self.cesar.getKey()))
            self.keyFrame = None
        elif method == "Vigenere":
            self.keyFrame = vigFrCont.VigenereKeyFrameController(self.vigenere,self.vigenere.getKey())
            self.keyFrame = None
        elif method == "Playfair":
            self.keyFrame = polPlayFrCont.PolybePlayfairKeyFrameController(self.playfair,self.playfair.getKey())
            self.keyFrame = None
        elif method == "AmelioCesar":
            self.keyFrame = AmelioCesarFrCont.AmelioCesarKeyFrameController(self.amelioCesar,self.amelioCesar.getKey())
            self.keyFrame = None
        elif method == "Polybe":
            self.keyFrame = polPlayFrCont.PolybePlayfairKeyFrameController(self.polybe,self.polybe.getKey())
            self.keyFrame = None
        elif method == "Hill":
            self.keyFrame = HillFrCont.HillKeyFrameController(self.hill,self.hill.getKey())
            self.keyFrame = None
        elif method == "Affine":
            self.keyFrame = affinCont.AffineKeyFrameController(self.affine,self.affine.getKey())
            self.keyFrame = None
        # elif method == "Transpo":
        #     self.keyFrame = vigFrCont.TranspoKeyFrameController(self.transpo)
        #     self.keyFrame = None
        elif method == "DES":
            self.keyFrame = DesFrCont.DESKeyFrameController(self.DES,self.DES.getKey())
            self.keyFrame = None
            



   
         


    def clearButtonAction2(self): # action du bouton effacer
            self.frame.textEntry.delete("0.0", "end")
            self.frame.setResultEntryText("")
            self.frame.textEntry.focus_set()


    def messageFormatDesChiffrement(self,message):# transforme les mots de 8 caracteres en chaine binaire de 8 bits
        while len(message)%8 !=0:
            message +=' ' 
        messageTab=[]
        messageBinTab = []
        i=0
        while i < len(message):
            messageTab.append(message[i:i+8])
            i +=8
        for m in messageTab:      
            messageBin = "".join(bin(ord(caractere))[2:].zfill(8) for caractere in m)
            messageBinTab.append(messageBin)
        return messageBinTab
    
    def messageFormatDesDechiffrement(self, message):#transforme les chaines de 64 bits binaires en mots de 8 lettres corespondants.
        if len(message)%64 != 0 :
            raise Exception("Le message à dechiffrer doit être entierement en binaire. Et sa taille doit être un multiple de 64")
        return [message[i:i+64] for i in range(0, len(message), 64)]



        


   
    

                
        


    def go(self):
        self.frame.start()    
    


    



    