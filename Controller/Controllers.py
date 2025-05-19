import View.Frames as fr
import Model.chiffreur as ch
import Controller.VigenereKeyFrameController as vigFr
import Controller.CesarKeyFrameController as cesFr
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
        self.DES = ch.DesChiffreur()
        self.keyFrame = None

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

    def keyDefButtonFunction(self):
        method = self.frame.getMethodeDeChiffrement()
        if self.keyFrame != None:
            self.keyFrame.destroy()
        if method == "Cesar":
            self.keyFrame = cesFr.CesarKeyFrameController(self.cesar)
            self.keyFrame = None
        elif method == "Vigenere":
            self.keyFrame = vigFr.VigenereKeyFrameController(self.vigenere)
            self.keyFrame = None
        elif method == "Playfair":
            self.keyFrame = vigFr.PlayfairKeyFrameController(self.playfair)
            self.keyFrame = None
        elif method == "AmelioCesar":
            self.keyFrame = vigFr.AmelioCesarKeyFrameController(self.amelioCesar)
            self.keyFrame = None
        elif method == "Polybe":
            self.keyFrame = vigFr.PolybeKeyFrameController(self.polybe)
            self.keyFrame = None
        elif method == "Hill":
            self.keyFrame = vigFr.HillKeyFrameController(self.hill)
            self.keyFrame = None
        elif method == "Affine":
            self.keyFrame = vigFr.AffineKeyFrameController(self.affine)
            self.keyFrame = None
        elif method == "Transpo":
            self.keyFrame = vigFr.TranspoKeyFrameController(self.transpo)
            self.keyFrame = None
        elif method == "DES":
            self.keyFrame = vigFr.DESKeyFrameController(self.DES)
            self.keyFrame = None
            



   
         


    def clearButtonAction2(self):
            self.frame.textEntry.delete("0.0", "end")
            self.frame.resultEntry.delete("0.0", "end")
            self.frame.textEntry.focus_set()
        
   
    

                
        


    def go(self):
        self.frame.start()    
    


    



    