
from View.Frames import defineCesarKeyFrame as fr

class CesarKeyFrameController:
    def __init__(self,cesarChiffreur,key=""):
        self.frame = fr()
        self.cesar = cesarChiffreur()
        self.keyEntry = self.frame.getKeyEntry()
        self.ValidateButton =self.frame.getValidateButton()
        #doit permettre de recuperer la cle mise dans l'interface
        
        self.keyEntry.insert(0,key)
        self.ValidateButton = self.frame.getValidateButton() 
        self.ValidateButton.configure(command=self.validateButtonAction)
        self.frame.mainloop()
    #Cesar #==========================================================
   
        
        
    def validateButtonAction(self):
        key = self.keyEntry.get()
        if key == "":
            self.cesar.initialiser()
        else:
            try:
                self.cesar.setKey(key)
                self.frame.destroy()
            except Exception as e:
                self.frame.messageAlerte(str(e),title="Erreur",buttonText="OK")
    
    def destroyFrame(self):
        if self.frame != None:
            self.frame.destroy()
        self.frame = None


    #==========================================================