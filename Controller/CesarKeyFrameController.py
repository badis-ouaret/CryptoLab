
from View.Frames import defineCesarKeyFrame as fr
from tkinter import messagebox

class CesarKeyFrameController:
    def __init__(self, cesarChiffreur, key=""):
        self.frame = fr()  # instanciation de la fenêtre
        self.cesar = cesarChiffreur
        self.keyEntry = self.frame.getKeyEntry()  # appel via l'instance
        self.ValidateButton = self.frame.getValidateButton()
        
        self.keyEntry.insert(0, key)
        self.ValidateButton.configure(command=self.validateButtonAction)
        
        self.frame.mainloop()  # ici aussi : self.frame, pas self.keyFrame

   
        
        
    def validateButtonAction(self):
        key = self.keyEntry.get()
        if key == "":
            self.cesar.initialiser()
            self.frame.destroy()
        else:
            try:
                self.cesar.setKey(int(key))
                self.frame.destroy()
            except Exception as e:
                messagebox.showwarning(title="Avertissement", message=str(e))
    
    def destroyFrame(self):
        if self.frame != None:
            self.frame.destroy()
        self.frame = None


    #==========================================================