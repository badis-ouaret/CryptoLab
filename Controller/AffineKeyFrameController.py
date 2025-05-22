
from View.Frames import defineAffineKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from Model.chiffreur import CalculMatriciel 
from tkinter import messagebox

class AffineKeyFrameController(AbstractKeyFrameController):

    def insererKey(self, key):
        self.keyEntry = self.getKeyEntry()
        self.keyinversMod26Entry,self.decalageEntry = self.keyEntry
        keyinversMod26EntryCurrentVal,decalageEntryCurrentVal = key #key = [cleInvMod26,decalage]       
        self.keyinversMod26Entry.insert(0,keyinversMod26EntryCurrentVal) 
        self.decalageEntry.insert(0,decalageEntryCurrentVal)       

    def create_frame(self):
        return fr()

    def getKeyEntry(self):
        return self.frame.getKeyEntry()#return self.keyEntry, self.decalageEntry
    

    def getValidateButton(self):
        return self.frame.getValidateButton()

    def validateButtonAction(self):
        key26 = int(self.keyinversMod26Entry.get())
        decalage = int(self.decalageEntry.get())
        if key26 == "" or decalage =="":
            self.chiffreur.initialiser()
            self.destroyFrame()
        elif not CalculMatriciel.numInversibleModNum(key26,26):
            messagebox.showwarning(title="Avertissement", message="La clé doit être inversible modulo 26")
        else:
            try:
                self.chiffreur.setKey(key26,decalage)#(keymod26,decalage)
                self.destroyFrame()
            except Exception as e:
                messagebox.showwarning(title="Avertissement", message=str(e))




