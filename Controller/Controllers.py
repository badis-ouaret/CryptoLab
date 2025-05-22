import View.Frames as fr
import Model.chiffreur as ch
import Controller.VigenereKeyFrameController as vigFrCont
import Controller.CesarKeyFrameController as cesFrCont
import Controller.PolybePlayfairKeyFrameController as polPlayFrCont
import Controller.DESKeyFrameController as DesFrCont
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
        # try :
        #     if method == "Cesar":
        #         if operation == "Chiffrer" :
        #             text = self.cesar.chiffrer(self.frame.getTextEntry().get("0.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.cesar.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)

        #     elif method == "Vigenere":
        #         if operation == "Chiffrer" :
        #             text = self.vigenere.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.vigenere.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
                
        #     elif method == "Playfair":
        #         if operation == "Chiffrer" :
        #             text = self.playfair.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.playfair.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
                
        #     elif method == "AmelioCesar":
        #         if operation == "Chiffrer" :
        #             text = self.amelioCesar.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.amelioCesar.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
                
        #     elif method == "Polybe":
                
        #         if operation == "Chiffrer" :
        #             text = self.polybe.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text) 
        #         else:
        #             text = self.polybe.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)               

        #     elif method == "Hill":
        #         if operation == "Chiffrer" :
        #             text = self.hill.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.hill.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #     elif method == "Affine":
        #         if operation == "Chiffrer" :
        #             text = self.affine.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.affine.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #     elif method == "Transpo":
        #         if operation == "Chiffrer" :
        #             text = self.transpo.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.transpo.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #     elif method == "DES":
                
        #         if operation == "Chiffrer" :
        #             text = self.DES.chiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        #         else:
        #             text = self.DES.dechiffrer(self.frame.getTextEntry().get("1.0", "end")) 
        #             self.frame.setResultEntryText(text)
        # except Exception as e:
        #         self.frame.messageAlerte(str(e),title="Erreur",buttonText="OK")#c'est juste pour deboguer à ne pas oublier de remettre comme avant

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
            elif method == "DES":
                textF =""
                if operation == "Chiffrer" :                    
                    text = self.messageFormatDesChiffrement(self.frame.getTextEntry().get("1.0", "end"))#retourne une liste de chaines de len bin 64bits
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

    def keyDefButtonFunction(self):
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
            self.keyFrame = vigFrCont.AmelioCesarKeyFrameController(self.amelioCesar)
            self.keyFrame = None
        elif method == "Polybe":
            self.keyFrame = polPlayFrCont.PolybePlayfairKeyFrameController(self.polybe,self.polybe.getKey())
            self.keyFrame = None
        elif method == "Hill":
            self.keyFrame = vigFrCont.HillKeyFrameController(self.hill)
            self.keyFrame = None
        elif method == "Affine":
            self.keyFrame = vigFrCont.AffineKeyFrameController(self.affine)
            self.keyFrame = None
        # elif method == "Transpo":
        #     self.keyFrame = vigFrCont.TranspoKeyFrameController(self.transpo)
        #     self.keyFrame = None
        elif method == "DES":
            self.keyFrame = DesFrCont.DESKeyFrameController(self.DES,self.DES.getKey())
            self.keyFrame = None
            



   
         


    def clearButtonAction2(self):
            self.frame.textEntry.delete("0.0", "end")
            self.frame.setResultEntryText("")
            self.frame.textEntry.focus_set()


    def messageFormatDesChiffrement(self,message):
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
    
    def messageFormatDesDechiffrement(self, message):
        return [message[i:i+64] for i in range(0, len(message), 64)]



        


   
    

                
        


    def go(self):
        self.frame.start()    
    


    



    