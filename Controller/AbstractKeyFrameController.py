from abc import ABC, abstractmethod
from Controller.KeyFrameManager import KeyFrameManager

# Classe de base pour tous les contrôleurs de fenêtres de clé (César, Vigenère, etc.)
class AbstractKeyFrameController(ABC):
    def __init__(self, chiffreur, key):
        if not KeyFrameManager.set_active(self):
            return  # Une autre fenêtre est déjà ouverte

        self.chiffreur = chiffreur
        self.frame = self.create_frame()
        self.frame.protocol("WM_DELETE_WINDOW", self.destroyFrame)
        self.keyEntry = None
        
        self.ValidateButton = self.getValidateButton()

        self.insererKey(key)
        self.ValidateButton.configure(command=self.validateButtonAction)

        self.frame.after(10, self.bring_to_front)
        self.frame.mainloop()

    def bring_to_front(self):
        self.frame.lift()
        self.frame.focus_force()

    def destroyFrame(self):
        if self.frame:
            try:
                self.frame.destroy()
            except:
                pass
            finally:
                KeyFrameManager.clear()
                self.frame = None
    
    def insererKey(self,key):
        self.keyEntry = self.getKeyEntry()
        self.keyEntry.insert(0,key)


    @abstractmethod
    def create_frame(self):
        """Retourne une instance du frame graphique associé (à surcharger)."""
        pass

    @abstractmethod
    def getKeyEntry(self):
        """Retourne le champ de saisie de la clé (à surcharger)."""
        pass

    @abstractmethod
    def getValidateButton(self):
        """Retourne le bouton de validation (à surcharger)."""
        pass

    @abstractmethod
    def validateButtonAction(self):
        """Définit le comportement à la validation (à surcharger)."""
        pass
