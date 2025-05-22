

from View.Frames import defineDESeKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from tkinter import messagebox

class DESKeyFrameController(AbstractKeyFrameController):
    def create_frame(self):
        return fr()

    def getKeyEntry(self):
        return self.frame.getKeyEntry()

    def getValidateButton(self):
        return self.frame.getValidateButton()

    def validateButtonAction(self):
        key = self.keyEntry.get()
        if key == "":
            self.chiffreur.initialiser()
            self.destroyFrame()
        else:
            try:
                while len(key) < 64:
                    key = '0'+key
                self.chiffreur.setKey(key)
                self.destroyFrame()
            except Exception as e:
                messagebox.showwarning(title="Avertissement", message=str(e))





