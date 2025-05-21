from View.Frames import defineVigenereKeyFrame as fr

from View.Frames import defineVigenereKeyFrame as fr

class VigenereKeyFrameController:
    def __init__(self, vigenereChiffreur, key=""):
        self.frame = fr()
        self.vigenere = vigenereChiffreur()
        self.keyEntry = self.frame.getKeyEntry()
        self.ValidateButton = self.frame.getValidateButton()
        
        self.keyEntry.insert(0, key)
        self.ValidateButton.configure(command=self.validateButtonAction)
        
        self.frame.mainloop()



       
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