

from View.Frames import defineCesarKeyFrame as fr
from Controller.AbstractKeyFrameController import AbstractKeyFrameController
from tkinter import messagebox

class CesarKeyFrameController(AbstractKeyFrameController):
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
                self.chiffreur.setKey(int(key))
                self.destroyFrame()
            except Exception as e:
                messagebox.showwarning(title="Avertissement", message=str(e))