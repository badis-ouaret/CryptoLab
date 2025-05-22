
from View.Frames import defineAmelioCesarKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from Model.chiffreur import AmelioredCesarChiffreur
from tkinter import messagebox

class AmelioCesarKeyFrameController(AbstractKeyFrameController):

    def insererKey(self, key):
        self.keyEntry = self.getKeyEntry()#retourne le dictionnaire contenant les entry l'id est la lettre ex 'A'
        for k,v in key.items():
            self.keyEntry.get(k).insert(0,v)      

    def create_frame(self):
        return fr()

    def getKeyEntry(self):
        return self.frame.getKeyEntry()##retourne le dictionnaire contenant les entry l'id est la lettre ex 'A'    

    def getValidateButton(self):
        return self.frame.getValidateButton()

    def validateButtonAction(self):  
        self.keyEntry = self.getKeyEntry()
        dico = {}

        try:
            for v in self.keyEntry.values():
                if v.get() == '' or v.get() == "":
                    raise ValueError("Vous devez faire correspondre chaque lettre à une autre lettre.")
            for k,v in self.keyEntry.items():
                dico[v.get()]=k        
            self.chiffreur.setKey(dico)
            self.destroyFrame()
        except Exception as e:
            messagebox.showwarning(title="Avertissement", message=str(e))