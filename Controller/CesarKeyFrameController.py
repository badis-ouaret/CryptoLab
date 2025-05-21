
# from View.Frames import defineCesarKeyFrame as fr
# from tkinter import messagebox

# class CesarKeyFrameController:
#     _instance = None  # Singleton

#     def __new__(cls, cesarChiffreur, key=""):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         else:
#             # Si déjà instancié, on ramène la fenêtre au premier plan
#             try:
#                 cls._instance.frame.lift()
#                 cls._instance.frame.focus_force()
#             except:
#                 pass
#             return cls._instance
#         return cls._instance

#     def __init__(self, cesarChiffreur, key=""):
#         if hasattr(self, "frame") and self.frame.winfo_exists():
#             # Ne pas réinitialiser si déjà initialisé
#             return

#         self.cesar = cesarChiffreur
#         self.frame = fr()
#         self.frame.protocol("WM_DELETE_WINDOW", self.destroyFrame)

#         self.keyEntry = self.frame.getKeyEntry()
#         self.ValidateButton = self.frame.getValidateButton()

#         self.keyEntry.insert(0, key)
#         self.ValidateButton.configure(command=self.validateButtonAction)

#         self.frame.after(10, lambda: self.frame.lift())  # Lève au premier plan
#         self.frame.mainloop()

#     def validateButtonAction(self):
#         key = self.keyEntry.get()
#         if key == "":
#             self.cesar.initialiser()
#             self.destroyFrame()
#         else:
#             try:
#                 self.cesar.setKey(int(key))
#                 self.destroyFrame()
#             except Exception as e:
#                 messagebox.showwarning(title="Avertissement", message=str(e))

#     def destroyFrame(self):
#         if self.frame is not None:
#             try:
#                 self.frame.destroy()
#             except:
#                 pass
#             finally:
#                 CesarKeyFrameController._instance = None
#                 self.frame = None

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