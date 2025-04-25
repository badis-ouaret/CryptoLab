import customtkinter as ctk
from abc import ABC, abstractmethod

FRAME_WIDTH = 1200
FRAME_HEIGHT = 700

#--------------------------------------------
#MainFrame
MAIN_FRAME_BG_COLOR = "black"
#--------------------------------------------
#MENU
MENU_HEIGHT = FRAME_HEIGHT
MENU_WIDTH = 200
MENU_TEXT_COLOR = "white"
MENU_BG_COLOR = "black"
MENU_FONT = ("Arial", 16)
PADY_RADIO_MENU = 20
PADY_FIRST_RADIO_MENU = (80, PADY_RADIO_MENU)
PADX_RADIO_MENU = (10, 0)
#--------------------------------------------
# PanelDroit
RIGHT_PANEL_WIDTH = FRAME_WIDTH - MENU_WIDTH
RIGHT_PANEL_HEIGHT = FRAME_HEIGHT
RIGHT_PANEL_BG_COLOR = "white"
RIGHT_PANEL_FONT = ("Arial", 20)
RIGHT_PANEL_TEXT_COLOR = "black"
RIGHT_PANEL_TITLE_FONT = ("Arial", 40)
RIGHT_PANEL_TITLE_COLOR = "black"

OPTION_PANEL_HEIGHT = 70

PADY_RADIO_OPTION_PANEL = 20
OPTION_PANEL_BG_COLOR = "gray"
OPTION_PANEL_FONT = ("Arial", 16)
OPTION_PANEL_TEXT_COLOR = "white"
KEY_ENTRY_FONT = ("Arial", 16)
#--------------------------------------------
#boutons
BUTTON_BG_COLOR_HOVER = "gray"
BUTTON_BG_COLOR = "black"
BUTTON_TEXT_COLOR_HOVER = "white"
BUTTON_TEXT_COLOR = "white"
BUTTON_BORDER_COLOR = "black"
BUTTON_BORDER_WIDTH = 3
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 200
BUTTON_FONT = ("Arial", 16)
BUTTON_BORDER_COLOR_HOVER = "black"
BUTTON_BORDER_WIDTH_HOVER = 3

#--------------------------------------------


class ToolBox(ABC,ctk.CTk):

   
    
    @staticmethod
    def configureGrid(pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1}):

        for line,weight in dictR.items():
            pannel.grid_rowconfigure(line, weight=weight)
        for col,weight in dictC.items():
            pannel.grid_columnconfigure(col, weight=weight)
        
    
    @staticmethod
    def createTextsEntrys(pannel,ligne = 3,colonne = 0,textLabel = "Texte en clair",resultLabel = "Texte chiffré",entryWidth = 300,entryHeight = 200,entryBorderColor = "black",entryBorderWidth=3, entryFgColor = "white" ,entryTextColor = RIGHT_PANEL_TEXT_COLOR,entryFont = RIGHT_PANEL_FONT,label1Text = "Texte en clair",label2Text = "Texte chiffré",label1Font = RIGHT_PANEL_FONT,label2Font = RIGHT_PANEL_FONT,label1TextColor= RIGHT_PANEL_TEXT_COLOR,label2TextColor = RIGHT_PANEL_TEXT_COLOR):
        textLabel = ctk.CTkLabel(pannel,text=label1Text,font=label1Font, text_color=label1TextColor)
        textLabel.grid(row=ligne-1, column=colonne+1, pady=0, padx=(10,0), sticky="nesw")

        resultLabel = ctk.CTkLabel(pannel,text=label2Text,font=label2Font, text_color=label2TextColor)
        resultLabel.grid(row=ligne-1, column=colonne+3, pady=0, padx=(0, 10), sticky="nesw")
        
        textEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        textEntry.grid(row=ligne, column=colonne, pady=30, padx=(30, 0),columnspan=2, sticky="nesw")
        textEntry.focus_set()

        resultEntry = ctk.CTkTextbox(pannel, width=entryWidth,height=entryHeight,font=entryFont, text_color=entryTextColor,wrap="word",activate_scrollbars=True,fg_color=entryFgColor,border_width=entryBorderWidth,border_color=entryBorderColor)
        resultEntry.grid(row=ligne, column=colonne+3, pady=30, padx=(0, 30),columnspan=2, sticky="nesw")
        resultEntry.configure(state="disabled")

        return textLabel,resultLabel,textEntry,resultEntry
    



class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{FRAME_WIDTH}x{FRAME_HEIGHT}")

        self.choixMethode = ctk.StringVar(value="Cesar")
        self.choixOperation = ctk.StringVar(value="Chiffrer")

        self.main_frame = ctk.CTkFrame(self, fg_color=MAIN_FRAME_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        # Panel de menu
        self.menuPanel = ctk.CTkFrame(self.main_frame, width=MENU_WIDTH, height=MENU_HEIGHT, fg_color=MENU_BG_COLOR)
        self.menuPanel.pack(side="left", fill="y")

        # Liste des méthodes de chiffrement
        chiffrement_methods = [
            ("Cesar", "Cesar"),
            ("Vigenère", "Vigenere"),
            ("Cesar amélioré", "AmelioCesar"),
            ("Polybe", "Polybe"),
            ("Playfair", "Playfair"),
            ("Hill", "Hill"),
            ("Affine", "Affine"),
            ("Transposition", "Transpo")
        ]
        
        # Création dynamique des boutons radio pour les méthodes de chiffrement
        compte = 0
        for text, value in chiffrement_methods:
            compte +=1
            if compte == 1:
                self.radio = ctk.CTkRadioButton(self.menuPanel,
                                                text=text, 
                                                variable=self.choixMethode, 
                                                value=value, 
                                                width=MENU_WIDTH, 
                                                text_color=MENU_TEXT_COLOR, 
                                                font=MENU_FONT)
                self.radio.pack(padx=PADX_RADIO_MENU, pady=PADY_FIRST_RADIO_MENU)
            else:
                self.radio =ctk.CTkRadioButton(self.menuPanel,
                               text=text, 
                               variable=self.choixMethode, 
                               value=value, 
                               width=MENU_WIDTH, 
                               text_color=MENU_TEXT_COLOR, 
                               font=MENU_FONT).pack(padx=PADX_RADIO_MENU, pady=PADY_RADIO_MENU)
                


        # Panel de droite
        self.right_panel = ctk.CTkFrame(self.main_frame, height=RIGHT_PANEL_HEIGHT, width=RIGHT_PANEL_WIDTH, fg_color=RIGHT_PANEL_BG_COLOR)
        self.right_panel.pack(side="left", fill="both", expand=True)
            # Panel de choix d'opération
        self.choixOperationPanel = ctk.CTkFrame(self.right_panel, corner_radius=0, fg_color=OPTION_PANEL_BG_COLOR, height=OPTION_PANEL_HEIGHT)
        self.choixOperationPanel.pack(side="top", fill="x")

        self.centerChoixOperationPanel = ctk.CTkFrame(self.choixOperationPanel, fg_color=OPTION_PANEL_BG_COLOR)
        self.centerChoixOperationPanel.place(relx=0.5, rely=0.5, anchor="center")

        self.radioChiffrer = ctk.CTkRadioButton(self.centerChoixOperationPanel, text="Chiffrer", variable=self.choixOperation, value="Chiffrer", text_color=OPTION_PANEL_TEXT_COLOR, font=OPTION_PANEL_FONT)
        self.radioDechiffrer = ctk.CTkRadioButton(self.centerChoixOperationPanel, text="Déchiffrer", variable=self.choixOperation, value="Dechiffrer", text_color=OPTION_PANEL_TEXT_COLOR, font=OPTION_PANEL_FONT)

        self.radioChiffrer.pack(side="left", padx=10, pady=PADY_RADIO_OPTION_PANEL)
        self.radioDechiffrer.pack(side="left", padx=10, pady=PADY_RADIO_OPTION_PANEL)
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Panel principal++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.panelPrincipal = ctk.CTkFrame(self.right_panel,fg_color=RIGHT_PANEL_BG_COLOR,corner_radius=0)
        self.panelPrincipal.pack(side="bottom", fill="both", expand=True)
        self.operationButton,self.clearButton,self.textEntry,self.resultEntry,self.textLabel,self.resultLabel,self.title = self.mainPart(self.panelPrincipal,title="Chiffrement")        
        self.clearButton.configure(command=self.clearButtonAction2)        
        self.keyDefButton = self.createButton(self.panelPrincipal, text="Définir la clé",ligne=1,colonne=2,pady=(0,20))
        
        self.update_panel_for_method()
        self.choixMethode.trace_add("write",self.update_panel_for_method)
        #self.update_panel_for_operation()
        self.traceOperationId = self.choixOperation.trace_add("write",self.update_panel_for_operation)
            #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #Gestion de l'affichage selon les boutons radios selectionnés
    def update_panel_for_method(self, *args):         
        method = self.choixMethode.get()

        if method == "Cesar":
            self.title.configure(text = "Chiffrement de César")
        elif method == "Vigenere":
            self.title.configure(text = "Chiffrement de Vigenère")
        elif method == "Playfair":
            self.title.configure(text = "Chiffrement de Playfair")
        elif method == "AmelioCesar":
            self.title.configure(text = "Chiffrement de César Amélioré")
        elif method == "Polybe":
            self.title.configure(text = "Chiffrement de Polybe")
        elif method == "Hill":
            self.title.configure(text = "Chiffrement de Hill")
        elif method == "Affine":
            self.title.configure(text = "Chiffrement Affine")
        elif method == "Transpo":
            self.title.configure(text = "Chiffrement par Transposition")

    def update_panel_for_operation(self,*args):
        self.textLabel.configure(text="Texte en clair" if self.choixOperation.get() == "Chiffrer" else "Texte chiffré")
        self.resultLabel.configure(text="Texte chiffré" if self.choixOperation.get() == "Chiffrer" else "Texte en clair")
        self.operationButton.configure(text="Chiffrer" if self.choixOperation.get() == "Chiffrer" else "Déchiffrer")
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








    

    #Methodes de creation de panel et de configuration de la grille ============================
    def createPanel(self):
        panel = ctk.CTkFrame(self.panelPrincipal,corner_radius=0, fg_color="white")
        panel.pack(side="bottom",fill="both",expand=True)
        return panel
    

   
    
   
    
    def mainPart(self,pannel,title = "",titleFont = RIGHT_PANEL_TITLE_FONT,titleTextColor = RIGHT_PANEL_TITLE_COLOR,isGrid = True,dictC ={0: 0, 1: 1, 2: 1, 3: 1},dictR={}):
        titleFrame = ctk.CTkFrame(pannel.master,fg_color=pannel.cget("fg_color") ,corner_radius=0,height=100)
        titleFrame.pack(side="top",fill="x")
        titre = ctk.CTkLabel(titleFrame, text=title, font=titleFont, text_color=titleTextColor)
        titre.pack(expand = True,anchor = 'center' ,pady=30) 
        if isGrid:
            self.configureGrid(pannel,dictC=dictC,dictR=dictR)

        textLabel,resultLabel,textEntry,resultEntry = self.createTextsEntrys(pannel)    

        operationButton = self.createButton(pannel, text="Chiffrer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",ligne = 4,colonne = 2,padx=(0, 10),pady=(20,10))
        clearButton = self.createButton(pannel, text="Effacer", font=RIGHT_PANEL_FONT, text_color="white",fg_color="black",height=40,hover_color="gray",ligne = 5,colonne = 2,padx=(0, 10),pady=(20,10))
        
        
        return operationButton,clearButton,textEntry,resultEntry,textLabel,resultLabel,titre
    #=====================================================================
    
    #Methodes gestion boutons ====================================================================
    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)
    def clearButtonAction(self,textEntry,resultEntry,cleEntry):
        textEntry.delete("0.0", "end")
        resultEntry.delete("0.0", "end")
        cleEntry.delete(0, "end")
        textEntry.focus_set()
    
    def clearButtonAction2(self):
        self.textEntry.delete("0.0", "end")
        self.resultEntry.delete("0.0", "end")
        self.textEntry.focus_set()
    #=======================================================================

    #Methodes pannel des entrées et des boutons ==================================================

    def only_numbers(self,char):
        return char.isdigit()
    
    def only_alphabetic(self,char):
        return char.isalpha() and char.isascii()


class keyType1Frame(ctk.CTk):#cesar,vigenere,polybe,playfair
    def __init__(self):
        super().__init__()
        self.geometry("400x100")
        self.resizable(False, False)        
        self.main_frame = ctk.CTkFrame(self, fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)
        self.configureGrid(self.main_frame)
        keyEntry = self.createKeyEntry(self.main_frame)
    
    def createKeyEntry(self,pannel,ligne = 1,colonne = 2,validate = "key",vcmd = None,labelFont = RIGHT_PANEL_FONT,labelTextColor = RIGHT_PANEL_TEXT_COLOR ,entryFont = KEY_ENTRY_FONT,    entryTextColor = RIGHT_PANEL_TEXT_COLOR):
        cleLabel = ctk.CTkLabel(pannel, text="Clé", font=labelFont, text_color=labelTextColor)
        cleLabel.grid(row=ligne, column=colonne-1, pady=30, padx=(0, 10), sticky="e")

        cleEntry = ctk.CTkEntry(pannel, width=300,height=35,font=entryFont, text_color=entryTextColor ,validate = validate ,validatecommand=vcmd)
        cleEntry.grid(row=ligne, column=colonne, pady=30 ,padx=0, sticky="nesw")
        return cleEntry
    
    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1}):

        for line,weight in dictR.items():
            pannel.grid_rowconfigure(line, weight=weight)
        for col,weight in dictC.items():
            pannel.grid_columnconfigure(col, weight=weight)




class defineAmelioCesarKeyFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=RIGHT_PANEL_BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)
        self.configureGrid(self.main_frame,lineWay=True,nbrLine=6,nbrCol=10,lineVal=1,colVal=1)
        self.LETTRE_DE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lettresRestantes = self.LETTRE_DE_ALPHABET 
        vcmd = (self.register(self.gestionDesLettres),'%P','%s') 
        self.entryDict = {}    
        line = 0
        col = 0
        for c in range(ord('A'),ord('Z')+1):
            self.letter = ctk.CTkLabel(self.main_frame, text=chr(c)+" :", font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR)
            self.letter.grid(row=line, column=col, pady=10, padx=(20, 0), sticky="w")

            self.Entry = ctk.CTkEntry(self.main_frame,width=35,height=35,font=RIGHT_PANEL_FONT, text_color=RIGHT_PANEL_TEXT_COLOR ,validate = "key" ,validatecommand=vcmd)
            self.Entry.grid(row=line, column=col+1, pady=10 ,padx=(0,0), sticky="w")

            self.entryDict[c] = self.Entry

            col += 2
            if col == 10 :
                line = line +1
                col = 0
    
        self.buttonFrame = ctk.CTkFrame(self,fg_color=RIGHT_PANEL_BG_COLOR,corner_radius=0)
        self.buttonFrame.pack(side="bottom",fill="x")
        self.configureGrid(self.buttonFrame,lineWay=True,nbrLine=2,nbrCol=3,lineVal=1,colVal=1)
        self.submitButton = self.createButton(self.buttonFrame, text="Valider",ligne=0,colonne=1,pady =10)
        self.clearButton = self.createButton(self.buttonFrame, text="Effacer",command=self.clearButtonAction,ligne= 1,colonne=1,pady=10)

    def createButton(self,panel, text="Bouton", font=BUTTON_FONT, text_color=BUTTON_TEXT_COLOR,fg_color=BUTTON_BG_COLOR,height=BUTTON_HEIGHT,hover_color=None,command=lambda: None,ligne = 4,colonne = 2,padx=(0, 10),pady=(100,0)):
        button = ctk.CTkButton(panel,text=text, font=font, text_color=text_color,fg_color=fg_color,height=height,hover_color=hover_color,command=command)
        button.grid(row=ligne, column=colonne, pady=pady, padx=padx, sticky="nesw")
        button.bind("<Enter>", lambda event: self.buttonOnEnter(button))
        button.bind("<ButtonRelease-1>", lambda event: self.buttonOnEnter(button)) 
        button.bind("<Leave>", lambda event: self.buttonOnLeave(button))
        return button  

    def buttonOnEnter(self,button,fg_color=BUTTON_BG_COLOR_HOVER, text_color=BUTTON_TEXT_COLOR_HOVER, border_color=BUTTON_BORDER_COLOR_HOVER,border_width=BUTTON_BORDER_WIDTH_HOVER,event=None):
        button.configure(fg_color=fg_color, text_color=text_color, border_color=border_color,border_width=border_width)
    def buttonOnLeave(self,button,fg_color=BUTTON_BG_COLOR, text_color=BUTTON_TEXT_COLOR,event=None):        
        button.configure(fg_color=fg_color, text_color=text_color)
    
    def clearButtonAction(self):
        for entry in self.entryDict.values():
            entry.delete(0, "end")
        self.lettresRestantes = self.LETTRE_DE_ALPHABET
        self.entryDict[ord('A')].focus_set()


        
    

    
    def configureGrid(self,pannel,dictR = {},dictC={0: 0, 1: 1, 2: 1, 3: 1},nbrLine=0,nbrCol = 0,lineWay = False,lineVal = 0,colVal = 0):
        if not lineWay :
            for line,weight in dictR.items():
                pannel.grid_rowconfigure(line, weight=weight)
            for col,weight in dictC.items():
                pannel.grid_columnconfigure(col, weight=weight)
        else:
            for i in range(nbrLine):
                pannel.grid_rowconfigure(i, weight=lineVal)
            for i in range(nbrCol):
                pannel.grid_columnconfigure(i, weight=colVal)

    def gestionDesLettres(self,lettreApres,lettreAvant):

        if (lettreApres in self.lettresRestantes) and len(lettreApres) <=1 :
            self.lettresRestantes.remove(lettreApres)
            return True
        elif lettreApres == "" and lettreAvant.isalpha() and len(lettreAvant) == 1 and lettreAvant.isascii() and lettreAvant.isupper():
            self.lettresRestantes.append(lettreAvant)
            return True
        else:
            return False

    



    
if __name__ == "__main__":
    app = defineAmelioCesarKeyFrame()
    app.mainloop()
