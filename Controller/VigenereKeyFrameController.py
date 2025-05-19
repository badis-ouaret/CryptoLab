from View.Frames import defineVigenereKeyFrame as fr

class VigenereKeyFrameController:
    def __init__(self,vigenereChiffreur,key=""):
        self.frame = fr()
        self.vigenere = vigenereChiffreur()
        self.keyEntry = fr.getKeyEntry()
        self.ValidateButton =self.frame.getValidateButton()
        #doit permettre de recuperer la cle mise dans l'interface       
        self.keyEntry.insert(0,key)
        self.ValidateButton = self.frame.getValidateButton() 
        self.ValidateButton.configure(command=self.validateButtonAction)
        self.keyFrame.mainloop()


       
    def validateButtonAction(self):
        key = self.keyEntry.get()
        if key == "":
            self.vigenere.initialiser()
        else:
            try:
                self.vigenere.setKey(key)
                self.frame.destroy()
            except Exception as e:
                self.frame.messageAlerte(str(e),title="Erreur",buttonText="OK")