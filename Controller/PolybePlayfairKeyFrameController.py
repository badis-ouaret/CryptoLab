
from View.Frames import definePolybePlayfairKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from Model.chiffreur import PlayfairChiffreur
from tkinter import messagebox

class PolybePlayfairKeyFrameController(AbstractKeyFrameController):

    def insererKey(self, key):
        self.keyEntry = self.getKeyEntry()
        self.mainKeyEntry,self.jumle1Entry,self.jumle2Entry = self.keyEntry
        motCle,caractereJumle1,caractereJumle2 = key        
        self.jumle1Entry.insert(0,caractereJumle1)
        self.jumle2Entry.insert(0,caractereJumle2)
        #ce code est mal c'est juste pour forcer et aller vite (À REVOIR!!!!!!!!!)
        i=0
        for c in motCle:
            self.mainKeyEntry.insert(i,c) 
            i +=1                      
        #------------------------------------------------------------------
        self.frame.fillButton.invoke()



        

    def create_frame(self):
        if isinstance(self.chiffreur, PlayfairChiffreur):
            return fr(title="Playfair Key Frame")
        else:
            return fr(title="Polybe Key Frame")

    def getKeyEntry(self):
        return self.frame.getKeyEntry()#return self.keyEntry, self.lettresJumleesEntry1, self.lettresJumleesEntry2
    

    def getValidateButton(self):
        return self.frame.getValidateButton()

    def validateButtonAction(self):        
        keyCont = self.mainKeyEntry.get()
        jumle1Cont = self.jumle1Entry.get()
        jumle2Cont = self.jumle2Entry.get()        
        
        try:
            self.chiffreur.setKeys(keyCont,jumle1Cont,jumle2Cont)
            self.destroyFrame()
        except Exception as e:
            messagebox.showwarning(title="Avertissement", message=str(e))