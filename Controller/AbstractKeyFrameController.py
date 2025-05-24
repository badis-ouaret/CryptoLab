from abc import ABC, abstractmethod
from Controller.KeyFrameManager import KeyFrameManager

# Classe de base pour tous les contrôleurs de fenêtres de clé (César, Vigenère, etc.)
class AbstractKeyFrameController(ABC):
    def __init__(self, chiffreur, key):# prend le chiffreur en paramettre et la clé.
        if not KeyFrameManager.set_active(self):
            return  # Une autre fenêtre est déjà ouverte

        self.chiffreur = chiffreur 
        self.frame = self.create_frame()# instancie la fenetre adequate(definit dans chaque controleur)
        self.frame.protocol("WM_DELETE_WINDOW", self.destroyFrame)#l'action lorseque on clique sur la croix 
        self.keyEntry = None#le champs de la clé dans l'interface (pas initialisé)
        
        self.ValidateButton = self.getValidateButton() # recupere le bouton de validation de l'interface de définition de la clé

        self.insererKey(key)# insert la clé dans le chiffreur(definit dans chaque controlleur)
        self.ValidateButton.configure(command=self.validateButtonAction)# definit l'action du bouton de validation(definit dans chaque controleur)

        self.frame.after(10, self.bring_to_front)#ramene la fenetre au premier plan lorseque celle ci est instancié et qu'on clique sur le bouton definir clé de la fenetre principale
        self.frame.mainloop()#main loop de la fenetre

    def bring_to_front(self):#ramene la fenetre au premier plan
        self.frame.lift()
        self.frame.focus_force()

    def destroyFrame(self):#detruit la fenetre correctement
        if self.frame:
            try:
                self.frame.destroy()
            except:
                pass
            finally:
                KeyFrameManager.clear()
                self.frame = None
    
    def insererKey(self,key):#definit comment inserer la clé dans le chiffreur (differente selon le controlleur de chaque fenetre et chiffreur)
        self.keyEntry = self.getKeyEntry()
        self.keyEntry.insert(0,key)


    @abstractmethod
    def create_frame(self):#definit quelle classe de fenetre instancier
        """Retourne une instance du frame graphique associé (à surcharger)."""
        pass

    @abstractmethod
    def getKeyEntry(self):# ramene les champs de definition de la clé(different selon chaque fenetre)
        """Retourne le champ de saisie de la clé (à surcharger)."""
        pass

    @abstractmethod
    def getValidateButton(self):#ramene le bouton de validation
        """Retourne le bouton de validation (à surcharger)."""
        pass

    @abstractmethod
    def validateButtonAction(self):#definit l'action du bouton de validaiton differente selon chaque fenetre et chiffreur
        """Définit le comportement à la validation (à surcharger)."""
        pass
