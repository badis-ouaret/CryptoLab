
from View.Frames import defineHillKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from Model.chiffreur import HillChiffreur
from tkinter import messagebox

class HillKeyFrameController(AbstractKeyFrameController):

    def insererKey(self, key):
        self.keyEntry = self.getKeyEntry()#retourne une liste d'entry,Entry Pour indiquer la taille de la matrice 
        self.listEntry,self.tailleMatEntry = self.keyEntry
        currentMat,currentMatTaille = key
        self.tailleMatEntry.insert(0,currentMatTaille)
        self.frame.creerMatrice()
        self.keyEntry = self.getKeyEntry()#retourne une liste d'entry,Entry Pour indiquer la taille de la matrice 
        self.listEntry,self.tailleMatEntry = self.keyEntry

        for i, row in enumerate(currentMat):
            for j, value in enumerate(row):
                index = i * currentMatTaille + j
                self.listEntry[index].insert(0, value)
    
      

    def create_frame(self):
        return fr()

    def getKeyEntry(self):
        return self.frame.getKeyEntry()#retourne une liste d'entry,Entry Pour indiquer la taille de la matrice 
    

    def getValidateButton(self):
        return self.frame.getValidateButton()

    def validateButtonAction(self):  
        self.keyEntry = self.getKeyEntry()#retourne une liste d'entry,Entry Pour indiquer la taille de la matrice 
        self.listEntry,self.tailleMatEntry = self.keyEntry
        taille = int(self.tailleMatEntry.get())

        matrice = []
        for i in range(taille):
            ligne =[
                int(entry.get())
                for entry in self.listEntry[i * taille : (i + 1) * taille]
            ]
            matrice.append(ligne)       
        try:
            self.chiffreur.setKey(matrice)
            self.destroyFrame()
        except Exception as e:
            messagebox.showwarning(title="Avertissement", message=str(e))