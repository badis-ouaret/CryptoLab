import View.Frames as fr
import Model.chiffreur as ch
class MainController():
    
    def __init__(self):
        self.frame = fr.Interface()
        self.cesar = ch.CesarChiffreur()
        self.vigenere = ch.VigenereChiffreur()
        self.amelioCesar = ch.AmelioredCesarChiffreur()
        self.polybe=ch.PoybeChiffreur()
        self.playfair = ch.PlayfairChiffreur()
        self.affine = ch.AffineChiffreur()
        self.hill = ch.HillChiffreur()
        self.transpo = ch.TranspositionChiffreur()
        self.DES = ch.DESChiffreur()

        self.frame.keyDefButton.configure(command=self.keyDefButtonFunction)        
        self.frame.operationButton.configure(command=self.operationButtonFunction)
        self.frame.clearButton.configure(command=self.clearButtonAction2)

        



    #  #geters ========================================
    # getMethodeDeChiffrement(self):
    # getOperation(self):   
    # getTextEntry(self): 
    # getResultEntry(self):
    # messageAlerte(self,message,title="Erreur",buttonText="OK"):
    # #==========================================================
    # #seters ===================================================
    # setResultEntryText(self,text)  
    # #==========================================================

        


    
    def keyDefButtonFunction(self):
        print("bonjour")
    def operationButtonFunction(self):
        method = self.frame.getMethodeDeChiffrement()
        operation = self.frame.getOperation()
        try :
            if method == "Cesar":
                if operation == "Chiffrer" :
                    text = self.cesar.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
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
            elif method == "Transpo":
                if operation == "Chiffrer" :
                    text = self.transpo.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                    self.frame.setResultEntryText(text)
                else:
                    text = self.transpo.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                    self.frame.setResultEntryText(text)
            elif method == "DES":
                
                if operation == "Chiffrer" :
                    text = self.DES.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                    self.frame.setResultEntryText(text)
                else:
                    text = self.DES.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
                    self.frame.setResultEntryText(text)
        except Exception as e:
                self.frame.messageAlerte(str(e),title="Erreur",buttonText="OK")



    def clearButtonFunction(self):
        method = self.frame.getMethodeDeChiffrement()
        operation = self.frame.getOperation()
        if method == "Cesar":
            self.cesar.initialiser()
        elif method == "Vigenere":
            self.vigenere.initialiser()
        elif method == "Playfair":
            self.playfair.initialiser()
        elif method == "AmelioCesar":
            self.amelioCesar.initialiser()
        elif method == "Polybe":
            self.polybe.initialiser()
        elif method == "Hill":
            self.hill.initialiser()
        elif method == "Affine":
            self.affine.initialiser()
        elif method == "Transpo":
            self.transpo.initialiser()
        elif method == "DES":
            self.DES.initialiser()

         


    def clearButtonAction2(self):
            self.frame.textEntry.delete("0.0", "end")
            self.frame.resultEntry.delete("0.0", "end")
            self.frame.textEntry.focus_set()
            self.clearButtonFunction()


    def miniControllerCesarKeyFrame(self,key):
        #doit permettre de recuperer la cle mise dans l'interface
        print()

    def go(self):
        self.frame.start()    
    
